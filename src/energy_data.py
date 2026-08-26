import numpy as np


material_data = {
    "lead": {
        "energies": np.array([
            0.1,
            0.5,
            1.0,
            2.0
        ]),

        "attenuation_coefficients": np.array([
            5.0,
            0.7,
            0.5,
            0.3
        ])
    },

    "concrete": {
        "energies": np.array([
            0.1,
            0.5,
            1.0,
            2.0
        ]),

        "attenuation_coefficients": np.array([
            0.4,
            0.15,
            0.1,
            0.07
        ])
    },

    "water": {
        "energies": np.array([
            0.1,
            0.5,
            1.0,
            2.0
        ]),

        "attenuation_coefficients": np.array([
            0.17,
            0.10,
            0.07,
            0.05
        ])
    }
}

def get_attenuation_coefficient(
    material,
    energy
):
    """
    Return the attenuation coefficient for a material
    at a specified gamma-ray energy.

    Parameters
    ----------
    material : str
        Name of the shielding material.

    energy : float
        Gamma-ray energy in MeV.

    Returns
    -------
    float
        Interpolated attenuation coefficient.
    """

    if material not in material_data:
        raise ValueError(
            f"Unknown material: {material}"
        )

    if energy <= 0:
        raise ValueError(
            "Energy must be greater than zero."
        )

    energies = material_data[material]["energies"]

    coefficients = material_data[material][
        "attenuation_coefficients"
    ]

    if energy < energies.min() or energy > energies.max():
        raise ValueError(
            "Energy is outside the available data range."
        )

    return np.interp(
        energy,
        energies,
        coefficients
    )