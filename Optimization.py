import numpy as np
from scipy.optimize import minimize

# Load constraint raised 1000 -> 1500 tasks
def cost(v):
    x, y, z = v
    return 2 * x + 3 * y + 1.5 * z

def load(v):
    return sum(v) - 1500

bounds = [(0, 900), (0, 800), (0, 600)]
constraints = [{"type": "ineq", "fun": load}]

res = minimize(cost, [400, 400, 700], method="SLSQP",
               bounds=bounds, constraints=constraints)

print("Optimal workers:", np.round(res.x, 2))
print("Minimum cost:", round(res.fun, 2))
print("Load check:", round(sum(res.x), 2))
print("Converged:", res.success)
