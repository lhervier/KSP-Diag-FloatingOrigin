# The measurements

Part of [KSP Diag - Floating Origin](../README.md): the four cases of [the protocol](the-protocol.md),
played on stock. What they show is in [What the measurements show](what-the-measurements-show.md).

The four cases were played on KSP 1.12.5 with both expansions, [KSP Community
Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes) and the two mods it needs, Harmony and
ModuleManager, this mod and [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the
protocol, and nothing else in `GameData`. They were played by
[the script of the protocol](the-protocol.md#played-by-a-script), `run-cases.py`: cases 1 to 3 in one
session, case 4 alone in another. The game's interface is in French. The bottom line of each table is
the reading in progress, not a record.

## Case 1: loading the same save three times

`Diag3-Rover` on the runway, quicksaved right after rollout, then quickloaded three times, about ten
seconds apart, with one record after each quickload.

![Case 1: a quicksave loaded three times](../imgs/stock-case1-quickload.png)

| record | UT (s) | directRotAngle | Sphere origin (m) | Shifts | Last shift (m) |
|---|---|---|---|---|---|
| 1, after the first quickload | 5062.18 | -140.168417 | (492190.813, 508.996, -343266.281) | 1 | 93,716.864 |
| 2, after the second quickload | 5062.18 | -140.404636 | (490771.406, 508.996, -345292.563) | 1 | 131,725.900 |
| 3, after the third quickload | 5062.16 | -140.640856 | (489343.656, 508.996, -347312.969) | 1 | 131,725.899 |

Each quickload puts the clock back to the date of the quicksave: the UT of every line is that date,
plus the few seconds waited before the record. Each quickload shifted the world origin once.

**→ What it shows: [Loading a save does not give back the frame it was saved in](what-the-measurements-show.md#loading-a-save-does-not-give-back-the-frame-it-was-saved-in)**

## Case 2: leaving the rotating frame and coming back, in one flight

`Diag3-Rocket` from the launch pad, SAS on, straight up at full throttle: one record on the pad, one
once **Frame** read `Inertial`, one once it read `Rotating` again, on the way down.

![Case 2: the sounding rocket](../imgs/stock-case2-sounding-rocket.png)

| record | UT (s) | Frame | directRotAngle | InverseRotAngle | Shifts | Last shift (m) |
|---|---|---|---|---|---|---|
| 1, on the pad | 5062.48 | Rotating | -140.640856 | 315.213544 | 1 | 448.328 |
| 2, above the threshold | 5184.58 | Inertial | -140.639520 | 317.251983 | 5215 | 18.868 |
| 3, back below it | 5477.96 | Rotating | -135.740048 | 317.253654 | 14668 | 18.710 |

**Frame** changed at 100 km: the script, which reads it every fifth of a second, saw it switch at an
altitude of 100,093 m on the way up and 99,880 m on the way down. Between lines 1 and 3,
`directRotAngle` moved by 4.900808°: Kerbin's rotation over 293.4 s. In flight, the world origin was
shifted 19,883 times, by about 19 m each time.

**→ What it shows: [The frame also changes during a flight, with nothing loaded](what-the-measurements-show.md#the-frame-also-changes-during-a-flight-with-nothing-loaded)**

## Case 3: a rover near a parked craft, then on its own

`approach-kerbin`, one drive: one record at the start, one 100 m from the capsule, one once the capsule
was unloaded, one after the next shift.

![Case 3: the rover near a parked craft, then on its own](../imgs/stock-case3.png)

| record | UT (s) | Sphere origin (m) | Origin distance (m) | Shifts | Last shift (m) |
|---|---|---|---|---|---|
| 1, at the start | 2041.94 | (21257.676, 664.943, -599688.875) | 0.3 | 1 | 31,735,566.501 |
| 2, 100 m from the capsule | 2044.00 | (21257.676, 664.943, -599688.875) | 0.3 | 0 | -- |
| 3, capsule unloaded | 2197.46 | (21251.555, 3139.016, -599677.375) | 203.2 | 1 | 2,474.108 |
| 4, after the next shift | 2312.72 | (21260.332, 3638.887, -599670.063) | 1.8 | 1 | 500.001 |

The shift of line 1 is the one made by loading the save. The save opens with the rover 26 m from the
capsule, so line 2 was recorded where line 1 was, two seconds later. **Origin distance** is read once
the rover has stopped, a little after the shift of lines 3 and 4.

**→ What it shows: [The world origin moves by 500 m at a time, and not at all near a parked craft](what-the-measurements-show.md#the-world-origin-moves-by-500-m-at-a-time-and-not-at-all-near-a-parked-craft)**

## Case 4: a rover driven 2 km and back

`Diag3-Rover` on the runway: one record at the start, one at the far end of the runway, one back at
the start.

![Case 4: the rover, down the runway and back](../imgs/stock-case4-runway.png)

| record | directRotAngle | Sphere origin (m) | Origin distance (m) | Shifts | Last shift (m) |
|---|---|---|---|---|---|
| 1, at the start | -140.000535 | (493194.000, 508.996, -341822.250) | 0.6 | 1 | 1,394.781 |
| 2, at the far end | -140.000535 | (494330.844, 489.395, -340175.563) | 259.6 | 4 | 500.116 |
| 3, back at the start | -140.000535 | (493196.156, 503.046, -341820.219) | 6.5 | 4 | 500.002 |

The shift of line 1 is the one made by the rollout. Lines 1 and 3 are 6.6 m apart in **Sphere origin**.

**→ What it shows: [The frame also changes during a flight, with nothing loaded](what-the-measurements-show.md#the-frame-also-changes-during-a-flight-with-nothing-loaded)**

## The logs

In [`diag/runs`](../diag/README.md#the-runs):
[`cases-stock.log`](../diag/runs/cases-stock.log), the `KSP.log` of the session of cases 1 to 3, with
what the script printed in [`cases-stock-script.txt`](../diag/runs/cases-stock-script.txt) and every
line it recorded in [`cases-stock-lines.json`](../diag/runs/cases-stock-lines.json); and
[`case4-stock.log`](../diag/runs/case4-stock.log), the session of case 4, with
[`case4-stock-script.txt`](../diag/runs/case4-stock-script.txt) and
[`case4-stock-lines.json`](../diag/runs/case4-stock-lines.json). The first session also played a case 4
after case 3, its lines in the same files: the capsule of case 3 was still within range, the origin
never moved, and that case 4 is not used.
