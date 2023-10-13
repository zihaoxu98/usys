import numpy as np

from .utils import hot_array
from .constant import *

DIMENSION_INDEX = {
    'TIME': 0,
    'LENGTH': 1,
    'MASS': 2,
    'CURRENT': 3,
    'TEMPERATURE': 4,
    'MOLE': 5,
    'LUMINOSITY': 6,
}

DIMENSION = {dim: hot_array(len(DIMENSION_INDEX), DIMENSION_INDEX[dim]) for dim in DIMENSION_INDEX}

UNIT_SYSTEM = {
    'NULL': {
        'DIMENSION': [],
        'MULTIPLIER': [],
    },
    'BASIS': {
        'DIMENSION': list(DIMENSION.values()),
        'MULTIPLIER': np.ones(len(DIMENSION)),
    },
}

def use_unit_system(use):
    if use.lower() == 'si':
        UNIT_SYSTEM['NULL']['DIMENSION'] = []
        UNIT_SYSTEM['NULL']['MULTIPLIER'] = []
        UNIT_SYSTEM['BASIS']['DIMENSION'] = list(DIMENSION.values())
        UNIT_SYSTEM['BASIS']['MULTIPLIER'] = np.ones(len(DIMENSION))
    elif use.lower() == 'natural':
        UNIT_SYSTEM['NULL']['DIMENSION'] =[c.dim, hbar.dim]
        UNIT_SYSTEM['NULL']['MULTIPLIER'] = [c.value, hbar.value]
        UNIT_SYSTEM['BASIS']['DIMENSION'] = UNIT_SYSTEM['NULL']['DIMENSION']
        UNIT_SYSTEM['BASIS']['DIMENSION'].extend([
            DIMENSION['MASS'],
            DIMENSION['CURRENT'],
            DIMENSION['TEMPERATURE'],
            DIMENSION['MOLE'],
            DIMENSION['LUMINOSITY'],
        ])
        UNIT_SYSTEM['BASIS']['MULTIPLIER'] = UNIT_SYSTEM['NULL']['DIMENSION']
        UNIT_SYSTEM['BASIS']['MULTIPLIER'].extend([
            kg.value,
            A.value,
            K.value,
            mol.value,
            Cd.value,
        ])
