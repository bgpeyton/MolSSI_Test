"""
Testing for the math.py module.
"""
import MolSSI_Test as mst
import pytest
# pytest will catch any function starting with "test_"


def test_add():
    assert mst.add(5, 2) == 7
    assert mst.add(2, 5) == 7


def test_mult():
    assert mst.mult(9, 2) == 18
    assert mst.mult(4, 12) == 48
