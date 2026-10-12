
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import csv

# ----------- CONSTANT USER INPUTS -----------
a = 0.05639
inv_b = 84.7731        # 1/b in nm
lambda0 = 780          # nm

z_min = 0
z_max = 30000      # nm
g_end = -7000      # nm
N = 1000               # number of z samples

w_um = 342.166         # beam waist in microns
output_file = r"C:\Users\Asna\Downloads\gap_profile.csv"
# -------------------------------------------

# Convert w to nm
w_nm = w_um * 1000.0

# Generate z array
z = np.linspace(z_min, z_max, N)

# ----------- Define stable g(z) -----------
def g_func(zp, w):
    term1 = lambda0 / (a * np.sqrt(2 * np.pi**3) * w)
    term2 = np.exp(-2 * (zp / w)**2)
    term3 = 1 - erf(np.sqrt(2) * zp / w)

    # prevent log(0)
    term3 = np.clip(term3, 1e-300, None)

    return inv_b * (
        np.log(term3)
        - np.log(term1)
        - np.log(term2)
    )

# Compute g values
g_vals = g_func(z, w_nm)

# ----------- Linear Fit g = x*z + y -----------
x, y = np.polyfit(z, g_vals, 1)

g_fit = x * z + y

print("===== Linear Fit Results =====")
print(f"Slope (x)     = {x:.6e}")
print(f"Intercept (y) = {y:.6e}")

# ----------- Plotting -----------
plt.figure(figsize=(8,6))

plt.plot(z, g_vals, label=f"g(z), w = {w_um} µm")
plt.plot(z, g_fit, '--', label=f"Linear fit: g = {x:.3e} z + {y:.3e}")

plt.xlabel("z (nm)")
plt.ylabel("g(z)")
plt.title("g(z) and Linear Fit")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------- Save CSV (SI units, 2 decimal places) -----------
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    # Write computed data (convert nm → m)
    for g_val, z_val in zip(-1 * g_vals, z):
        g_si = g_val * 1e-9
        z_si = z_val * 1e-9
        writer.writerow([f"{g_si:.2e}", f"{z_si:.2e}"])

    # Append two extra points (also convert to SI)
    writer.writerow([f"{g_end*1e-9:.2e}", f"{z_max*1e-9:.2e}"])
    writer.writerow([f"{g_end*1e-9:.2e}", f"{z_min*1e-9:.2e}"])

print(f"\nSaved CSV in SI units: {output_file}")

print(f"\nSaved CSV: {output_file}")