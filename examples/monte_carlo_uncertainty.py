import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import get_linear_attenuation_coefficient
from src.monte_carlo import (
    simulate_transmission,
    transmission_uncertainty
)
from src.attenuation import transmitted_intensity


material = "lead"
energy = 1.0
thickness = 5.718

particle_numbers = np.array([
    1000,
    3000,
    10000,
    30000,
    100000,
    300000,
    1000000
])

number_of_runs = 20


mu = get_linear_attenuation_coefficient(
    material,
    energy
)

analytical = transmitted_intensity(
    1.0,
    mu,
    thickness
)


mean_transmissions = []
measured_uncertainties = []
theoretical_uncertainties = []


for number_of_particles in particle_numbers:

    results = []

    for _ in range(number_of_runs):

        transmission = simulate_transmission(
            mu,
            thickness,
            number_of_particles
        )

        results.append(transmission)

    results = np.array(results)

    mean = np.mean(results)
    measured_uncertainty = np.std(results, ddof=1)

    theoretical_uncertainty = transmission_uncertainty(
        mean,
        number_of_particles
    )

    mean_transmissions.append(mean)
    measured_uncertainties.append(measured_uncertainty)
    theoretical_uncertainties.append(
        theoretical_uncertainty
    )

    print(
        f"N = {number_of_particles:>7}: "
        f"mean = {mean:.6f}, "
        f"measured σ = {measured_uncertainty:.6f}, "
        f"theoretical σ = {theoretical_uncertainty:.6f}"
    )


mean_transmissions = np.array(mean_transmissions)
measured_uncertainties = np.array(measured_uncertainties)
theoretical_uncertainties = np.array(
    theoretical_uncertainties
)


plt.figure()

plt.errorbar(
    particle_numbers,
    mean_transmissions,
    yerr=measured_uncertainties,
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
    "Monte Carlo uncertainty and convergence"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/monte_carlo_uncertainty.png",
    dpi=300
)

plt.show()


plt.figure()

plt.loglog(
    particle_numbers,
    measured_uncertainties,
    marker="o",
    label="Measured uncertainty"
)

plt.loglog(
    particle_numbers,
    theoretical_uncertainties,
    marker="o",
    label="Theoretical uncertainty"
)

plt.loglog(
    particle_numbers,
    theoretical_uncertainties[0]
    * np.sqrt(
        particle_numbers[0] / particle_numbers
    ),
    linestyle="--",
    label=r"$1/\sqrt{N}$"
)

plt.xlabel("Number of simulated photons")

plt.ylabel("Uncertainty")

plt.title(
    "Monte Carlo statistical uncertainty"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/monte_carlo_uncertainty_scaling.png",
    dpi=300
)

plt.show()