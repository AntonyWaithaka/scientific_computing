import numpy as np

# Halved time step: dt=0.25 (was 0.5)
t = np.array([0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5,
              1.75, 2.0, 2.25, 2.5, 2.75, 3.0])
y = 8.2 * t**2       # exact positions

v = np.gradient(y, t)
a = np.gradient(v, t)

print("Time   Position   Velocity   Acceleration")
for i in range(len(t)):
    print(f"{t[i]:4.2f}  {y[i]:8.3f}  {v[i]:8.3f}  {a[i]:8.3f}")

print("\nExpected v = 16.4 t, a = 16.4")
print(f"Mean acceleration: {np.mean(a[1:-1]):.4f}")
