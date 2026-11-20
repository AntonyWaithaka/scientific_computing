New assumptions
Total load raised from 1000 to 1500 tasks.

Worker bounds scaled up to allow more of each type.

Input data
Cost = 2x + 3y + 1.5z, constraint x+y+z ≥ 1500.

Output
text
Optimal workers: [   0.  600.  900.]
Minimum cost: 3150.0
Load check: 1500.0
Converged: True
Interpretation
The cheapest solution uses only worker types C and B (which have the best cost per task) and avoids A, hitting the upper bound on B. The solver found a tight constraint (load = 1500 exactly) because extra workers only add cost. This demonstrates how bounds and constraints shape the optimum.
