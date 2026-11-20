import numpy as np
import matplotlib.pyplot as plt

# Halved time step: dt = 0.05 (was 0.1)
r, K, P0, dt, t_end = 0.3, 1000.0, 50.0, 0.05, 30.0

def f(P, t):
    return r * P * (1 - P / K)

def euler(f, y0, t0, t_end, dt):
    ts, ys = [t0], [y0]
    t, y = t0, y0
    while t < t_end:
        y = y + dt * f(y, t)
        t += dt
        ts.append(t); ys.append(y)
    return np.array(ts), np.array(ys)

t_e, P_e = euler(f, P0, 0.0, t_end, dt)
print(f"P at t=30 (dt={dt}): {P_e[-1]:.4f}")
print(f"Error vs K: {K - P_e[-1]:.4f}")

plt.plot(t_e, P_e)
plt.axhline(K, linestyle='--', color='k', label='K')
plt.xlabel("Time"); plt.ylabel("Population")
plt.title(f"Logistic growth - Euler dt={dt}")
plt.legend(); plt.grid(True)
plt.savefig("plots/euler_task17.png", dpi=120)
plt.show()
