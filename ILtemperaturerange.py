from IsingLattice import IsingLattice
from matplotlib import pyplot as plt
import numpy as np

n_rows = 32
n_cols = 32
il = IsingLattice(n_rows, n_cols)
il.lattice = np.ones((n_rows, n_cols))

# recalculate the energy after changing the lattice
il.energy()
il.magnetisation()

spins = n_rows * n_cols
runtime = 30000
times = range(runtime)
temps = np.concatenate([
    np.arange(0.5, 1.5, 0.2),  # 0.5 -> 1.7
    np.arange(1.4, 3.3, 0.05),  # 1.7 -> 3.2
    np.arange(3.2, 5.1, 0.2)   # 3.2 -> 5.0
])

energies = []
magnetisations = []
energysq = []
magnetisationsq = []
for t in temps:
    il.lattice = np.ones((n_rows, n_cols))
    il.energy()
    il.magnetisation()
    for i in times:
        if i % 1000 == 0:
            print(t, i)
        energy, magnetisation = il.montecarlostep(t)
    aveE, aveE2, aveM, aveM2, n_steps = il.statistics()
    energies.append(aveE)
    energysq.append(aveE2)
    magnetisations.append(aveM)
    magnetisationsq.append(aveM2)
    # reset the IL object for the next cycle
    il.E_tally = 0.0
    il.E2_tally = 0.0
    il.M_tally = 0.0
    il.M2_tally = 0.0
    il.n_steps = 0
fig = plt.figure()
enerax = fig.add_subplot(2, 1, 1)
enerax.set_ylabel("Energy per spin")
enerax.set_xlabel("Temperature")
enerax.set_ylim((-2.1, 0.1))
magax = fig.add_subplot(2, 1, 2)
magax.set_ylabel("Magnetisation per spin")
magax.set_xlabel("Temperature")
magax.set_ylim((-1.1, 1.1))
enerax.plot(temps, np.array(energies))
magax.plot(temps, np.array(magnetisations))
plt.show()

final_data = np.column_stack(
    (temps, energies, energysq, magnetisations, magnetisationsq)
)
np.savetxt(f"{n_rows}x{n_cols}.dat", final_data)
