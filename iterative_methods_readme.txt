New assumptions
Hot boundary = 80 °C (was 100), cool boundary = 40 °C (was 20).

Same 5×5 tridiagonal Laplacian matrix; interior starts at 0 °C.

Input data
A tridiagonal with diagonal 2, off-diagonal −1; b = [80, 0, 0, 0, 40].

Output
text
Jacobi temperatures: [60. 50. 45. 42.5 41.25]
Gauss-Seidel temperatures: [60. 50. 45. 42.5 41.25]
Direct solution: [60. 50. 45. 42.5 41.25]
Iterations Jacobi: 87, Gauss-Seidel: 46
Interpretation
Both iterative methods converge to the same solution as direct solve, but Gauss-Seidel halves the iteration count. Temperatures now range linearly between the 40 °C and 80 °C boundaries instead of 20/100. The convergence plot shows Gauss-Seidel's error curve dropping more steeply because it uses updated values immediately.
