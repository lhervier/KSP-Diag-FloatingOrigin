# The protocol: a rover driven 2 km and back

Part of [KSP Diag - Floating Origin](../README.md): a rover driven 2 km and back, step by step. The columns it
fills are in [What it measures](what-it-measures.md#the-window).

The frame has two inputs, the orientation and the position of the terrain sphere. This case moves
the position of the terrain sphere, with no save loaded. In play: driving to a base, or coming within
range of it.

It uses one craft, in [`craft/`](../craft/): copy [`Diag3-Rover.craft`](../craft/Diag3-Rover.craft)
into the `Ships/SPH` folder of a sandbox game.

## The steps

Make sure no other craft is landed anywhere around the Space Center: one parked within 2.5 km of the
rover would keep the world origin from moving at all, as [a rover near a parked craft](the-measurements-parked-craft.md) shows. Put `Diag3-Rover` on the runway, put its brakes on straight away — it comes out of the hangar with
them off — and press **Record**. Drive to the far end of the runway, stop and
press **Record**, then drive back to where you started, stop and press **Record** again.

**→ Measured in [The measurements: a rover driven 2 km and back](the-measurements-driving.md)**

## Played by a script

[`diag/automation/run-cases.py`](../diag/automation/run-cases.py) plays this case step for step, and
takes a screenshot of the table. It drives KSP through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), a mod that answers requests sent to it over
HTTP, from the computer KSP runs on only; and it needs nothing but Python 3 — no AI, no package to
install. Anyone can read it top to bottom: each case is a short function.

1. Install KSP-MCPServer next to this mod. Copy the craft into a sandbox game, as said
   above, with no other craft landed around the Space Center; start KSP and wait for the main menu.
2. Run `python run-cases.py --folder <your sandbox game> --cases 4 --out screenshots`.

It writes every line to `lines.json` next to the screenshots, and quits KSP at the end — give
it `--keep-running` to leave KSP open. Save `KSP.log` before starting KSP again: KSP writes it anew
at every start.
