""""This is a module testing code."""

import pytest

from petropy.calcs import acoustic_impedance, classifier

from numpy.testing import assert_almost_equal, assert_array_almost_equal

import numpy as np

def test_acoustic_impedance_valid_scalars():
    """
    Test with valid scalars numbers.
    Remember the test file should start with test_   or ends with _test
    Also, remember you must put # Setup  # Exercise and # Verify
    """

    # Setup
    vp = 2200
    rho = 2400
    truth = 5280000

    # Excersice
    result = acoustic_impedance(rho, vp)

    # Verify
    assert truth == result


def test_floating_substraction():

    # Setup
    truth = 0.293

    # Excercise
    result = 1 - 0.707

    # Verify
    assert_almost_equal(truth, result)


def test_floating_substraction_array():

    # Setup
    truth = np.array([0.293, 0.401])

    # Excercise
    result = np.array([1 - 0.707, 1 - 0.599])

    # Verify
    assert_almost_equal(truth, result)
     
# We can skip testing a test by using the following decorator
@pytest.mark.skip(reason='For time being I want to skip this test.')
def test_classifier_granite():
    # Setup
    density_in = 2751
    truth = 'granite'

    # Excersice
    result = classifier(density_in)

    # Verify
    assert truth == result

def test_classifier_sandstone():
    # Setup
    density_in = 2401
    truth = 'sandstone'

    # Excersice
    result = classifier(density_in)

    # Verify
    assert truth == result 

def test_classifier_not_a_rock():
    # Setup
    density_in = 2399
    truth = 'not a rock'

    # Excersice
    result = classifier(density_in)

    # Verify
    assert truth == result 

@pytest.mark.parametrize('density, expected',
                        [(2751, 'granite'), 
                        (2500, 'sandstone'), 
                        (2000, 'not a rock')])
def test_classifier(density, expected):
    """Verify that we properly classify rocks."""

    # Setup

    # Excercise
    result = classifier(density)

    # Verify
    assert result == expected

def test_classifier_ValueError():
    """Verify that we properly classify rocks."""
    # Setup
    density = 0

    # Excercise/verify
    with pytest.raises(ValueError):
        classifier(density)