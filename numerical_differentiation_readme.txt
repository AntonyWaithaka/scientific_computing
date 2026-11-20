New assumptions
Sampling interval halved from 0.5 s to 0.25 s.

Positions are exact (no noise) so we can isolate the effect of step size.

Input data
13 samples, t ∈ [0, 3] with dt = 0.25.

Output
text
Time   Position   Velocity   Acceleration
0.00     0.000     0.000      16.400
0.25     0.513     4.100      16.400
0.50     2.050     8.200      16.400
...
3.00    73.800    49.200      16.400

Expected v = 16.4 t, a = 16.4
Mean acceleration: 16.4000
Interpretation
Halving dt doubles the sample count but the recovered acceleration is still exactly 16.4 — the central-difference scheme is exact for quadratics. Velocity at t=1.5 is now 24.6 m/s (was 24.6 with fewer points but more noise-prone). Finer sampling is more robust to noise in real data.
