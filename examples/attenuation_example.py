import numpy as np
import matplotlib.pyplot as plt

from src.attenuation import transmitted_intensity
from src.materials import materials


thicknesses = np.linspace(0, 10, 200)

initial_intensity = 1.0

for material_name, material in materials.items():

    intensities = transmitted_intensity(
        initial_intensity,
        material["mu"],
        thicknesses
    )

    plt.plot(
        thicknesses,
        intensities,
        label=material_name
    )


plt.xlabel("Shielding thickness (cm)")
plt.ylabel("Transmitted intensity")
plt.title("Gamma-ray attenuation")

plt.legend()
plt.grid()

plt.savefig("figures/attenuation.png", dpi=300)

plt.show()