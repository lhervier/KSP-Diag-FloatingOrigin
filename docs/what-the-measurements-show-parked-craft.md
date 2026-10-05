# What the measurements show: a rover near a parked craft, then on its own

Part of [KSP Diag - Floating Origin](../README.md): what [the measurements of a rover near a parked craft, then on its own](the-measurements-parked-craft.md)
say about the frame the ground is built in.

This page says when the frame changes, and by how much. What a change of frame does to the ground is
on [the page of the
fix](https://github.com/lhervier/KSP-TerrainPrecisionFix/blob/main/docs/the-culprit-ground.md#why-it-is-different-at-every-load).

## The world origin moves by 500 m at a time, and not at all near a parked craft

On its own, the
rover dragged the origin 500.001 m away before it jumped: the next shift moved the terrain
sphere by exactly that much. Near the capsule, there was no shift at all: the rover drove away from it,
out of its range, before the origin moved, in a single shift of 2,474.108 m the moment the capsule was
unloaded: the distance the rover then stood from it, which it had been waiting for. So a frame is kept still for as long as a craft
is parked within 2.5 km of the one you fly, and leaving that craft behind is what moves it — all at
once, by however far the trip has taken you.
