New assumptions
Operating pressure raised to 300 atm (was 200).

Kp = 1.6e-5 unchanged; reaction still N2 + 3H2 ⇌ 2NH3.

Input data
P = 300 atm, Kp = 1.6e-5, initial feeds 1 mol N2 / 3 mol H2.

Output
text
Equilibrium conversion x = 0.292055
NH3 produced = 0.584110 mol
Residual: 4.319e-17
Polynomial roots: [1. 2. 3.]
Interpretation
Raising pressure from 200 to 300 atm increases conversion x from ~0.24 to ~0.29, consistent with Le Chatelier's principle (fewer gas moles on product side). The polynomial check confirms np.roots recovers exact integer roots 1, 2, 3.
