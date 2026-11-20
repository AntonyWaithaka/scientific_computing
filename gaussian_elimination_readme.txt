New assumptions
A fourth measurement vector [20, 18, 15] has been added.

A is fixed and well-conditioned; the same LU factorisation can be reused.

Input data
A as above; four b vectors as shown.

Output
text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.6 6.4 5.8]
Residual norm: 1.1102230246251565e-15

Measurement set 3
Solution: [4.8 4.2 5.06666667]
Residual norm: 4.440892098500626e-16

Measurement set 4
Solution: [7. 8. 7.66666667]
Residual norm: 4.440892098500626e-16
Interpretation
Adding the fourth measurement set costs almost no extra computation because A was already factored. Each new solution has residual norm ≈ 1e-15, i.e. exact up to floating-point round-off. This is the key benefit of LU decomposition: repeat solves with the same A become ~O(n²) instead of O(n³).
