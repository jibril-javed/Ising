import numpy as np
import matplotlib.pyplot as plt

lattice_sizes = [2,4,8]
fig, (axC, axChi) = plt.subplots(2, 1, figsize=(8, 10))

for size in lattice_sizes:
    filename = f"{size}x{size}.dat"
    data = np.loadtxt(filename)
    T        = data[:, 0]  # Temperature
    E_mean   = data[:, 1]  # <E> per spin
    E2_mean  = data[:, 2]  # <E^2> per spin^2
    M_mean   = data[:, 3]  # <M> per spin
    M2_mean  = data[:, 4]  # <M^2> per spin^2

    # Number of spins
    N = size * size
    
    # var(e) = <e^2> - <e>^2
    var_e = E2_mean - E_mean**2
    # var(m) = <m^2> - <m>^2
    var_m = M2_mean - M_mean**2

    # ----------------------------
    # Heat Capacity: 
    #   C = N^2 * var(e) / T^2
    # ----------------------------
    C = N**2 * var_e / (T**2)

    # ----------------------------
    # Susceptibility:
    #   χ = (1/T) * N^2 * var(m)
    # ----------------------------
    chi = N**2 * var_m / T

    axC.plot(T, C, label=f"{size}x{size}")
    axChi.plot(T, chi, label=f"{size}x{size}")

axC.set_xlabel("Temperature")
axC.set_ylabel("Heat Capacity, C")
axC.set_title("Heat Capacity vs Temperature")
axC.legend()

axChi.set_xlabel("Temperature")
axChi.set_ylabel("Susceptibility, χ")
axChi.set_title("Susceptibility vs Temperature")
axChi.legend()

plt.tight_layout()
plt.show()