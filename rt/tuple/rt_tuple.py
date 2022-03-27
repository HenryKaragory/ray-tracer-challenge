from math import sqrt
from rt.constants import is_float_equal
import numpy as np


class Tuple:

    def __init__(self, x: float, y: float, z: float, w: int):
        self._tuple = np.array([x, y, z, w])

    @property
    def x(self) -> float:
        return self._tuple[0]

    @property
    def y(self) -> float:
        return self._tuple[1]

    @property
    def z(self):
        return self._tuple[2]

    @property
    def w(self) -> int:
        return self._tuple[3]

    @property
    def tuple(self) -> np.array:
        return self._tuple

    @property
    def position_tuple(self) -> np.array:
        return self._tuple[:3]

    def is_vector(self) -> bool:
        return self.w == 0

    def is_point(self) -> bool:
        return self.w == 1

    def negate(self) -> 'Tuple':
        return Tuple(-self.x, -self.y, -self.z, self.w)

    def __eq__(self, other: 'Tuple') -> 'Tuple':
        return is_float_equal(self.x, other.x) \
            and is_float_equal(self.y, other.y) \
            and is_float_equal(self.z, other.z) \
            and self.w == other.w

    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> 'Tuple':
        return self / self.magnitude()

    def __add__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w,
        )

    def __sub__(self, other: 'Tuple') -> 'Tuple':
        return Tuple(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w,
        )

    def __mul__(self, value: 'float') -> 'Tuple':
        return Tuple(self.x * value, self.y * value, self.z * value, self.w)

    def __truediv__(self, value: float) -> 'Tuple':
        return Tuple(self.x / value, self.y / value, self.z / value, self.w)


def make_point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1)


def make_vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0)


def dot(left: Tuple, other: Tuple) -> float:
    if left.is_point() or other.is_point():
        raise Exception("Attempting to take the dot product of a point.")
    return left.x * other.x + left.y * other.y + left.z * other.z


def cross(left: Tuple, right: Tuple) -> Tuple:
    if left.is_point() or right.is_point():
        raise Exception("Attempting to take the dot product of a point.")

    np_cross_array = np.cross(left.position_tuple, right.position_tuple)
    return make_vector(np_cross_array[0], np_cross_array[1], np_cross_array[2])
