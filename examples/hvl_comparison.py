from src.data_loader import (
    get_linear_attenuation_coefficient
)

from src.attenuation import (
    half_value_layer
)


energy = 1.0

materials = [
    "lead",
    "concrete"
]


for material in materials:

    mu = get_linear_attenuation_coefficient(
        material,
        energy
    )

    hvl = half_value_layer(mu)

    print(
        f"{material.capitalize()}: "
        f"μ = {mu:.5f} cm^-1, "
        f"HVL = {hvl:.3f} cm"
    )