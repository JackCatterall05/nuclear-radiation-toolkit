import numpy as np


def transmitted_intensity(initial_intensity, attenuation_coefficient, thickness):
    """
    Calculate transmitted intensity through a material.

    Parameters
    ----------
    initial_intensity : float
        Initial radiation intensity.
    attenuation_coefficient : float
        Linear attenuation coefficient in cm^-1.
    thickness : float or numpy.ndarray
        Shielding thickness in cm.

    Returns
    -------
    float or numpy.ndarray
        Transmitted radiation intensity.
    """

    thickness = np.asarray(thickness)

    if np.any(thickness < 0):
        raise ValueError("Thickness cannot be negative.")

    if attenuation_coefficient < 0:
        raise ValueError("Attenuation coefficient cannot be negative.")

    return initial_intensity * np.exp(
        -attenuation_coefficient * thickness
    )

def half_value_layer(attenuation_coefficient):
    """
    Calculate the half-value layer.

    Parameters
    ----------
    attenuation_coefficient : float
        Linear attenuation coefficient in cm^-1.

    Returns
    -------
    float
        Half-value layer in cm.
    """

    if attenuation_coefficient <= 0:
        raise ValueError(
            "Attenuation coefficient must be greater than zero."
        )

    return np.log(2) / attenuation_coefficient

def required_thickness(
    initial_intensity,
    final_intensity,
    attenuation_coefficient
):
    """
    Calculate the shielding thickness required to reduce
    radiation from an initial intensity to a final intensity.

    Parameters
    ----------
    initial_intensity : float
        Initial radiation intensity.

    final_intensity : float
        Desired final radiation intensity.

    attenuation_coefficient : float
        Linear attenuation coefficient in cm^-1.

    Returns
    -------
    float
        Required shielding thickness in cm.
    """

    if initial_intensity <= 0:
        raise ValueError(
            "Initial intensity must be greater than zero."
        )

    if final_intensity <= 0:
        raise ValueError(
            "Final intensity must be greater than zero."
        )

    if attenuation_coefficient <= 0:
        raise ValueError(
            "Attenuation coefficient must be greater than zero."
        )

    if final_intensity > initial_intensity:
        raise ValueError(
            "Final intensity cannot be greater than initial intensity."
        )

    return -np.log(
        final_intensity / initial_intensity
    ) / attenuation_coefficient
