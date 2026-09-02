import numpy as np

from src.data_loader import (
    load_attenuation_data
)


def test_load_lead_data():

    energies, coefficients = (
        load_attenuation_data("lead")
    )

    assert len(energies) > 0

    assert len(energies) == len(coefficients)

    assert np.all(energies > 0)

    assert np.all(coefficients > 0)