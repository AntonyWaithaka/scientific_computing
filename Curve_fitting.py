import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Extended time range to 10 and added more data
t_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2.1, 2.8, 3.9, 5.1, 6.8, 8.9,
                   11.7, 15.4, 20.2, 26.5, 34.8])

def model(t, a, b):
    return a * np.exp(b * t)

popt, pcov = curve_fit(model, t_data, y_data, p0=[2.0, 0.2])
perr = np.sqrt(np.diag(pcov))

print(f"Fitted a = {popt[0]:.4f} +/- {perr[0]:.4f}")
print(f"Fitted b = {popt[1]:.4f} +/- {perr[1]:.4f}")
rmse = np.sqrt(np.mean((y_data - model(t_data, *popt))**2))
print(f"RMSE: {rmse:.4f}")

t_fit = np.linspace(0, 10, 100)
plt.scatter(t_data, y_data, label="Data")
plt.plot(t_fit, model(t_fit, *popt), 'r-', label="Fit")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Exponential growth fit")
plt.legend(); plt.grid(True)
plt.savefig("plots/curve_fit_task14.png", dpi=120)
plt.show()
