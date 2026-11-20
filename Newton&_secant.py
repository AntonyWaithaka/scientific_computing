import numpy as np

# Supply voltage raised 12 -> 15 V (Instruction C)
def f(I):
    return 15 - 1.5 * I - 0.026 * np.log(1 + I / 1e-12)

def df(I):
    return -1.5 - 0.026 / (1 + I / 1e-12) * (1 / 1e-12)

def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for k in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iter

def secant(f, x0, x1, tol=1e-10, max_iter=100):
    for k in range(max_iter):
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) < tol:
            return x2, k + 1
        x0, x1 = x1, x2
    return x2, max_iter

r_n, it_n = newton(f, df, 5.0)
r_s, it_s = secant(f, 4.0, 6.0)

print(f"Newton current: {r_n:.8f} A, iterations: {it_n}")
print(f"Secant current: {r_s:.8f} A, iterations: {it_s}")
print(f"Residual Newton: {f(r_n):.3e}")
print(f"Residual Secant: {f(r_s):.3e}")
