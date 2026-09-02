from src.data_loader import (
    get_linear_attenuation_coefficient
)

from src.attenuation import (
    transmitted_intensity
)


material = "lead"

energy = 1.0

thickness = 5.0


mu = get_linear_attenuation_coefficient(
    material,
    energy
)


transmission = transmitted_intensity(
    initial_intensity=1.0,
    attenuation_coefficient=mu,
    thickness=thickness
)


print(f"Material: {material}")
print(f"Energy: {energy} MeV")
print(f"Linear attenuation coefficient: {mu:.5f} cm^-1")
print(f"Transmission: {transmission:.6f}")