import numpy as np


def sample_free_paths(attenuation_coefficient, number_of_particles):
    """
    Generate random distances travelled by particles before
    their first interaction.

    Parameters
    ----------
    attenuation_coefficient : float
        Linear attenuation coefficient in cm^-1.

    number_of_particles : int
        Number of particles to simulate.

    Returns
    -------
    numpy.ndarray
        Random free paths in cm.
    """

    if attenuation_coefficient <= 0:
        raise ValueError(
            "Attenuation coefficient must be greater than zero."
        )

    if number_of_particles <= 0:
        raise ValueError(
            "Number of particles must be greater than zero."
        )

    return np.random.exponential(
        scale=1 / attenuation_coefficient,
        size=number_of_particles
    )

def simulate_transmission(
    attenuation_coefficient,
    thickness,
    number_of_particles
):
    """
    Simulate particle transmission through shielding.
    """

    if thickness < 0:
        raise ValueError(
            "Thickness cannot be negative."
        )

    free_paths = sample_free_paths(
        attenuation_coefficient,
        number_of_particles
    )

    transmitted = free_paths > thickness

    return np.mean(transmitted)

def transmission_uncertainty(transmission, number_of_particles):
    """
    Calculate the statistical uncertainty in a Monte Carlo
    transmission estimate.

    Parameters
    ----------
    transmission : float
        Estimated transmission fraction.

    number_of_particles : int
        Number of simulated particles.

    Returns
    -------
    float
        Statistical uncertainty in the transmission fraction.
    """

    if transmission < 0 or transmission > 1:
        raise ValueError(
            "Transmission must be between 0 and 1."
        )

    if number_of_particles <= 0:
        raise ValueError(
            "Number of particles must be greater than zero."
        )

    return np.sqrt(
        transmission * (1 - transmission)
        / number_of_particles
    )
