import pytest
import sys

sys.path.insert(1, "../src")

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


triangle_a = 3
triangle_b = 4
triangle_c = 5

rectangle_a = 10
rectangle_b = 5

square_a = 5

circle_radius = 5


def test_get_area_triangle():
    triangle = Triangle(triangle_a, triangle_b, triangle_c)
    polu_perimetr = (triangle_a + triangle_b + triangle_c) / 2
    assert triangle.get_area() == (polu_perimetr * (polu_perimetr - triangle_a) * (polu_perimetr - triangle_b) * (
            polu_perimetr - triangle_c)) ** 0.5


def tests_get_perimetr_triangle():
    triangle = Triangle(triangle_a, triangle_b, triangle_c)
    assert triangle.perimetr == triangle_a + triangle_b + triangle_c


def test_get_area_triangle_wrong_params():
    with pytest.raises(ValueError):
        Triangle(10, -1, '')


def test_get_area_rectangle():
    rectangle = Rectangle(rectangle_a, rectangle_b)
    assert rectangle.get_area() == rectangle_a * rectangle_b


def test_get_perimetr_rectangle():
    rectangle = Rectangle(rectangle_a, rectangle_b)
    assert rectangle.perimetr == rectangle_a * 2 + rectangle_b * 2


def test_create_rectangle_wrong_params():
    with pytest.raises(ValueError):
        Rectangle('', -1)


def test_get_area_square():
    square = Square(square_a)
    assert square.get_area() == square_a ** 2


def test_get_perimetr_square():
    square = Square(square_a)
    assert square.perimetr == square_a * 4


@pytest.mark.parametrize('side', ['', -1, None])
def test_create_square_wrong_params(side):
    with pytest.raises(ValueError):
        Square(side)


def test_get_area_circle():
    circle = Circle(circle_radius)
    assert circle.get_area() == 3.14 * circle.radius ** 2


def test_get_circle_length():
    circle = Circle(circle_radius)
    assert circle.length == 2 * 3.14 * circle.radius


@pytest.mark.parametrize('radius', ['', -1, None])
def test_create_circle_wrong_params(radius):
    with pytest.raises(ValueError):
        Circle(radius)
