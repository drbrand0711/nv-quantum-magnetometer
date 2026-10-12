import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ---- Load data ----
data = np.loadtxt(r"C:\Users\Asna\Downloads\gap,neff_data.txt")
g = data[:, 0]
neff_real = data[:, 1]
neff_imag = data[:, 2]

# ---- Exponential model ----
def exp_model(g, a, b):
    return a * np.exp(-b * g)

# ---- Fit ----
popt, pcov = curve_fit(exp_model, g, neff_imag, p0=(1e-2, 0.01))
a_fit, b_fit = popt

print("Fitted parameters:")
print(f"a = {a_fit}")
print(f"1/b = {1/b_fit}")

# Generate smooth fitted curve
g_fit = np.linspace(min(g), max(g), 400)
neff_imag_fit = exp_model(g_fit, a_fit, b_fit)

# ---- Plot log-scale imag(n_eff) ----
plt.figure(figsize=(7,5))
plt.plot(g, neff_imag, 'o', label='Raw Data')
plt.plot(g_fit, neff_imag_fit, '-', label=f'Fit: a * exp(-b*g)\n a={a_fit:.3e},  b={b_fit:.3e}')
plt.yscale("log")
plt.xlabel("Gap (nm)")
plt.ylabel("Imag(n_eff)")
plt.title("Imag(n_eff) vs Gap (log scale) with Exponential Fit")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.show()
