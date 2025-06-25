import numpy as np
import matplotlib.pyplot as plt
from IsingLattice import IsingLattice

n_rows = 8
n_cols = 8

runtime = 100000      
equil_skip = 20000     
n_repeats = 5     

temps = np.concatenate([
    np.arange(0.5, 1.8, 0.2),  
    np.arange(1.7, 3.3, 0.1),  
    np.arange(3.2, 5.1, 0.2)])

energies_mean = []
energies_std  = []
mags_mean     = []
mags_std      = []

for T in temps:
    E_vals = []
    M_vals = []
  
    for _ in range(n_repeats):
        # Create a fresh lattice for each run
        il = IsingLattice(n_rows, n_cols)
       
        # Random initial configuration 
        il.lattice = np.random.choice([-1, 1], size=(n_rows, n_cols))
      
        il.n_skip = equil_skip
       
        for step in range(runtime):
            il.montecarlostep(T)
        aveE, _, aveM, _, _ = il.statistics()
        E_vals.append(aveE)
        M_vals.append(aveM)   # take absolute value
  
    # Convert to numpy arrays
    E_vals = np.array(E_vals)
    M_vals = np.array(M_vals)
  
    # Mean and (sample) standard deviation across the repeats
    energies_mean.append(E_vals.mean())
    energies_std.append(E_vals.std(ddof=1))
    mags_mean.append(M_vals.mean())
    mags_std.append(M_vals.std(ddof=1))


fig, (axE, axM) = plt.subplots(2, 1, figsize=(8, 10))

# Energy
axE.errorbar(temps, energies_mean, yerr=energies_std, fmt='x-', capsize=5, markersize=4, elinewidth=1)
axE.set_ylabel("Energy per spin")
axE.set_xlabel("Temperature")
axE.set_ylim(-2.2, 0.2)

# Magnetisation
axM.errorbar(temps, mags_mean, yerr=mags_std, fmt='x-', capsize=5, markersize=4, elinewidth=1)
axM.set_ylabel("Magnetisation per spin (absolute)")
axM.set_xlabel("Temperature")
axM.set_ylim(-0.1, 1.1)

plt.tight_layout()
plt.show()