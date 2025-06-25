import numpy as np


class IsingLattice:
    def __init__(self, n_rows, n_cols, tol=1e-5, max_steps=100000):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.tol = tol
        self.n_skip = 10000
        self.max_steps = max_steps
        self.lattice = np.random.choice([-1, 1], size=(n_rows, n_cols))

        current_en = self.energy()
        current_mag = self.magnetisation()

        # Running tallies
        self.E_tally = current_en
        self.E2_tally = current_en**2
        self.M_tally = current_mag
        self.M2_tally = current_mag**2

        self.n_steps = 0
        self.prev_avg_E = None
        self.prev_avg_M = None

    def energy(self):
        """Return the total energy of the current lattice configuration using NumPy roll and sum."""
        right = np.roll(self.lattice, shift=-1, axis=1)
        left = np.roll(self.lattice, shift=1, axis=1)
        bottom = np.roll(self.lattice, shift=-1, axis=0)
        top = np.roll(self.lattice, shift=1, axis=0)
        
        energy = -np.sum(self.lattice * (right + left + bottom + top)) / 2
        return energy

    def magnetisation(self):
        """Return the total magnetisation of the current lattice configuration using NumPy sum."""
        return np.sum(self.lattice)

    def montecarlostep(self, temp):
        """Performs one step on IsingLattice object using the Metropolis Monte Carlo method ."""
        #picks a random row and column to result in the flipping of a random spin
        random_i = np.random.randint(self.n_rows) 
        random_j = np.random.randint(self.n_cols)
    
        dE = self.delta_energy(random_i, random_j) #calls the change in energy function for the given spin flip
    
        # Only allows said flip based on the algorithm's energy rules
        if dE <= 0 or np.random.rand() < np.exp(-dE / temp):
            self.lattice[random_i, random_j] *= -1  # Flip the spin (if allowed)

        #now update emnergy/ magnetisation
        energy = self.energy()
        magnetisation = self.magnetisation()
        self.n_steps += 1
    
        # Update the tallies
       # Perform averaging only after the equilibration period
        if self.n_steps >= self.n_skip:
            self.E_tally += energy
            self.E2_tally += energy**2
            self.M_tally += magnetisation
            self.M2_tally += magnetisation**2
        
            
        return energy, magnetisation
         

    def run_simulation(self, temp):
        """Runs the Monte Carlo simulation until convergence or max steps reached."""
        while self.n_steps < self.max_steps:
            self.montecarlostep(temp)  # Call single-step function
            avg_E, _, avg_M, _, _ = self.statistics()
      
            self.prev_avg_E = avg_E
            self.prev_avg_M = avg_M


    def statistics(self):
        """Return the average energy per spin, squared energy per spin, 
           magnetisation per spin, squared magnetisation per spin, and steps."""
        if self.n_steps <= self.n_skip:  # Only return averages after eq.
            return 0, 0, 0, 0, 0

        num_samples= self.n_steps - self.n_skip # We are now only dividing by steps that are after eq.
        num_spins = self.n_rows * self.n_cols  # Total number of spins
        
        avg_E = self.E_tally / (num_samples * num_spins)  # Energy per spin
        avg_E2 = self.E2_tally / (num_samples * num_spins**2)  
        avg_M = self.M_tally / (num_samples * num_spins)  # Magnetization per 
        avg_M2 = self.M2_tally / (num_samples * num_spins**2)  
        return avg_E, avg_E2, avg_M, avg_M2, self.n_steps

    

    def delta_energy(self, i, j):
        """Return the change in energy if the spin at (i,j) were to be flipped."""
        spin = self.lattice[i, j]
        neighbors = (
            self.lattice[i, (j + 1) % self.n_cols] +
            self.lattice[i, (j - 1) % self.n_cols] +
            self.lattice[(i + 1) % self.n_rows, j] +
            self.lattice[(i - 1) % self.n_rows, j])
        return 2 * spin * neighbors

    
