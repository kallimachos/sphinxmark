#!/bin/python3
# coding: utf-8
"""Example test file."""

import source


def test_square():
    """Test square."""
    assert source.square(1) == 1
    assert source.square(2) == 4
    assert source.square(3) == 9
    assert source.square(4) == 16
    assert source.square(5) == 25


if __name__ == '__main__':
    pass
