import math
import unittest
import rt.tuple.rt_tuple as Tuple
from rt.constants import is_float_equal


class TestTuple(unittest.TestCase):

    def test_is_point(self):
        t = Tuple.Tuple(1, 2, 3, 0)
        self.assertTrue(t.is_vector())
        self.assertFalse(t.is_point())

    def test_is_vector(self):
        t = Tuple.Tuple(1, 2, 3, 1)
        self.assertTrue(t.is_point())
        self.assertFalse(t.is_vector())

    def test_add_tuples(self):
        t1 = Tuple.Tuple(1, 2, 3, 1)
        t2 = Tuple.Tuple(4, 5, 6, 0)
        t3 = t1 + t2

        self.assertEqual(t3.x, 5)
        self.assertEqual(t3.y, 7)
        self.assertEqual(t3.z, 9)

    def test_make_point_is_point(self):
        p = Tuple.make_point(1, 2, 3)
        self.assertTrue(p.is_point())
        self.assertFalse(p.is_vector())

    def test_make_vector_is_vector(self):
        p = Tuple.make_vector(1, 2, 3)
        self.assertTrue(p.is_vector())
        self.assertFalse(p.is_point())

    def test_subtract_vector_from_point(self):
        t1 = Tuple.Tuple(1, 2, 3, 1)
        t2 = Tuple.Tuple(4, 5, 7, 0)
        t3 = t1 - t2

        self.assertEqual(t3.x, -3)
        self.assertEqual(t3.y, -3)
        self.assertEqual(t3.z, -4)
        self.assertEqual(t3.w, 1)
        self.assertTrue(t3.is_point())

    def test_subtract_two_vectors(self):
        t1 = Tuple.make_vector(1, 2, 3)
        t2 = Tuple.make_vector(4, 6, 8)

        t3 = t2 - t1

        self.assertTrue(t3.is_vector())
        self.assertFalse(t3.is_point())

        self.assertEqual(t3.x, 3)
        self.assertEqual(t3.y, 4)
        self.assertEqual(t3.z, 5)

    def test_negate_vector(self):
        v = Tuple.make_vector(1, 2, 3)
        v_negated = v.negate()

        self.assertEqual(v.x, -v_negated.x)
        self.assertEqual(v.y, -v_negated.y)
        self.assertEqual(v.z, -v_negated.z)

    def test_magnitude(self):
        v = Tuple.make_vector(1, 2, 3)

        self.assertTrue(is_float_equal(v.magnitude(), math.sqrt(14)))

    def test_multiply_vector(self):
        v = Tuple.make_vector(1, 2, 3)
        new_v = v * 0.5

        expected_new_v = Tuple.make_vector(0.5, 1.0, 1.5)

        self.assertTrue(new_v.is_vector())
        self.assertTrue(expected_new_v == new_v)

    def test_divide_vector(self):
        v = Tuple.make_vector(1, 2, 3)
        new_v = v / 0.5

        expected_new_v = Tuple.make_vector(2.0, 4.0, 6.0)

        self.assertTrue(new_v.is_vector())
        self.assertTrue(expected_new_v == new_v)

    def test_normalize(self):
        v = Tuple.make_vector(1, 2, 3)
        v_normalized = v.normalize()

        self.assertTrue(is_float_equal(v_normalized.magnitude(), 1.0))
        self.assertTrue(is_float_equal(v_normalized.x, 1.0 / math.sqrt(14)))
        self.assertTrue(is_float_equal(v_normalized.y, 2.0 / math.sqrt(14)))
        self.assertTrue(is_float_equal(v_normalized.z, 3.0 / math.sqrt(14)))

    def test_dot_product(self):
        left = Tuple.make_vector(1, 2, 3)
        right = Tuple.make_vector(2, 3, 4)

        expected_dot_product = 20.0
        actual_dot_product = Tuple.dot(left, right)

        self.assertTrue(
            is_float_equal(actual_dot_product, expected_dot_product))

    def test_cross_product_1(self):
        left = Tuple.make_vector(1, 2, 3)
        right = Tuple.make_vector(2, 3, 4)

        expected_cross_product = Tuple.make_vector(-1, 2, -1)
        actual_cross_product = Tuple.cross(left, right)

        self.assertTrue(expected_cross_product == actual_cross_product)

    def test_cross_product_2(self):
        left = Tuple.make_vector(2, 3, 4)
        right = Tuple.make_vector(1, 2, 3)

        expected_cross_product = Tuple.make_vector(1, -2, 1)
        actual_cross_product = Tuple.cross(left, right)

        self.assertTrue(expected_cross_product == actual_cross_product)
