import numpy as np

# Break-even with raised selling price: 45 per unit (was 40)
def f(x):
    return 45 * x - (2000 + 15 * x + 0.05 * x**2)

def bisection(f, a, b, tol=1e-8, max_iter=200):
    if f(a) * f(b) > 0:
        raise ValueError("f(a), f(b) must straddle zero")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(b - a) / 2 < tol or f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def fixed_point(g, x0, tol=1e-8, max_iter=500):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x_new

root_bis = bisection(f, 0, 300)

# Rearranged fixed-point: x = (2000 + 0.05x^2)/30
g = lambda x: (2000 + 0.05 * x**2) / 30
root_fp = fixed_point(g, 100)

print(f"Break-even units (bisection): {root_bis:.4f}")
print(f"Break-even units (fixed-point): {root_fp:.4f}")
print(f"f(root) bisection: {f(root_bis):.3e}")
print(f"f(root) fixed-point: {f(root_fp):.3e}")
