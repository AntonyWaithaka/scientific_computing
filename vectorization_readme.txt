New assumptions
Latency values now range 10–500 ms (was 5–250 ms).

All 1,000,000 values must still be converted to seconds and squared.

Loop and vectorised versions must produce identical results.

Input data
1,000,000 uniform random values in [10, 500] ms.

Output
text
First five squared latency values: [0.0612  0.0184  0.1893  0.0072  0.1465]
Loop time: 0.3187 s
Vectorized time: 0.0026 s
Approximate speed-up: 122.6x
Interpretation
Changing the latency range did not change the speed-up because vectorised NumPy cost is dominated by array size, not value magnitude. The vectorised version ran ~120× faster than the Python loop for one million elements, 
proving that vectorisation matters most on large datasets.
