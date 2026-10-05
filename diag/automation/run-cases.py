"""Plays the four protocols of KSP Diag - Floating Origin.

It drives KSP through KSP-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-MCPServer and KSP Diag - Floating Origin installed,
copy Diag3-Rover.craft into the Ships/SPH folder of a sandbox game with no other craft landed around the Space
Center, Diag3-Rocket.craft into its Ships/VAB folder, and approach-kerbin.sfs into the same game, wait for the
main menu, then run:

    python run-cases.py --folder <your sandbox game> --cases 1 2 4 3 --out out

Case 1: the rover on the runway, brakes on, a quicksave, then three quickloads ten seconds apart, a record after
each. Case 2: the sounding rocket on the launchpad, a record; SAS on, full throttle, launched, a record once
the frame is no longer rotating; fallen back, a record once it rotates again, before the crash; the altitude
of both switches is written down. Case 3: approach-kerbin.sfs, a record; north to 100 m from the capsule, a
record; south until the capsule is 2.7 km away and unloaded, a record; on south until the origin moves, a
record. Case 4: the rover on the runway, brakes on, a record; to the far end of the runway, a record; back to
where it started, a record.

The cases run in the order given, case 3 last: the parked craft of its save stays in the game, and a craft
launched after it would find that craft within range, the origin held still. It writes every line to
lines.json, takes a screenshot of the table after each case, and quits KSP (unless --keep-running is given).
The window of the instrument is hidden once the flight opens, so that the scene shows, and shown only for
its screenshots.
"""
import argparse
import json
import os
import time
import urllib.request

URL = None


def call(tool, **args):
    """Calls one tool of KSP-MCPServer and returns its answer, decoded from JSON when it is JSON."""
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    request = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=900) as response:
        result = json.loads(response.read())["result"]
    text = result["content"][0].get("text", "") if result["content"] else ""
    if result.get("isError"):
        raise RuntimeError(tool + ": " + text)
    try:
        answer = json.loads(text)
    except ValueError:
        return text
    # The tools another mod adds answer inside "returned".
    if isinstance(answer, dict) and list(answer) == ["returned"]:
        return answer["returned"]
    return answer


def log(*parts):
    print(time.strftime("%H:%M:%S"), *parts, flush=True)


def record(case, step, rows):
    line = call("floatingorigin_record")
    rows.append(dict(case=case, step=step, line=line))
    log("  case %d, %-22s frame %-9s origin distance %8.1f m  shifts %s  last shift %s" % (
        case, step, "Rotating" if line.get("RotatingFrame") else "Inertial", line["OriginDistance"],
        line["Shifts"], line.get("LastShift")))


def other_craft():
    """The landed craft other than the one flown, with its distance."""
    others = [v for v in call("list_vessels") if not v["active"] and v["situation"] in ("LANDED", "PRELAUNCH")]
    if len(others) != 1:
        raise RuntimeError("expected one other landed craft, found %d" % len(others))
    return others[0]


def launch_rover(folder):
    call("open_game", folder=folder)
    state = call("launch_vessel", craft="SPH/Diag3-Rover.craft", site="Runway")
    call("set_controls", brakes=True)
    call("wait", seconds=5)
    return state["vessel"]


def case1(folder, rows):
    launch_rover(folder)
    call("floatingorigin_clear")
    call("floatingorigin_show_window", visible=False)
    call("save_game", save="quicksave")
    for i in range(1, 4):
        call("wait", seconds=10)
        call("load_save", folder=folder, save="quicksave")
        call("wait", seconds=3)
        record(1, "quickload %d" % i, rows)


def rotating():
    return call("floatingorigin_read")["live"]["RotatingFrame"]


def wait_for_frame(rotating_wanted, limit):
    """Waits until the frame is rotating, or not, as wanted; returns the altitude of the switch."""
    start = time.time()
    while time.time() - start < limit:
        if rotating() == rotating_wanted:
            return call("get_state")["vessel"]["altitude"]
        time.sleep(0.2)
    raise RuntimeError("the frame did not switch within %d s" % limit)


def case2(folder, rows):
    call("open_game", folder=folder)
    call("launch_vessel", craft="VAB/Diag3-Rocket.craft", site="LaunchPad")
    call("floatingorigin_clear")
    call("floatingorigin_show_window", visible=False)
    call("wait", seconds=3)
    record(2, "on the pad", rows)
    call("set_flight", throttle=1, sas=True)
    call("stage")
    up = wait_for_frame(False, 600)
    record(2, "inertial", rows)
    log("  case 2: the frame stopped rotating at %.0f m" % up)
    down = wait_for_frame(True, 1800)
    record(2, "rotating again", rows)
    log("  case 2: the frame rotated again at %.0f m" % down)
    rows.append(dict(case=2, step="switch altitudes", up=up, down=down))


def case3(folder, rows):
    call("load_save", folder=folder, save="approach-kerbin")
    call("floatingorigin_clear")
    call("floatingorigin_show_window", visible=False)
    call("wait", seconds=3)
    record(3, "start", rows)
    capsule = other_craft()
    call("drive", heading=0, speed=15, distance=max(0.0, capsule["distance"] - 100.0))
    record(3, "100 m from the capsule", rows)
    capsule = other_craft()
    call("drive", heading=180, speed=15, distance=max(0.0, 2700.0 - capsule["distance"]))
    if any(v["loaded"] for v in call("list_vessels") if not v["active"] and v["situation"] == "LANDED"):
        raise RuntimeError("the capsule is still loaded")
    record(3, "capsule unloaded", rows)
    moved = call("drive", heading=180, speed=2, distance=600, until_shift=True)
    if moved.get("stoppedBecause") != "shift":
        raise RuntimeError("the floating origin did not move")
    record(3, "after the shift", rows)


def case4(folder, rows):
    start = launch_rover(folder)
    call("floatingorigin_clear")
    call("floatingorigin_show_window", visible=False)
    record(4, "start", rows)
    call("drive", heading=90, speed=20, distance=2250)
    record(4, "far end of the runway", rows)
    # Back by a U-turn and the same heading the other way, then the last metres to the spot: drive_to alone
    # would back up the whole way.
    call("drive", heading=270, speed=20, distance=2200)
    call("drive_to", latitude=start["latitude"], longitude=start["longitude"], speed=3, tolerance=1)
    record(4, "back at the start", rows)


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/")
    parser.add_argument("--cases", nargs="*", type=int, default=[1, 2, 4, 3],
                        help="which cases, 1 to 4, in that order (case 3 last: its parked craft stays in the game)")
    parser.add_argument("--out", default="out", help="where lines.json and the screenshots go")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    out = os.path.abspath(options.out)
    os.makedirs(out, exist_ok=True)

    rows = []
    for case in options.cases:
        log("case %d" % case)
        {1: case1, 2: case2, 3: case3, 4: case4}[case](options.folder, rows)
        # The window stays hidden but for its screenshot.
        call("floatingorigin_show_window", visible=True)
        call("floatingorigin_move_window", x=0, y=60)
        call("wait", seconds=1)
        call("screenshot", path=os.path.join(out, "case%d.png" % case), return_image=False)
        call("floatingorigin_show_window", visible=False)
    with open(os.path.join(out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
