import numpy as np

N=16*16

# "8x8_r.dat" contains: T, E, E², M, M², C (all normalized per spin)
ref_filename = "64x64_r.dat"
ref_data = np.loadtxt(ref_filename)
T = ref_data[:, 0]
E = ref_data[:, 1]
M = ref_data[:, 3]  # net magnetisation per spin
M2 = ref_data[:, 4]
C = ref_data[:, 5]

# Compute susceptibility per spin for reference data similarly:
chi = N*(M2 - M**2) / T

out_data=np.column_stack((T, C, chi))

np.savetxt("64x64_ref_C_Chi.dat", out_data, header="T C chi", comments="")