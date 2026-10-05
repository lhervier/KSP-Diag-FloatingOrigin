# The saves

Part of [KSP Diag - Floating Origin](../README.md): the saves its protocol uses, and the ones the
loading protocol of the other instruments of the family uses on Real Solar System.

- [`approach-kerbin.sfs`](approach-kerbin.sfs) — the save [the protocol of a rover near a parked craft](../docs/the-protocol-parked-craft.md)
  uses: a capsule landed on the flat grass west of the KSC, and a rover 26 m from it.

Copy a save into the folder of a sandbox game and load it from that game.

## The script

[`automation/run-cases.py`](automation/run-cases.py) plays the four protocols through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), with Python 3 alone; how to run it is at the
top of the file, and in the *Played by a script* chapter of each protocol, such as
[the loading one](../docs/the-protocol-loading.md#played-by-a-script).

## The runs

KSP 1.12.5 with both expansions, Harmony, ModuleManager, KSP Community Fixes 1.41.1, this mod and
KSP-MCPServer, the cases played by `run-cases.py`. Read in the measurements of each protocol, such as
[loading the same save](../docs/the-measurements-loading.md).

- [`runs/cases-stock.log`](runs/cases-stock.log) — the `KSP.log` of the session of loading the same
  save, leaving the rotating frame, and a rover near a parked craft;
  what the script printed in [`runs/cases-stock-script.txt`](runs/cases-stock-script.txt), and every
  line it recorded in [`runs/cases-stock-lines.json`](runs/cases-stock-lines.json). The session ends
  with a rover driven 2 km and back, played after the parked craft, its capsule still within range: not
  used.
- [`runs/case4-stock.log`](runs/case4-stock.log) — the session of a rover driven 2 km and back, played alone; what the script
  printed in [`runs/case4-stock-script.txt`](runs/case4-stock-script.txt), and every line it recorded
  in [`runs/case4-stock-lines.json`](runs/case4-stock-lines.json).

## On Real Solar System

The saves of the loading protocol of
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight)
on [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0, kept here too so
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
