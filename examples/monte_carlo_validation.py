from src.attenuation import transmitted_intensity
from src.data_loader import get_linear_attenuation_coefficient
from src.monte_carlo import (
    simulate_transmission,
    transmission_uncertainty
)


material_pb = "lead"
energy = 1.0
thickness_pb = 5.718
number_of_particles = 100000

material_con = "concrete"
thickness_con = 30.828


mu_pb = get_linear_attenuation_coefficient(
    material_pb,
    energy
)


analytical_pb = transmitted_intensity(
    1.0,
    mu_pb,
    thickness_pb
)


monte_carlo_pb = simulate_transmission(
    mu_pb,
    thickness_pb,
    number_of_particles
)


uncertainty_pb = transmission_uncertainty(
    monte_carlo_pb,
    number_of_particles
)


print("Monte Carlo validation")
print("----------------------")
print(f"Material: {material_pb}")
print(f"Energy: {energy} MeV")
print(f"Thickness: {thickness_pb:.3f} cm")
print(f"Attenuation coefficient: {mu_pb:.5f} cm^-1")
print()
print(f"Analytical transmission: {analytical_pb:.6f}")
print(
    f"Monte Carlo transmission: "
    f"{monte_carlo_pb:.6f} ± {uncertainty_pb:.6f}"
)

difference_pb = abs(
    monte_carlo_pb - analytical_pb
)

print(
    f"Absolute difference: "
    f"{difference_pb:.6f}"
)

z_score_pb = (
    monte_carlo_pb - analytical_pb
) / uncertainty_pb

print(
    f"Difference in standard deviations: "
    f"{z_score_pb:.2f}"
)

mu_con = get_linear_attenuation_coefficient(
    material_con,
    energy
)


analytical_con = transmitted_intensity(
    1.0,
    mu_con,
    thickness_con
)


monte_carlo_con = simulate_transmission(
    mu_con,
    thickness_con,
    number_of_particles
)


uncertainty_con = transmission_uncertainty(
    monte_carlo_con,
    number_of_particles
)


print("Monte Carlo validation")
print("----------------------")
print(f"Material: {material_con}")
print(f"Energy: {energy} MeV")
print(f"Thickness: {thickness_con:.3f} cm")
print(f"Attenuation coefficient: {mu_con:.5f} cm^-1")
print()
print(f"Analytical transmission: {analytical_con:.6f}")
print(
    f"Monte Carlo transmission: "
    f"{monte_carlo_con:.6f} ± {uncertainty_con:.6f}"
)

difference_con = abs(
    monte_carlo_con - analytical_con
)

print(
    f"Absolute difference: "
    f"{difference_con:.6f}"
)

z_score_con = (
    monte_carlo_con - analytical_con
) / uncertainty_con

print(
    f"Difference in standard deviations: "
    f"{z_score_con:.2f}"
)