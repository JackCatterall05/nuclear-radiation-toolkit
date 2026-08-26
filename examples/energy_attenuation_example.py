from src.energy_data import (
    get_attenuation_coefficient
)

from src.attenuation import (
    transmitted_intensity
)


material = "lead"
energy = 1.0

thickness = 5.0


attenuation_coefficient = (
    get_attenuation_coefficient(
        material,
        energy
    )
)


transmission = transmitted_intensity(
    initial_intensity=1.0,
    attenuation_coefficient=attenuation_coefficient,
    thickness=thickness
)


print(f"Material: {material}")
print(f"Gamma-ray energy: {energy} MeV")

print(
    f"Attenuation coefficient: "
    f"{attenuation_coefficient:.4f} cm^-1"
)

print(
    f"Transmission: "
    f"{transmission:.6f}"
)