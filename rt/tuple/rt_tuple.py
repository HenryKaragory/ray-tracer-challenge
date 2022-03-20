from math import sqrt
from rt.constants import is_float_equal


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: int):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    def is_vector(self) -> bool:
        return self._w == 0

    def is_point(self) -> bool:
        return self._w == 1

    def negate(self) -> 'Tuple':
        return Tuple(
            -self._x,
            -self._y,
            -self._z,
            self._w
        )

    def __eq__(self, other: 'Tuple') -> 'Tuple':
        return is_float_equal(self._x, other._x) \
            and is_float_equal(self._y, other._y) \
            and is_float_equal(self._z, other._z) \
            and self._w == other._w

    def magnitude(self) -> float:
        return sqrt(
            self._x ** 2 + self._y ** 2 + self._z ** 2
        )

    def normalize(self) -> 'Tuple':
        return self / self.magnitude()

    def __add__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self._x + other._x,
            self._y + other._y,
            self._z + other._z,
            self._w + other._w,
        )

    def __sub__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self._x - other._x,
            self._y - other._y,
            self._z - other._z,
            self._w - other._w,
        )

    def __mul__(self, value: 'float') -> 'Tuple':
        return Tuple(
            self._x * value,
            self._y * value,
            self._z * value,
            self._w
        )

    def __truediv__(self, value: float) -> 'Tuple':
        return Tuple(
            self._x / value,
            self._y / value,
            self._z / value,
            self._w
        )


def make_point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1)


def make_vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0)


def dot(left: Tuple, other: Tuple) -> Tuple:
    if left.is_point() or other.is_point():
        raise Exception("Attempting to take the dot product of a point.")
    return left._x * other._x + left._y * other._y + left._z * other._z


def cross(left: Tuple, right: Tuple) -> Tuple:
    if left.is_point() or right.is_point():
        raise Exception("Attempting to take the dot product of a point.")

    return make_vector(
        left._y * right._z - left._z * right._y,
        left._z * right._x - left._x * right._z,
        left._x * right._y - left._y * right._x
    )
