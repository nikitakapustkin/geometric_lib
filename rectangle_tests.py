import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    def test_str_perimeter(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter(5,'5')

    def test_float_perimeter(self):
        res = rectangle.perimeter(1.2,3.7)
        self.assertAlmostEqual(res,9.8,delta=0.1)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_equal_sides_perimeter(self):
        res = rectangle.perimeter(10,10)
        self.assertEqual(res,40)

    def test_int_perimeter(self):
        res = rectangle.perimeter(314214,214124)
        self.assertEqual(res,1056676)

    def test_str_area(self):
        with self.assertRaises(TypeError):
            res = rectangle.area("10", "10")

    def test_float_area(self):
        res = rectangle.area(1.2,1.3)
        self.assertEqual(res,1.56)

    def test_zero_area(self):
        res = rectangle.area(3,0)
        self.assertEqual(res,0)

    def test_equal_sides_area(self):
        res = rectangle.area(2,2)
        self.assertEqual(res,4)

    def test_int_area(self):
        res = rectangle.area(32532,9879)
        self.assertEqual(res,321383628)