# Nuclear Radiation Toolkit

A Python project investigating gamma-ray attenuation and Monte Carlo radiation transport.

## Author

Jack Catterall

## Goals

- Gamma attenuation
- Monte Carlo particle transport
- Detector simulation
- Radiation shielding

## Data sources

Photon attenuation data are obtained from the [NIST XCOM Photon Cross Sections Database](https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html).

The concrete composition used in this project is the NIST "Concrete, Ordinary" reference composition, with a density of 2.30 g/cm³.

The attenuation data are represented as mass attenuation coefficients, μ/ρ, in cm²/g. These are converted to linear attenuation coefficients using:

μ = (μ/ρ)ρ

where ρ is the material density in g/cm³.

### References

1. [NIST XCOM: Photon Cross Sections Database](https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html)
2. [NIST X-Ray Mass Attenuation Coefficients: Concrete, Ordinary](https://physics.nist.gov/PhysRefData/XrayMassCoef/ComTab/concrete.html)