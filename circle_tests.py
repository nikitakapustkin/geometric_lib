import unittest
import circle


class CircleTestCase(unittest.TestCase):

    def test_negative_value_perimeter(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(-1)
    def test_negative_value_area(self):
        with self.assertRaises(ValueError):
            res = circle.area(-1)
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = circle.area(0)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            res = circle.area("15")

    def test_float_area(self):
        res = circle.area(1.2)
        self.assertAlmostEqual(res, 4.523, delta=0.0001)

    def test_int_area(self):
        res = circle.area(4543543)
        self.assertAlmostEqual(res, 64854356992636.336, delta=0.0001)

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter(0)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            res = circle.area(0)

    def test_float_perimeter(self):
        res = circle.perimeter(3.4)
        self.assertAlmostEqual(res, 21.362830044410593, delta=0.0000000000000001)

    def test_int_perimeter(self):
        res = circle.perimeter(325235)
        self.assertAlmostEqual(res, 2043511.7733805527, delta=0.00000000001)
