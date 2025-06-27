from IsingLattice import IsingLattice
from matplotlib import pyplot as plt
import numpy as np

n_rows = 8
n_cols = 8
temperature = 0.5
runtime = 5000
il = IsingLattice(n_rows, n_cols)
spins = n_rows * n_cols
times = range(runtime)
E = []
M = []
for i in times:
    if i % 100 == 0:
        print("Step ", i)
    energy, magnetisation = il.montecarlostep(temperature)
    E.append(energy)
    M.append(magnetisation)

# Create subplots using the modern approach
fig, (matax, enerax, magax) = plt.subplots(3, 1, figsize=(8, 10))

# Plot the lattice
matax.matshow(il.lattice)
matax.set_title('Ising Lattice Final State')

# Plot energy
enerax.set_ylabel("Energy per spin")
enerax.set_xlabel("Monte Carlo Steps")
enerax.set_ylim([-2.1, 2.1])
enerax.plot(times, np.array(E) / spins)

# Plot magnetisation
magax.set_ylabel("Magnetisation per spin")
magax.set_xlabel("Monte Carlo Steps")
magax.set_ylim([-1.1, 1.1])
magax.plot(times, np.array(M) / spins)

plt.tight_layout()
plt.show()
