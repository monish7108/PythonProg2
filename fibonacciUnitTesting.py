import unittest
from fibonacciNumChecking import *


class MyTestCase(unittest.TestCase):

    def test_isNot_PerfectSquare(self):
        self.assertFalse(isPerfectSquare(12))

    def test_is_PerfectSquare(self):
        self.assertTrue(isPerfectSquare(49))

    def test_is_member_of_fibonacciSeries(self):
        self.assertTrue(fibonacciSeries(5))

    def test_isNot_member_of_fibonacciSeries(self):
        self.assertFalse(fibonacciSeries(12))

    def test_for_ValueError(self):
        self.assertRaises(ValueError,fibonacciSeries('a'))

if __name__ == '__main__':
    unittest.main()
