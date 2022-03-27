import unittest
from rt.transformations.transformations import translation, scaling
from rt.tuple.rt_tuple import make_point, make_vector


class TestCanvas(unittest.TestCase):

    def setUp(self):
        self.scaling = scaling(2, 3, 4)
        self.translation = translation(5, -3, 2)
        self.point = make_point(-3, 4, 5)
        self.vector = make_vector(1, 2, 3)

    def test_translation(self):
        transformed_point = self.translation.apply(self.point)
        expected_point = make_point(2, 1, 7)
        self.assertTrue(transformed_point == expected_point)

    def test_inverse_translation(self):
        inverse_transform = self.translation.inverse()
        transformed_point = inverse_transform.apply(self.point)
        expected_point = make_point(-8, 7, 3)
        self.assertTrue(transformed_point == expected_point)

    def test_translation_no_affect_on_vectors(self):
        transformed_vector = self.translation.apply(self.vector)
        self.assertTrue(self.vector == transformed_vector)

    def test_scaling(self):
        transformed_point = self.scaling.apply(self.point)
        transformed_vector = self.scaling.apply(self.vector)

        expected_point = make_point(-6, 12, 20)
        expected_vector = make_vector(2, 6, 12)

        self.assertTrue(expected_point == transformed_point)
        self.assertTrue(expected_vector == transformed_vector)

    def test_inverse_scaling(self):
        inverse_scaling = self.scaling.inverse()
        transformed_vector = inverse_scaling.apply(self.vector)

        expected_vector = make_vector(0.5, 0.6666, 0.75)

        self.assertTrue(expected_vector == transformed_vector)