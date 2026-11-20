import numpy as np

# Changed b from [20, 72] to [24, 80] to test a different scenario
# Type A: 4 CPU, 8 GB    Type B: 2 CPU, 12 GB
A = np.array([
    [4.0,  2.0],
    [8.0, 12.0]
])
b = np.array([24.0, 80.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
