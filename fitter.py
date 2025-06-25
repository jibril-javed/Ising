import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("8x8_ref_C_chi.dat", skiprows=1)
T_all   = data[:, 0]
C_all   = data[:, 1]
chi_all = data[:, 2]

TminC, TmaxC = 0,5
degC = 10

maskC = (T_all > TminC) & (T_all < TmaxC)

T_Cfit = T_all[maskC]
C_Cfit = C_all[maskC]

coefC = np.polyfit(T_Cfit, C_Cfit, degC) # Perform the polynomial fit
T_Crange = np.linspace(TminC, TmaxC, 300)
C_fit    = np.polyval(coefC, T_Crange)


TminChi, TmaxChi = 1.7, 2.5 # Fit Susceptibility
degChi = 5
maskChi = (T_all > TminChi) & (T_all < TmaxChi)
T_Chifit = T_all[maskChi]
chi_Chifit = chi_all[maskChi]
coefChi = np.polyfit(T_Chifit, chi_Chifit, degChi)
T_Chirange = np.linspace(TminChi, TmaxChi, 300)
chi_fit = np.polyval(coefChi, T_Chirange)

fig, (axC, axChi) = plt.subplots(2, 1, figsize=(8, 10))

# Heat Capacity Plot
axC.plot(T_all, C_all, 'o', label="Raw Heat Capacity")
axC.plot(T_Crange, C_fit, '-', label=f"Poly deg={degC}, {TminC}<T<{TmaxC}")
axC.set_xlabel("Temperature")
axC.set_ylabel("Heat Capacity (per spin)")
axC.set_title("Heat Capacity vs Temperature Fit- 64x64 Lattice")
axC.legend()

# Susceptibility Plot
axChi.plot(T_all, chi_all, 'o', label="Raw Susceptibility")
axChi.plot(T_Chirange, chi_fit, '-', label=f"Poly deg={degChi}, {TminChi}<T<{TmaxChi}")
axChi.set_xlabel("Temperature")
axChi.set_ylabel("Susceptibility (per spin)")
axChi.set_title("Susceptibility vs Temperature (Peak-Only Fit)")
axChi.legend()

plt.tight_layout()
plt.savefig("16x16_peak_fits.png")
plt.show()

#Printing function
Cmax = np.max(C_fit)
Tmax = T_Crange[np.argmax(C_fit)]

print("Fitted Maximum heat capacity=", Cmax)
print("Temperature at which max C occurd =", Tmax)