import pytest

from src.attenuation import (
    transmitted_intensity,
    half_value_layer,
    required_thickness
)

def test_zero_thickness():
    assert transmitted_intensity(100, 0.5, 0) == 100


def test_positive_thickness():
    result = transmitted_intensity(100, 0.5, 2)

    assert result == pytest.approx(36.7879, rel=1e-4)


def test_negative_thickness():
    with pytest.raises(ValueError):
        transmitted_intensity(100, 0.5, -1)

def test_half_value_layer():
    result = half_value_layer(0.5)

    assert result == pytest.approx(
        1.386294,
        rel=1e-4
    )

def test_negative_hvl_coefficient():
    with pytest.raises(ValueError):
        half_value_layer(-0.5)

def test_required_thickness():
    result = required_thickness(
        100,
        50,
        0.5
    )

    assert result == pytest.approx(
        1.386294,
        rel=1e-4
    )

def test_invalid_final_intensity():
    with pytest.raises(ValueError):
        required_thickness(
            100,
            -50,
            0.5
        )