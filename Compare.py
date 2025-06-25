import numpy as np
import matplotlib.pyplot as plt

# "8x8.dat" contains: T, E, E², M, M² (all normalized per spin)
sim_filename = "8x8.dat"
sim_data = np.loadtxt(sim_filename)
T_sim = sim_data[:, 0]
E_sim = sim_data[:, 1]
E2_sim = sim_data[:, 2]
M_sim = sim_data[:, 3]
M2_sim = sim_data[:, 4]

# Number of spins for an 8x8 lattice
N = 8*8  # change for diff size

# Compute heat capacity per spin from simulation:
# Total energy variance: Var(E_total) = N^2*(E2 - E^2).
# Per spin: C = Var(E_total)/(N T^2) = N*(E2 - E^2)/T^2.
C_sim = (E2_sim - E_sim**2) * N / (T_sim**2)

# Compute susceptibility per spin from simulation:
chi_sim = N * (M2_sim - M_sim**2) / T_sim

# For the order parameter plot, use the absolute magnetisation
M_sim_abs = np.abs(M_sim)

# ----- Load Reference Data -----
# "8x8_r.dat" contains: T, E, E², M, M², C (all normalized per spin)
ref_filename = "8x8_r.dat"
ref_data = np.loadtxt(ref_filename)
T_ref = ref_data[:, 0]
E_ref = ref_data[:, 1]
M_ref = ref_data[:, 3]  # net magnetisation per spin
M2_ref = ref_data[:, 4]
C_ref = ref_data[:, 5]

# Compute susceptibility per spin for reference data similarly:
chi_ref = N*(M2_ref - M_ref**2) / T_ref

# For plotting the order parameter, take absolute magnetisation:
M_ref_abs = np.abs(M_ref)

#Create 4 subplots: Energy, Magnetisation, Heat Capacity, and Susceptibility.
fig, (axE, axM, axC, axChi) = plt.subplots(2, 1, figsize=(10, 12))

# Energy vs Temperature
axE.plot(T_sim, E_sim, 'o-', label="Our Data: Energy")
axE.plot(T_ref, E_ref, 's-', label="Reference: Energy")
axE.set_xlabel("Temperature")
axE.set_ylabel("Energy per spin")
axE.set_title("Energy per spin vs Temperature (8x8 lattice)")
axE.legend()

# Magnetisation vs Temperature (order parameter)
axM.plot(T_sim, M_sim_abs, 'o-', label="Our Data: |Magnetisation|")
axM.plot(T_ref, M_ref_abs, 's-', label="Reference: |Magnetisation|")
axM.set_xlabel("Temperature")
axM.set_ylabel("Magnetisation per spin")
axM.set_title("Magnetisation per spin vs Temperature (8x8 lattice)")
axM.legend()

# Heat Capacity vs Temperature
axC.plot(T_sim, C_sim, 'o-', label="Our Data: Heat Capacity")
axC.plot(T_ref, C_ref, 's-', label="Reference: Heat Capacity")
axC.set_xlabel("Temperature")
axC.set_ylabel("Heat Capacity per spin")
axC.set_title("Heat Capacity per spin vs Temperature (32x32 lattice)")
axC.legend()

# Susceptibility vs Temperature
axChi.plot(T_sim, chi_sim, 'o-', label="Our Data: Susceptibility")
axChi.plot(T_ref, chi_ref, 's-', label="Reference: Susceptibility")
axChi.set_xlabel("Temperature")
axChi.set_ylabel("Susceptibility per spin")
axChi.set_title("Susceptibility per spin vs Temperature (32x32 lattice)")
axChi.legend()

plt.tight_layout()
plt.savefig("8x8_comparison_with_susceptibility.png")
plt.show()