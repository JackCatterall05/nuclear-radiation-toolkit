import numpy as np
import pytest

from src.monte_carlo import (
    sample_free_paths,
    simulate_transmission,
    transmission_uncertainty
)


def test_number_of_paths():

    paths = sample_free_paths(
        attenuation_coefficient=0.5,
        number_of_particles=100
    )

    assert len(paths) == 100


def test_paths_are_positive():

    paths = sample_free_paths(
        attenuation_coefficient=0.5,
        number_of_particles=100
    )

    assert np.all(paths >= 0)


def test_invalid_attenuation_coefficient():

    with pytest.raises(ValueError):
        sample_free_paths(
            attenuation_coefficient=-0.5,
            number_of_particles=100
        )


def test_invalid_number_of_particles():

    with pytest.raises(ValueError):
        sample_free_paths(
            attenuation_coefficient=0.5,
            number_of_particles=-100
        )

def simulate_transmission(
    attenuation_coefficient,
    thickness,
    number_of_particles
):
    """
    Simulate particle transmission through shielding.

    Parameters
    ----------
    attenuation_coefficient : float
        Linear attenuation coefficient in cm^-1.

    thickness : float
        Shielding thickness in cm.

    number_of_particles : int
        Number of particles to simulate.

    Returns
    -------
    float
        Estimated transmission fraction.
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

def test_transmission_uncertainty():

    result = transmission_uncertainty(
        transmission=0.5,
        number_of_particles=10000
    )

    assert result == pytest.approx(0.005)

def test_invalid_transmission():

    with pytest.raises(ValueError):
        transmission_uncertainty(
            transmission=1.5,
            number_of_particles=100
        )

def test_invalid_particle_number_for_uncertainty():

    with pytest.raises(ValueError):
        transmission_uncertainty(
            transmission=0.5,
            number_of_particles=0
        )

def test_transmission_uncertainty():

    result = transmission_uncertainty(
        0.5,
        10000
    )

    expected = (
        (0.5 * 0.5 / 10000) ** 0.5
    )

    assert result == pytest.approx(
        expected
    )


def test_zero_transmission():

    result = transmission_uncertainty(
        0.0,
        10000
    )

    assert result == 0.0


def test_full_transmission():

    result = transmission_uncertainty(
        1.0,
        10000
    )

    assert result == 0.0