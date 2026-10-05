# What the measurements show: leaving the rotating frame and coming back, in one flight

Part of [KSP Diag - Floating Origin](../README.md): what [the measurements of leaving the rotating frame and coming back, in one flight](the-measurements-rotating-frame.md)
say about the frame the ground is built in.

This page says when the frame changes, and by how much. What a change of frame does to the ground is
on [the page of the
fix](https://github.com/lhervier/KSP-TerrainPrecisionFix/blob/main/docs/the-culprit-ground.md#why-it-is-different-at-every-load).

## The frame changes during a flight, with nothing loaded

`directRotAngle` stays put
while the rocket is below 100 km and follows the clock above it: on the way back down, it was
4.900808° further than on the pad, Kerbin's rotation over the 293.4 s spent above. The craft that lands
there finds a frame that depends on its trajectory. Its position moved all along the way too: at that
speed, the world origin follows the rocket at almost every frame, some 19 m at a time.
Coming down from orbit is ordinary play, and the ground built on the way is built in that frame.
