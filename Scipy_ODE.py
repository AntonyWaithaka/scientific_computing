import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Lower transmission: beta = 0.2 (was 0.4)
N, beta, gamma = 10000, 0.2, 0.15
S0, I0, R0 = N - 10, 10, 0

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

sol = solve_ivp(sir, [0, 100], [S0, I0, R0],
                t_eval=np.linspace(0, 100, 500))

print(f"Peak infected: {np.max(sol.y[1]):.0f}")
print(f"Peak time:     {sol.t[np.argmax(sol.y[1])]:.1f} days")
print(f"Final recovered: {sol.y[2][-1]:.0f}")
print(f"Final susceptible: {sol.y[0][-1]:.0f}")

plt.plot(sol.t, sol.y[0], label="Susceptible")
plt.plot(sol.t, sol.y[1], label="Infected")
plt.plot(sol.t, sol.y[2], label="Recovered")
plt.xlabel("Days"); plt.ylabel("People")
plt.title(f"SIR beta={beta} gamma={gamma}")
plt.legend(); plt.grid(True)
plt.savefig("plots/sir_task18.png", dpi=120)
plt.show()
