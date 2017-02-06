import unittest
from primeNumber import *

class MyTestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(8))

    def test_nextprime(self):
        self.assertEqual(next_prime(7),11)

if __name__ == '__main__':
    unittest.main()
