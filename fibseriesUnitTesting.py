import unittest
from fibonacciSeries import fibonacciSeries

class MyTestCase(unittest.TestCase):

    def test_fibSeries_succes(self):
        self.assertListEqual(fibonacciSeries(5),[0,1,1,2,3])

    def test_fibSeries_fail(self):
        self.assertNotEqual(fibonacciSeries(10),[0,1,1,2,3])

if __name__ == '__main__':
    unittest.main()
