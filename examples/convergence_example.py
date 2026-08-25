import numpy as np
import matplotlib.pyplot as plt

from src.attenuation import transmitted_intensity
from src.monte_carlo import (
    simulate_transmission,
    transmission_uncertainty
)


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


analytical_transmission = transmitted_intensity(
    initial_intensity=1.0,
    attenuation_coefficient=attenuation_coefficient,
    thickness=thickness
)


monte_carlo_results = []
uncertainties = []


for number_of_particles in particle_numbers:

    transmission = simulate_transmission(
        attenuation_coefficient,
        thickness,
        number_of_particles
    )

    uncertainty = transmission_uncertainty(
        transmission,
        number_of_particles
    )

    monte_carlo_results.append(transmission)
    uncertainties.append(uncertainty)


plt.errorbar(
    particle_numbers,
    monte_carlo_results,
    yerr=uncertainties,
    marker="o",
    linestyle=""
)

plt.axhline(
    analytical_transmission,
    linestyle="--",
    label="Analytical result"
)

plt.xscale("log")

plt.xlabel("Number of simulated particles")
plt.ylabel("Transmission fraction")

plt.title("Monte Carlo convergence")

plt.legend()
plt.grid()

plt.savefig(
    "figures/monte_carlo_convergence.png",
    dpi=300
)

plt.show()