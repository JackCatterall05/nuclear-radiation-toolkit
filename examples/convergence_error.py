import numpy as np
import matplotlib.pyplot as plt

from src.attenuation import transmitted_intensity
from src.monte_carlo import simulate_transmission


attenuation_coefficient = 0.5
thickness = 2.0

particle_numbers = np.array([
    100,
    300,
    1000,
    3000,
    10000,
    30000,
    100000
])


analytical_result = transmitted_intensity(
    1.0,
    attenuation_coefficient,
    thickness
)


errors = []


for number_of_particles in particle_numbers:

    monte_carlo_result = simulate_transmission(
        attenuation_coefficient,
        thickness,
        number_of_particles
    )

    error = abs(
        monte_carlo_result - analytical_result
    )

    errors.append(error)


plt.plot(
    particle_numbers,
    errors,
    marker="o"
)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Number of simulated particles")
plt.ylabel("Absolute error")

plt.title("Monte Carlo error convergence")

plt.grid()

plt.savefig(
    "figures/monte_carlo_error.png",
    dpi=300
)

plt.show()