import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import (
    get_linear_attenuation_coefficient
)

from src.attenuation import (
    transmitted_intensity
)


energy = 1.0

thicknesses = np.linspace(
    0,
    20,
    200
)


materials = [
    "lead",
    "concrete"
]


for material in materials:

    mu = get_linear_attenuation_coefficient(
        material,
        energy
    )

    transmission = transmitted_intensity(
        initial_intensity=1.0,
        attenuation_coefficient=mu,
        thickness=thicknesses
    )

    plt.plot(
        thicknesses,
        transmission,
        label=material
    )


plt.xlabel("Shielding thickness (cm)")
plt.ylabel("Transmission")

plt.title(
    f"Radiation attenuation at {energy} MeV"
)

plt.yscale("log")

plt.legend()
plt.grid()

plt.savefig(
    "figures/material_comparison.png",
    dpi=300
)

plt.show()