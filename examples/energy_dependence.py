import numpy as np
import matplotlib.pyplot as plt

from src.energy_data import (
    get_attenuation_coefficient
)


energies = np.linspace(
    0.1,
    2.0,
    200
)


materials = [
    "lead",
    "concrete",
    "water"
]


for material in materials:

    coefficients = []

    for energy in energies:

        mu = get_attenuation_coefficient(
            material,
            energy
        )

        coefficients.append(mu)

    plt.plot(
        energies,
        coefficients,
        label=material
    )


plt.xlabel("Gamma-ray energy (MeV)")

plt.ylabel(
    "Linear attenuation coefficient (cm$^{-1}$)"
)

plt.title(
    "Energy dependence of gamma-ray attenuation"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/energy_dependence.png",
    dpi=300
)

plt.show()