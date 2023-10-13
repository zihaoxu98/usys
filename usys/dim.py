import numpy as np
from .unit_system import *
from .utils import hot_array, differ_by_null


class DimensionalNumberBase():
    value = 0
    dim = hot_array(len(DIMENSION_INDEX), [])

    def __init__(self, value, dim):
        self.value = value
        self.dim = dim

    def __add__(self, other):
        if isinstance(other, DimensionalNumber):
            if np.any(self.dim != other.dim):
                raise ValueError("Incompatible dimension!")
            return DimensionalNumber(self.value + other.value, self.dim)
        else:
            return DimensionalNumber(self.value + other, self.dim)

    def __sub__(self, other):
        if isinstance(other, DimensionalNumber):
            if np.any(self.dim != other.dim):
                raise ValueError("Incompatible dimension!")
            return DimensionalNumber(self.value - other.value, self.dim)
        else:
            return DimensionalNumber(self.value - other, self.dim)

    def __mul__(self, other):
        if isinstance(other, DimensionalNumber):
            return DimensionalNumber(self.value * other.value, self.dim + other.dim)
        else:
            return DimensionalNumber(self.value * other, self.dim)

    def __truediv__(self, other):
        if isinstance(other, DimensionalNumber):
            return DimensionalNumber(self.value / other.value, self.dim - other.dim)
        else:
            return DimensionalNumber(self.value / other, self.dim)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, DimensionalNumber):
            if np.any(self.dim != other.dim):
                raise ValueError("Incompatible dimension!")
            return DimensionalNumber(other.value - self.value, self.dim)
        else:
            return DimensionalNumber(other - self.value, self.dim)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        if isinstance(other, DimensionalNumber):
            return DimensionalNumber(other.value / self.value, other.dim - self.dim)
        else:
            return DimensionalNumber(other / self.value, -self.dim)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __pow__(self, power):
        return DimensionalNumber(self.value ** power, self.dim * power)

    def __str__(self):
        dimension = [f'[{dim}]^{power}' for dim, power in zip(list(DIMENSION_INDEX.keys()), self.dim) if power != 0]
        if len(dimension) == 0:
            return str(self.value)
        else:
            return str(self.value) + ' x ' + ' '.join(dimension)

    def __repr__(self):
        return 'DimensionalNumberBase(' + self.__str__() + ')'


class DimensionalNumber(DimensionalNumberBase):
    def __init__(self, value, dim):
        super().__init__(value, dim)

    def have_same_dimension(self, other):
        return differ_by_null(self.dim, other.dim, UNIT_SYSTEM['NULL']['DIMENSION'])

    def in_unit(self, unit):
        if not self.have_same_dimension(unit):
            raise ValueError("Incompatible dimension!")
        else:
            dim_diff = np.atleast_2d(self.dim - unit.dim).T
            basis = np.array(UNIT_SYSTEM['BASIS']['DIMENSION']).T
            exps = np.linalg.solve(basis, dim_diff).ravel()
            multiplier = np.prod(np.power(UNIT_SYSTEM['BASIS']['MULTIPLIER'], exps))
            return self.value / (unit.value * multiplier)
