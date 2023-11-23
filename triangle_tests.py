import unittest
import triangle

class TriangleTestCase(unittest.TestCase):


    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            res = triangle.area(-1,2)


    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(-1,2,-3)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            res = triangle.area('2',2)

    def test_float_area(self):
        res = triangle.area(1.2,1.3)
        self.assertAlmostEqual(res,0.78,delta = 0.001)

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            with self.assertRaises(ValueError):
                res = triangle.area(2,0)

    def test_int_area(self):
        res = triangle.area(4354353,768768)
        self.assertEqual(res,1673743623552)

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter("1","12","14")

    def test_float_perimeter(self):
        res = triangle.perimeter(1.2,1.1,1.3)
        self.assertAlmostEqual(res,3.6,delta = 0.01)

    def test_zero_perim(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(0,0,0)

    def test_int_perimeter(self):
        res = triangle.perimeter(453543,758346,134542)
        self.assertEqual(res,1346431)

