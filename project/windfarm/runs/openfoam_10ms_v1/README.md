# Wind farm: 10 m/s OpenFOAM URANS

23 annular Gaussian actuator rotors on an 8 m uniform terrain grid.
Actual recorded samples span 2–300 physical seconds. The source solver
completed at 300 s with all final checkpoint fields and passed numerical
stability, continuity and force-conservation checks.

This is a scenario adaptation of the rotor-force model, not a validated
reproduction of paper experiments. Ct=0.75, SST turbulence and the selected
inlet turbulence parameters are scenario assumptions. Rotor motion is
visual only (assumed tip-speed ratio), not a mechanical/controller solution.
Missing terrain coverage and missing sample points remain masked.

Source run: 20260929T075513Z_ebd84574. The original 299.968254 s ending was
archived and the final segment recomputed from 286 s to obtain a true 300 s
checkpoint. Metadata contains real timestamps; no frames were invented.
The preceding published_movie_v1 resources remain unchanged.
