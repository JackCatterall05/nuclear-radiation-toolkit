from src.attenuation import transmitted_intensity
from src.monte_carlo import simulate_transmission


attenuation_coefficient = 0.5
thickness = 2.0

number_of_particles = 100000


analytical_transmission = transmitted_intensity(
    initial_intensity=1.0,
    attenuation_coefficient=attenuation_coefficient,
    thickness=thickness
)


monte_carlo_transmission = simulate_transmission(
    attenuation_coefficient=attenuation_coefficient,
    thickness=thickness,
    number_of_particles=number_of_particles
)


print(
    f"Analytical transmission: "
    f"{analytical_transmission:.5f}"
)

print(
    f"Monte Carlo transmission: "
    f"{monte_carlo_transmission:.5f}"
)