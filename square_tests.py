import unittest
import square


class SquareTestCase(unittest.TestCase):

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(-1)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            res = square.area(-1)
    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            res = square.perimeter("12")

    def test_float_perimeter(self):
        res = square.perimeter(4.2)
        self.assertEqual(res,16.8)

    def test_int_perimeter(self):
        res = square.perimeter(43534)
        self.assertEqual(res,174136)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            res = square.area("12")

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = square.area(0)

    def test_float_area(self):
        res = square.area(1.2)
        self.assertAlmostEqual(res,1.44,delta=0.001)

    def test_int_area(self):
        res=square.area(32352)
        self.assertEqual(res,1046651904)

