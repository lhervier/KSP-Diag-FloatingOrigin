# What the measurements show: loading the same save three times

Part of [KSP Diag - Floating Origin](../README.md): what [the measurements of loading the same save three times](the-measurements-loading.md)
say about the frame the ground is built in.

This page says when the frame changes, and by how much. What a change of frame does to the ground is
on [the page of the
fix](https://github.com/lhervier/KSP-TerrainPrecisionFix/blob/main/docs/the-culprit-ground.md#why-it-is-different-at-every-load).

## Loading a save does not give back the frame it was saved in

The same quicksave, loaded three
times, gives three different angles. From one quickload to the next, `directRotAngle` moved back
by 0.236219° then 0.236220°: Kerbin's rotation over 14.14 s each time, the order of the time spent in
flight between two loadings. The frame a save comes back in depends on how long the game ran before it was loaded,
which the save knows nothing about. The terrain sphere moved by 2.5 km each time.
