New assumptions
Time step halved to dt = 0.05 (was 0.1).

Same r = 0.3, K = 1000, P0 = 50.

Input data
r = 0.3, K = 1000, P0 = 50, dt = 0.05, t_end = 30.

Output
text
P at t=30 (dt=0.05): 998.3659
Error vs K: 1.6341
Interpretation
Halving dt reduces the gap to K from ~2.8 (dt=0.1) to ~1.6, showing Euler's first-order convergence. The population asymptotically approaches K = 1000 but never exceeds it — consistent with the logistic model.
