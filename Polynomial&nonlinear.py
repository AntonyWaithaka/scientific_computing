import numpy as np
from scipy.optimize import root

# Pressure raised 200 -> 300 atm (Le Chatelier)
def equilibrium(vars):
    x = vars[0]
    if not (0 < x < 1):
        return [1e6]
    Kp, P = 1.6e-5, 300.0          # P changed
    return [((2*x)**2) / ((1 - x)*(3 - 3*x)**3) * P**-2 - Kp]

res = root(equilibrium, [0.5])
x_eq = res.x[0]
print(f"Equilibrium conversion x = {x_eq:.6f}")
print(f"NH3 produced = {2*x_eq:.6f} mol")
print(f"Residual: {res.fun[0]:.3e}")

# Polynomial root check
coeffs = [1, -6, 11, -6]
print("Polynomial roots:", np.sort(np.roots(coeffs)))
