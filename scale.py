import numpy as np
import matplotlib.pyplot as plt

# Lattice sizes (L) and the corresponding peak temperatures (T_C)
L = np.array([2, 4, 8, 16, 32, 64], dtype=float)
T_C = np.array([
    2.5224080267558526,
    2.448160535117057,
    2.34247491638796,
    2.3153846153846156,
    2.294983277591973,
    2.283010033444816
], dtype=float)


# T_C(L) = A * (1/L) + T_C_infty
inv_L = 1.0 / L

# Fit a line: T_C(L) = slope * (1/L) + intercept
# slope ~ A, intercept ~ T_C_infty
coeff = np.polyfit(inv_L, T_C, 1)
A = coeff[0]
T_C_infty = coeff[1]

print("Fitted slope (A) =", A)
print("Fitted T_C_infty =", T_C_infty)


inv_L_dense = np.linspace(0, inv_L.max(), 200)
T_line = np.polyval(coeff, inv_L_dense)

plt.figure(figsize=(6, 5))
plt.plot(inv_L, T_C, 'x', label="Datapoints")
plt.plot(inv_L_dense, T_line, '-', label=f"Line of Best fit, Tc = {A:.4f}(1/L) + {T_C_infty:.4f}")
plt.xlabel("1/L")
plt.ylabel("Curie Temperature)")
plt.title("Curie Temperature plotted against 1/L")
plt.legend()
plt.tight_layout()
plt.savefig("Tc_scaling.png")
plt.show()

