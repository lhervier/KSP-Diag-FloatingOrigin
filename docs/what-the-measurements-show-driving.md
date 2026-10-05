# What the measurements show: a rover driven 2 km and back

Part of [KSP Diag - Floating Origin](../README.md): what [the measurements of a rover driven 2 km and back](the-measurements-driving.md)
say about the frame the ground is built in.

This page says when the frame changes, and by how much. What a change of frame does to the ground is
on [the page of the
fix](https://github.com/lhervier/KSP-TerrainPrecisionFix/blob/main/docs/the-culprit-ground.md#why-it-is-different-at-every-load).

## The frame changes during a drive, with nothing loaded

The angle never moves, but **Sphere
origin** does: back at the very spot it started from, the rover finds the terrain sphere 6.6 m from
where it was, after four shifts each way, because the world origin follows the craft in jumps, and where the last jump happened
depends on the way it drove (see [the floating origin](what-it-measures.md)).
Driving to a base is ordinary play, and the ground built on the way, or when a parked craft comes
within range, is built in that frame.
