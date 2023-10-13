from usys.dim import DimensionalNumber, DIMENSION

m = DimensionalNumber(1.0, DIMENSION['LENGTH'])
kg = DimensionalNumber(1.0, DIMENSION['MASS'])
s = DimensionalNumber(1.0, DIMENSION['TIME'])
K = DimensionalNumber(1.0, DIMENSION['TEMPERATURE'])
A = DimensionalNumber(1.0, DIMENSION['CURRENT'])
mol = DimensionalNumber(1.0, DIMENSION['MOLE'])
Cd = DimensionalNumber(1.0, DIMENSION['LUMINOSITY'])


J = 1 * (kg * m**2 / s**2)
V = 1 * (J / (A * s))
c = 299792458 * (m / s)
hbar = 1.054571817e-34 * (J * s)
e = 1.602176634e-19 * (A * s)
eV = e * V
