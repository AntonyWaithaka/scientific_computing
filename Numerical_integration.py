import numpy as np
from scipy.integrate import simpson

# Halved sample spacing: 481 points (was 241)
t = np.linspace(0, 24, 481)
P = 500 + 200 * np.sin(2 * np.pi * t / 24)

trapz_wh   = np.trapz(P, t)
simpson_wh = simpson(P, t)

print(f"Energy trapezoidal: {trapz_wh/1000:.6f} kWh")
print(f"Energy Simpson:     {simpson_wh/1000:.6f} kWh")
print(f"Analytical:         {12.0:.6f} kWh")
