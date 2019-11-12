"""This is our module docsting. It does awesome calculations."""

import numpy as np

def acoustic_impedance(rho, vp):
    return rho*vp

def classifier(density_in):
    if density_in >= 2750:
        return 'granite'
    elif density_in >= 2400:
        return 'sandstone'
    elif density_in > 0:
        return 'not a rock'
    else:
        raise ValueError('Density cannot be zero or negative.')

