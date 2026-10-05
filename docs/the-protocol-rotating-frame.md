# The protocol: leaving the rotating frame and coming back, in one flight

Part of [KSP Diag - Floating Origin](../README.md): leaving the rotating frame and coming back, in one flight, step by step. The columns it
fills are in [What it measures](what-it-measures.md#the-window).

The frame has two inputs, the orientation and the position of the terrain sphere. This case moves
the orientation of the terrain sphere, with no save loaded. In play: coming down from orbit to land
near a base.

It uses one craft, in [`craft/`](../craft/): copy [`Diag3-Rocket.craft`](../craft/Diag3-Rocket.craft)
into the `Ships/VAB` folder of a sandbox game.

## The steps

Put `Diag3-Rocket` on the launch pad. It is a sounding rocket that climbs high enough for the frame
of Kerbin to stop being `Rotating`. It has no decoupler: its crew does not survive the
landing.

Press **Record** on the pad. Turn SAS on, so that the rocket keeps pointing straight up, launch at
full throttle, and press **Record** once **Frame**
reads `Inertial`. Let it fall back, and press **Record** again once **Frame** reads `Rotating`, before
it hits the ground. Compare the lines: no save was loaded between them. All along the flight, keep an eye
on **Frame**: the moment it changes, on the way up and on the way down, note the altitude shown by the
game's altimeter.

**→ Measured in [The measurements: leaving the rotating frame and coming back, in one flight](the-measurements-rotating-frame.md)**

## Played by a script

[`diag/automation/run-cases.py`](../diag/automation/run-cases.py) plays this case step for step, and
takes a screenshot of the table. It drives KSP through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), a mod that answers requests sent to it over
HTTP, from the computer KSP runs on only; and it needs nothing but Python 3 — no AI, no package to
install. Anyone can read it top to bottom: each case is a short function.

1. Install KSP-MCPServer next to this mod. Copy the craft into a sandbox game, as said
   above, with no other craft landed around the Space Center; start KSP and wait for the main menu.
2. Run `python run-cases.py --folder <your sandbox game> --cases 2 --out screenshots`.

The script reads the frame every fifth of a second and writes down the altitude at which it switches.
It writes every line to `lines.json` next to the screenshots, and quits KSP at the end — give
it `--keep-running` to leave KSP open. Save `KSP.log` before starting KSP again: KSP writes it anew
at every start.
