import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import (
    load_attenuation_data
)

from src.materials import materials


MATERIALS = [
    "lead",
    "concrete"
]

TARGET_TRANSMISSION = 0.01

plt.figure()

for material in MATERIALS:

    energies, mass_coefficients = (
        load_attenuation_data(material)
    )

    density = materials[material]["density"]

    linear_coefficients = (
        mass_coefficients * density
    ) 

    hvl = (
        np.log(2) /
        linear_coefficients
    )

    required_thickness = (
        -np.log(TARGET_TRANSMISSION)
        / linear_coefficients
    )


    print(f"\n{material.capitalize()}")

    print("----------------")

    for energy, mu, value, thickness in zip(
        energies,
        linear_coefficients, 
        hvl, 
        required_thickness
    ):

        print(
            f"{energy:.3f} MeV: "
            f"μ = {mu:.5f} cm^-1"
            f" HVL = {value:.3f} cm"
            f" Thickness to reduce the intensity to 1% = {thickness:.3f} cm"
        )

    plt.plot(
        energies,
        required_thickness,
        marker="x",
        label=material.capitalize()
    )

plt.xlabel("Photon energy (MeV)")

plt.ylabel(
    "Required shielding thickness (cm)"
)

plt.title(
    "Shielding thickness to reduce transmission to 1% vs energy"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/required_thickness_vs_energy.png",
    dpi=300
)

plt.show()


plt.figure()

for material in MATERIALS:

    energies, mass_coefficients = (
        load_attenuation_data(material)
    )

    density = materials[material]["density"]

    linear_coefficients = (
        mass_coefficients * density
    )

    hvl = (
        np.log(2) /
        linear_coefficients
    )

    plt.plot(
        energies,
        hvl,
        marker="o",
        label=material.capitalize()
    )


plt.xlabel("Photon energy (MeV)")

plt.ylabel("Half-value layer (cm)")

plt.title(
    "Half-value layer vs photon energy"
)

plt.legend()

plt.grid()

plt.savefig(
    "figures/hvl_vs_energy.png",
    dpi=300
)

plt.show()