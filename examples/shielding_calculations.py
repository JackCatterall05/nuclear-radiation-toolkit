from src.attenuation import (
    half_value_layer,
    required_thickness
)


attenuation_coefficient = 0.5

hvl = half_value_layer(
    attenuation_coefficient
)

print(f"Half-value layer: {hvl:.3f} cm")


thickness = required_thickness(
    initial_intensity=100,
    final_intensity=10,
    attenuation_coefficient=0.5
)

print(
    f"Required shielding thickness: "
    f"{thickness:.3f} cm"
)