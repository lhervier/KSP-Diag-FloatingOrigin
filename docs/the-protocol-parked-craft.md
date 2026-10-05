# The protocol: a rover near a parked craft, then on its own

Part of [KSP Diag - Floating Origin](../README.md): a rover near a parked craft, then on its own, step by step. The columns it
fills are in [What it measures](what-it-measures.md#the-window).

The frame has two inputs, the orientation and the position of the terrain sphere. This case moves
the position of the terrain sphere, with no save loaded. In play: driving to a base, and away from it.

It needs a craft parked 2 km away, so it comes with a save,
[`approach-kerbin.sfs`](../diag/approach-kerbin.sfs): copy it into the folder of a sandbox game, and
load it from that game.

## The steps

Load `approach-kerbin`. You drive `Diag3-Rover`, facing south; a capsule is landed about 2 km north
of it, on the same north–south line. Watch the line in progress all along: **Origin distance** and
**Shifts**.

- Press **Record**.
- Drive north to about 100 m from the capsule, stop and press **Record**.
- Turn round and drive south until the capsule is more than 2.6 km away, so that it is unloaded. Stop
  and press **Record**.
- Keep driving south in a straight line. When **Shifts** goes up, stop and press **Record**.
  *Spoiler, so that you do not have to creep forward a metre at a time: it happens when **Origin
  distance** reaches about 500 m.*

Compare **Origin distance** on the line taken near the capsule, and **Shifts** and **Last shift** on
the two lines after it.

**→ Measured in [The measurements: a rover near a parked craft, then on its own](the-measurements-parked-craft.md)**

## Played by a script

[`diag/automation/run-cases.py`](../diag/automation/run-cases.py) plays this case step for step, and
takes a screenshot of the table. It drives KSP through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), a mod that answers requests sent to it over
HTTP, from the computer KSP runs on only; and it needs nothing but Python 3 — no AI, no package to
install. Anyone can read it top to bottom: each case is a short function.

1. Install KSP-MCPServer next to this mod. Copy [the save](../diag/approach-kerbin.sfs) into a sandbox
   game, as said above; start KSP and wait for the main menu.
2. Run `python run-cases.py --folder <your sandbox game> --cases 3 --out screenshots`.

The script drives north until the capsule is 100 m away — at once, if the save opens closer than that —
then south until the capsule is unloaded, then on, slowly, until the origin moves. Played with other
cases in one session, this one goes last: the capsule of its save stays in the game, and a rover
launched after it would find a craft parked within range, the origin held still.
It writes every line to `lines.json` next to the screenshots, and quits KSP at the end — give
it `--keep-running` to leave KSP open. Save `KSP.log` before starting KSP again: KSP writes it anew
at every start.
