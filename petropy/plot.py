"""Makes the hard plot so you don't do it."""

import matplotlib.pyplot as plt

def better_scatter(x, y, x_label='', y_label='', **kwargs):
    fig, ax = fig.subplot()
    ax.scatter(x, y, **kwargs)
    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel(y_label, fontsize=14)  
    return fig, ax