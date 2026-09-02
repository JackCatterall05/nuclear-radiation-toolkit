import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import (
    get_linear_attenuation_coefficient
)

from src.monte_carlo import (
    simulate_transmission,
    transmission_uncertainty
)

from src.attenuation import (
    transmitted_intensity
)


material = "lead"
energy = 1.0
thickness = 5.718

particle_numbers = np.array([
    100,
    1000,
    10000,
    100000,
    1000000
])


mu = get_linear_attenuation_coefficient(
    material,
    energy
)


analytical = transmitted_intensity(
    1.0,
    mu,
    thickness
)


transmissions = []
uncertainties = []


for number_of_particles in particle_numbers:

    transmission = simulate_transmission(
        mu,
        thickness,
        number_of_particles
    )

    uncertainty = transmission_uncertainty(
        transmission,
        number_of_particles
    )

    transmissions.append(transmission)
    uncertainties.append(uncertainty)


    print(
        f"N = {number_of_particles:>7}: "
        f"T = {transmission:.6f} "
        f"+/- {uncertainty:.6f}"
    )


plt.figure()

plt.errorbar(
    particle_numbers,
    transmissions,
    yerr=uncertainties,
    marker="o",
    linestyle="none",
    capsize=4,
    label="Monte Carlo"
)

plt.axhline(
    analytical,
    linestyle="--",
    label="Analytical"
)

plt.xscale("log")

plt.xlabel("Number of simulated photons")

plt.ylabel("Transmission")

plt.title(
    "Monte Carlo convergence"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/monte_carlo_convergence.png",
    dpi=300
)

plt.show()