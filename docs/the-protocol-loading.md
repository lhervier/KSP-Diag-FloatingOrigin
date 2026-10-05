# The protocol: loading the same save three times

Part of [KSP Diag - Floating Origin](../README.md): loading the same save three times, step by step. The columns it
fills are in [What it measures](what-it-measures.md#the-window).

The frame has two inputs, the orientation and the position of the terrain sphere. This case moves
the orientation of the terrain sphere, with a save loaded between two records: the only case a change
made at loading can reach. In play: loading a game.

It uses one craft, in [`craft/`](../craft/): copy [`Diag3-Rover.craft`](../craft/Diag3-Rover.craft)
into the `Ships/SPH` folder of a sandbox game.

## The steps

Put `Diag3-Rover` on the runway, and put its brakes on straight away: it comes out of the hangar with
them off. Quicksave (F5). Then, three times: wait about ten seconds, quickload (hold F9) and press
**Record**. Compare the three lines.

**→ Measured in [The measurements: loading the same save three times](the-measurements-loading.md)**

## Played by a script

[`diag/automation/run-cases.py`](../diag/automation/run-cases.py) plays this case step for step, and
takes a screenshot of the table. It drives KSP through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), a mod that answers requests sent to it over
HTTP, from the computer KSP runs on only; and it needs nothing but Python 3 — no AI, no package to
install. Anyone can read it top to bottom: each case is a short function.

1. Install KSP-MCPServer next to this mod. Copy the craft into a sandbox game, as said
   above, with no other craft landed around the Space Center; start KSP and wait for the main menu.
2. Run `python run-cases.py --folder <your sandbox game> --cases 1 --out screenshots`.

It writes every line to `lines.json` next to the screenshots, and quits KSP at the end — give
it `--keep-running` to leave KSP open. Save `KSP.log` before starting KSP again: KSP writes it anew
at every start.
