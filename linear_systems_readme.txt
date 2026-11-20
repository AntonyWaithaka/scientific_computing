New assumptions
Same two server types but with new observed totals: 24 CPU and 80 GB memory.

Coefficients (per-server consumption) remain unchanged.

Input data
A = [[4, 2], [8, 12]], b = [24, 80].

Output
text
Type A servers: 4
Type B servers: 4
Verification A @ solution: [24. 80.]
Residual: [0. 0.]
Residual norm: 0.0
Interpretation
With higher observed totals (24 CPU / 80 GB instead of 20 / 72), the solution changes from 2 Type A + 6 Type B to 4 Type A + 4 Type B. The residual norm is 0, confirming the solution reproduces the totals exactly. This shows how a small change in observed resource usage dramatically changes the inferred server mix.
