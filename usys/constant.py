import numpy as np
from usys.dim import DimensionalNumber, DIMENSION

# SI unit system
m = DimensionalNumber(1.0, DIMENSION['LENGTH'])
kg = DimensionalNumber(1.0, DIMENSION['MASS'])
s = DimensionalNumber(1.0, DIMENSION['TIME'])
K = DimensionalNumber(1.0, DIMENSION['TEMPERATURE'])
A = DimensionalNumber(1.0, DIMENSION['CURRENT'])
mol = DimensionalNumber(1.0, DIMENSION['MOLE'])
Cd = DimensionalNumber(1.0, DIMENSION['LUMINOSITY'])

# Other useful unit
J = 1 * (kg * m**2 / s**2)
V = 1 * (J / (A * s))
W = 1 * (J / s)
N = 1 * (kg * m / s**2)
Pa = 1 * (N / m**2)
C = 1 * (A * s)

c = 2.99792458e8 * (m / s)
hbar = 1.054571817e-34 * (J * s)
kb = 1.380649e-23 * (J / K)
g = 6.67430e-11 * (m**3 / (kg * s**2))
e = 1.602176634e-19 * (A * s)
eps0 = 8.8541878128e-12 * (A * s / (V * m))
mu0 = 1.25663706212e-6 * (V * s / (A * m))

h = hbar * 2 * np.pi
eV = e * V
