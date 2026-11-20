New assumptions
The approximation of √2 uses 1.4142 instead of 1.414 (more digits).

Same tiny-x stability test cases as before.

Input data
calculated = 0.1 + 0.2, expected = 0.3

approx_value = 1.4142, true_value = np.sqrt(2)

x values: 1e-4, 1e-8, 1e-12

Output
text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00001356
Relative error: 0.000959%
x=1e-04: direct=0.499962512649, stable=0.499962512649
x=1e-08: direct=0.499999996961, stable=0.499999996961
x=1e-12: direct=0.499977300987, stable=0.499999999996
Interpretation
Changing the approximation to 1.4142 reduced absolute error from ~2.1e-4 to ~1.36e-5 (15× smaller). The exact comparison still fails for 0.1+0.2 because of binary representation — np.isclose correctly reports True. At x = 1e-12, the direct formula loses precision (returns 0.4999… with visible error) while the stable formula 
stays close to 0.5 — this demonstrates catastrophic cancellation.
