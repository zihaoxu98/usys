import numpy as np
from copy import deepcopy

from usys.utils import hot_array
from usys.dim import UNIT_SYSTEM
from usys.constant import *

def use_unit_system(use):
    if use.lower() == 'si':
        UNIT_SYSTEM['NULL']['DIMENSION'] = []
        UNIT_SYSTEM['NULL']['MULTIPLIER'] = []
        UNIT_SYSTEM['BASIS']['DIMENSION'] = list(DIMENSION.values())
        UNIT_SYSTEM['BASIS']['MULTIPLIER'] = np.ones(len(DIMENSION))
    elif use.lower() == 'natural':
        UNIT_SYSTEM['NULL']['DIMENSION'] =[c.dim, hbar.dim]
        UNIT_SYSTEM['NULL']['MULTIPLIER'] = [c.value, hbar.value]
        UNIT_SYSTEM['BASIS']['DIMENSION'] = deepcopy(UNIT_SYSTEM['NULL']['DIMENSION'])
        UNIT_SYSTEM['BASIS']['DIMENSION'].extend([
            DIMENSION['MASS'],
            DIMENSION['CURRENT'],
            DIMENSION['TEMPERATURE'],
            DIMENSION['MOLE'],
            DIMENSION['LUMINOSITY'],
        ])
        UNIT_SYSTEM['BASIS']['MULTIPLIER'] = deepcopy(UNIT_SYSTEM['NULL']['MULTIPLIER'])
        UNIT_SYSTEM['BASIS']['MULTIPLIER'].extend([
            kg.value,
            A.value,
            K.value,
            mol.value,
            Cd.value,
        ])
