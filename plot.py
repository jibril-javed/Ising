import numpy as np
import matplotlib.pyplot as plt

lattice_sizes = [2, 4, 8, 16, 32]

plt.figure(figsize=(8, 6))

for size in lattice_sizes:
    filename = f"{size}x{size}.dat" 
    data = np.loadtxt(filename)      
    T = data[:, 0]
    E_mean = data[:, 1]
    E_std = data[:, 2]
   
    # Overlay each lattice size's data with error bars
    plt.errorbar(T, E_mean, yerr=E_std,
                 label=f"{size}x{size}",
                 marker='o', linestyle='-', capsize=4)

plt.xlabel("Temperature")
plt.ylabel("Energy per spin")
plt.title("Energy vs. Temperature for Different Lattice Sizes")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))

for size in lattice_sizes:
    filename = f"{size}x{size}.dat"
    data = np.loadtxt(filename)
    T = data[:, 0]
    M_mean = data[:, 3]
    M_std = data[:, 4]
   
    plt.errorbar(T, M_mean, yerr=M_std,
                 label=f"{size}x{size}",
                 marker='o', linestyle='-', capsize=4)

plt.xlabel("Temperature")
plt.ylabel("Magnetisation per spin")
plt.title("Magnetisation vs. Temperature for Different Lattice Sizes")
plt.legend()
plt.tight_layout()
plt.show()