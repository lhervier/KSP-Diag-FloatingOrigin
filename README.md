# KSP Diag - Floating Origin

**⚠️ Work in progress.** This is an active investigation, not a finished mod. The code and this page can still change, and several questions are still open.

A measuring instrument for KSP 1.12. It shows, on your own install, the world frame the terrain of a
body is built in: how the body is turned in Unity's world axes, and where it sits in them. It records
that frame whenever you ask, so that you can compare it from one loading to the next, and from one
moment of a flight to another.

**It explains, it does not compare.** The other diagnostic mods of this family are read twice — once
on a stock install, once with a fix installed — and the difference between the two readings is the
whole point of running them. This one is read once. The five values it shows are the game's own
description of its world: a fix to the terrain does not have to touch them, and the one this family
proposes writes none of them. Reading the same figures with a fix installed is the expected outcome
here, not a sign that the fix does nothing. Every figure on this page is stock KSP, and what they show
is how the game places the ground it builds.

**How this was made.** Written with Claude, Anthropic's AI assistant, and reviewed line by line by a
human — me. I am saying so up front, because contributions made with an AI deserve a closer look than
others, and because some people would rather stop reading here. That look is easy to give here: this
mod changes nothing in the game and reads five values the game already holds, the source is a few
hundred lines, and the protocol runs on a stock install with no dependency of any kind.

## What it measures

Unity places every object with `float` coordinates, precise near the origin of its world and only to a
few centimetres 600 km away. So KSP keeps that origin on your craft, and shifts it back onto the craft
once it has drifted far enough — except while another landed craft is loaded, when it waits until that
craft is unloaded. Close to a planet, it stands still in Unity's axes and the sky turns around it; further
out, the planet turns. The ground is placed relative to the planet's terrain sphere: where that sphere sits
and how it is turned are the frame the ground is built in.

The window records, one line at a time: the game clock, whether the planet or the sky is turning, the
two angles the game splits the planet's rotation between, and the world position of the terrain
sphere; and, for the world origin itself, how far your craft is from it, how many times it has been
shifted since the previous line, and how far the last shift moved it. `Alt+F6` hides the window, and shows it again.

**→ Full chapter: [What it measures](docs/what-it-measures.md)**

## The situations

Each situation below comes with its protocol, its measurements and what they show. Each one moves one
input of the frame, its orientation or its position, in a situation every player meets, and only
loading the same save loads a save between two records. The craft and the save they use come with this
mod. Every series was played on stock KSP 1.12.5 with KSP Community Fixes, by a script through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer).

## Loading the same save three times

A rover on the runway, quicksaved, then quickloaded three times, about ten seconds apart, with a record
after each. A different angle at every quickload, −140.168417°, −140.404636°, −140.640856°, and a
terrain sphere moved by 2.5 km each time: loading a save does not give back the frame it was saved in.

**→ [The protocol](docs/the-protocol-loading.md) · [The measurements](docs/the-measurements-loading.md) · [What they show](docs/what-the-measurements-show-loading.md)**

## Leaving the rotating frame and coming back, in one flight

A sounding rocket, recorded on the pad, once out of the rotating frame, and once back in it on the way
down. The frame switches at 100 km, and the angle is 4.900808° further on the way down than on the pad:
the frame changes during a flight, with nothing loaded.

**→ [The protocol](docs/the-protocol-rotating-frame.md) · [The measurements](docs/the-measurements-rotating-frame.md) · [What they show](docs/what-the-measurements-show-rotating-frame.md)**

## A rover near a parked craft, then on its own

A rover driven to a parked capsule, then away until the capsule is unloaded, then on to the next shift
of the world origin. No shift while the capsule is in range; one shift of 2,474.108 m the moment it was
unloaded; then, on its own, one shift of 500.001 m.

**→ [The protocol](docs/the-protocol-parked-craft.md) · [The measurements](docs/the-measurements-parked-craft.md) · [What they show](docs/what-the-measurements-show-parked-craft.md)**

## A rover driven 2 km and back

A rover driven to the far end of the runway and back to where it started. Back at the very spot it
started from, the terrain sphere is 6.6 m from where it was: the frame changes during a drive too, with
nothing loaded.

**→ [The protocol](docs/the-protocol-driving.md) · [The measurements](docs/the-measurements-driving.md) · [What they show](docs/what-the-measurements-show-driving.md)**

## Get it

Either way you end up with the same `GameData/KSPDiagFloatingOrigin/` folder.

**Download it** — from the assets of the
[latest release](https://github.com/lhervier/KSP-Diag-FloatingOrigin/releases/latest).

**Or compile it** — clone this repository, set `KSPDIR` to your KSP install folder and run
`build.bat`. It needs the .NET SDK and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer) installed in that KSP, takes a few seconds,
reads the KSP assemblies straight from your install, and puts the DLL in
`GameData/KSPDiagFloatingOrigin/` inside the repository. It does not install anything.
KSP-MCPServer is only needed to compile: it provides the attribute that marks what this mod offers to
it, and this mod runs the same without it. Worth doing if you would rather not run a binary you have no source for while
reporting a measurement.

## Install

Drop `GameData/KSPDiagFloatingOrigin` into the `GameData` of KSP, so that you end up with
`GameData/KSPDiagFloatingOrigin/KSPDiagFloatingOrigin.dll`. It runs on a stock install:
no Harmony, no ModuleManager, no dependency of any kind.

It reads the world and writes nothing at all: the table lives in memory and is gone when you close the
game. Your saves are never touched. Removing the folder removes the mod.

## License

MIT
