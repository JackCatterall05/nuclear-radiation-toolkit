from pathlib import Path

import numpy as np

from src.materials import materials


DATA_DIRECTORY = (
    Path(__file__).parent.parent / "data"
)


def load_attenuation_data(material):
    """
    Load mass attenuation coefficient data for a material.

    Parameters
    ----------
    material : str
        Name of the material.

    Returns
    -------
    energies : numpy.ndarray
        Gamma-ray energies in MeV.

    mass_attenuation_coefficients : numpy.ndarray
        Mass attenuation coefficients in cm^2/g.
    """

    if material not in materials:
        raise ValueError(
            f"Unknown material: {material}"
        )

    file_path = (
        DATA_DIRECTORY /
        f"{material}_attenuation.csv"
    )

    data = np.loadtxt(
        file_path,
        delimiter=",",
        skiprows=1
    )

    energies = data[:, 0]

    mass_attenuation_coefficients = data[:, 1]

    return (
        energies,
        mass_attenuation_coefficients
    )

def get_linear_attenuation_coefficient(
    material,
    energy
):
    """
    Calculate the linear attenuation coefficient for a
    material at a specified energy.

    Parameters
    ----------
    material : str
        Name of the material.

    energy : float
        Gamma-ray energy in MeV.

    Returns
    -------
    float
        Linear attenuation coefficient in cm^-1.
    """

    energies, mass_coefficients = (
        load_attenuation_data(material)
    )

    if energy < energies.min() or energy > energies.max():
        raise ValueError(
            "Energy is outside the available data range."
        )

    mass_coefficient = np.interp(
        energy,
        energies,
        mass_coefficients
    )

    density = materials[material]["density"]

    return mass_coefficient * density