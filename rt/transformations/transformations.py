import numpy as np
from rt.tuple.rt_tuple import Tuple


class Transformation:

    def __init__(self, transform_matrix: 'np.ndarray'):
        self._transform_matrix = transform_matrix

    @property
    def transform_matrix(self):
        return self._transform_matrix

    def compose(self, other: 'Transformation') -> 'Transformation':
        self._transform_matrix = self._transform_matrix.dot(
            other.transform_matrix)
        return self

    def apply(self, obj: Tuple) -> Tuple:
        transformed_obj = self.transform_matrix.dot(obj.tuple)
        return Tuple(
            transformed_obj[0],
            transformed_obj[1],
            transformed_obj[2],
            transformed_obj[3],
        )

    def inverse(self):
        inverse = np.linalg.inv(self.transform_matrix)
        return Transformation(inverse)


def translation(x: float, y: float, z: float) -> Transformation:
    return Transformation(
        np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]))


def scaling(x: float, y: float, z: float) -> Transformation:
    return Transformation(
        np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]))
