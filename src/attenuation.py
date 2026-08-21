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