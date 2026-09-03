import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import load_attenuation_data
from src.materials import materials


MATERIALS = ["lead", "concrete"]
TARGET_TRANSMISSION = 0.01


results = {}


for material in MATERIALS:

    energies, mass_coefficients = load_attenuation_data(
        material
    )

    density = materials[material]["density"]

    mu = mass_coefficients * density

    hvl = np.log(2) / mu

    required_thickness = (
        -np.log(TARGET_TRANSMISSION) / mu
    )

    results[material] = {
        "energy": energies,
        "mu": mu,
        "hvl": hvl,
        "thickness": required_thickness
    }


# --------------------------------------------------
# Plot 1: Linear attenuation coefficient
# --------------------------------------------------

plt.figure()

for material in MATERIALS:

    plt.plot(
        results[material]["energy"],
        results[material]["mu"],
        marker="o",
        label=material.capitalize()
    )

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Photon energy (MeV)")
plt.ylabel(r"Linear attenuation coefficient $\mu$ (cm$^{-1}$)")

plt.title("Linear attenuation coefficient vs photon energy")

plt.legend()
plt.grid()

plt.savefig(
    "figures/linear_attenuation_vs_energy.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# Plot 2: HVL
# --------------------------------------------------

plt.figure()

for material in MATERIALS:

    plt.plot(
        results[material]["energy"],
        results[material]["hvl"],
        marker="o",
        label=material.capitalize()
    )

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Photon energy (MeV)")
plt.ylabel("Half-value layer (cm)")

plt.title("Half-value layer vs photon energy")

plt.legend()
plt.grid()

plt.savefig(
    "figures/final_hvl_comparison.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# Plot 3: Required shielding thickness
# --------------------------------------------------

plt.figure()

for material in MATERIALS:

    plt.plot(
        results[material]["energy"],
        results[material]["thickness"],
        marker="o",
        label=material.capitalize()
    )

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Photon energy (MeV)")
plt.ylabel("Required thickness (cm)")

plt.title(
    "Shielding thickness to reduce transmission to 1% vs photon energy"
)

plt.legend()
plt.grid()

plt.savefig(
    "figures/final_shielding_comparison.png",
    dpi=300
)

plt.show()

print("\nFinal shielding comparison")
print("--------------------------")

for material in MATERIALS:

    energy = results[material]["energy"]
    hvl = results[material]["hvl"]
    thickness = results[material]["thickness"]

    print(f"\n{material.capitalize()}")

    for i in range(len(energy)):

        print(
            f"{energy[i]:.3f} MeV: "
            f"HVL = {hvl[i]:.3f} cm, "
            f"1% thickness = {thickness[i]:.3f} cm"
        )

ratio = (
    results["concrete"]["thickness"]
    / results["lead"]["thickness"]
)
print("\nConcrete / Lead thickness ratio")

Energy = np.array([])
Value = np.array([])

for energy, value in zip(
    results["lead"]["energy"],
    ratio
):

    print(
        f"{energy:.3f} MeV: "
        f"{value:.2f}"
    )
	
    Energy = np.append(Energy, energy)
    Value = np.append(Value, value)


# --------------------------------------------------
# Plot 4: Ratio
# --------------------------------------------------

plt.plot(
        Energy,
        Value,
        marker="o",
    )

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Photon energy (MeV)")
plt.ylabel("Concrete to lead ratio")

plt.title("1% thickness ratio of concrete to lead vs photon energy")

plt.grid()

plt.savefig(
    "figures/final_ratio_comparison.png",
    dpi=300
)

plt.show()
