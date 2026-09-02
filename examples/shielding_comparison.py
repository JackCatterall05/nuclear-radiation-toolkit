from src.data_loader import (
    get_linear_attenuation_coefficient
)

from src.attenuation import (
    required_thickness
)


energy = 1.0

initial_intensity = 1.0
final_intensity = 0.01


materials = [
    "lead",
    "concrete"
]


for material in materials:

    mu = get_linear_attenuation_coefficient(
        material,
        energy
    )

    thickness = required_thickness(
        initial_intensity,
        final_intensity,
        mu
    )

    print(
        f"{material.capitalize()}: "
        f"{thickness:.3f} cm required"
    )