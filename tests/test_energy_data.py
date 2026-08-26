import pytest

from src.energy_data import (
    get_attenuation_coefficient
)


def test_known_energy():

    result = get_attenuation_coefficient(
        "lead",
        0.5
    )

    assert result == pytest.approx(0.7)


def test_interpolated_energy():

    result = get_attenuation_coefficient(
        "lead",
        0.75
    )

    assert result == pytest.approx(0.6)


def test_unknown_material():

    with pytest.raises(ValueError):

        get_attenuation_coefficient(
            "unobtainium",
            1.0
        )


def test_invalid_energy():

    with pytest.raises(ValueError):

        get_attenuation_coefficient(
            "lead",
            -1.0
        )


def test_energy_outside_range():

    with pytest.raises(ValueError):

        get_attenuation_coefficient(
            "lead",
            10.0
        )