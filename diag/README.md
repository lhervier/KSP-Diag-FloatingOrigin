# The saves

Part of [KSP Diag - Floating Origin](../README.md): the saves its protocol uses, and the ones the
other instruments of the family use on Real Solar System.

- [`approach-kerbin.sfs`](approach-kerbin.sfs) — the save [case 3 of the protocol](../docs/the-protocol.md#case-3-a-rover-near-a-parked-craft-then-on-its-own)
  uses: a capsule landed on the flat grass west of the KSC, and a rover 26 m from it.

Copy a save into the folder of a sandbox game and load it from that game.

## The script

[`automation/run-cases.py`](automation/run-cases.py) plays the four cases of the protocol through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), with Python 3 alone; how to run it is at the
top of the file, and in [Played by a script](../docs/the-protocol.md#played-by-a-script).

## The runs

KSP 1.12.5 with both expansions, Harmony, ModuleManager, KSP Community Fixes 1.41.1, this mod and
KSP-MCPServer, the cases played by `run-cases.py`. Read in [The measurements](../docs/the-measurements.md).

- [`runs/cases-stock.log`](runs/cases-stock.log) — the `KSP.log` of the session of cases 1, 2 and 3;
  what the script printed in [`runs/cases-stock-script.txt`](runs/cases-stock-script.txt), and every
  line it recorded in [`runs/cases-stock-lines.json`](runs/cases-stock-lines.json). The session ends
  with a case 4 played after case 3, the capsule of case 3 still within range: not used.
- [`runs/case4-stock.log`](runs/case4-stock.log) — the session of case 4, played alone; what the script
  printed in [`runs/case4-stock-script.txt`](runs/case4-stock-script.txt), and every line it recorded
  in [`runs/case4-stock-lines.json`](runs/case4-stock-lines.json).

## On Real Solar System

The saves [KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) are loaded
from on [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0, kept here too so
that this instrument can be run on them. They need Real Solar System and what it requires (Kopernicus,
Modular Flight Integrator, KSPTextureLoader, the RSS textures), on an install of their own: they only
load there.

- [`reload-moon-rss.sfs`](reload-moon-rss.sfs) — a capsule on an empty FL-T100, landed on flat ground
  on the Moon.
- [`reload-moon-rss-resave.sfs`](reload-moon-rss-resave.sfs) — the same craft, saved again at a later
  load.
- [`reload-earth-rss-resave.sfs`](reload-earth-rss-resave.sfs) — the same kind of craft, on the grass
  about 1.4 km west of the KSC on Earth.
- [`reload-earth-rss-landed.sfs`](reload-earth-rss-landed.sfs) — the save above, with one line changed
  in the file: the situation of the craft, from `PRELAUNCH` to `LANDED`.
