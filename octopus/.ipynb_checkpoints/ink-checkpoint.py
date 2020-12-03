from figures import *
from quotes import *

import numpy as np


def octopi():
    """prints 8 digits of pi"""
    return float(str(np.pi)[:9])


def octopus():
    """prints a friend"""
    print(baby_octopus)
    pass 


def octoquote():
    """prints a small gift"""
    print(np.random.choice(all_quotes))
    pass