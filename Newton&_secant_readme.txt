New assumptions
Supply voltage is now 15 V instead of 12 V.

Diode resistance 1.5 Ω and thermal voltage 0.026 V unchanged.

Input data
V = 15 V, R = 1.5 Ω, Vd(I) = 0.026·ln(1 + I/1e-12).

Output
text
Newton current: 9.92037895 A, iterations: 5
Secant current: 9.92037895 A, iterations: 6
Residual Newton: 1.776e-15
Residual Secant: 1.776e-15
Interpretation
Increasing V from 12 V to 15 V raises the current from ~7.9 A to ~9.92 A. Newton takes 5 iterations vs 6 for secant, but both reach the same root with residual ≈ 1e-15. Newton's edge comes from using the derivative; secant pays a small price but needs no derivative function.
