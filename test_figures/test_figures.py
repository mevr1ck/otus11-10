from Triangle import Triangle
import pytest


def test_get_area_triangle():
    triangle = Triangle(10, 11, 12)
    assert triangle.get_area() > 0


def test_get_area_trinagle_wrong_params():
    with pytest.raises(ValueError):
        Triangle(10, -1, '')
