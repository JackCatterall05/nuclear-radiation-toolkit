import pytest

from src.attenuation import transmitted_intensity


def test_zero_thickness():
    assert transmitted_intensity(100, 0.5, 0) == 100


def test_positive_thickness():
    result = transmitted_intensity(100, 0.5, 2)

    assert result == pytest.approx(36.7879, rel=1e-4)


def test_negative_thickness():
    with pytest.raises(ValueError):
        transmitted_intensity(100, 0.5, -1)