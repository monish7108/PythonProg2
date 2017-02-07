import unittest
from listingthepath import *

class MyTestCase(unittest.TestCase):

    def test_main_OSError(self):
        self.assertRaises(OSError,main("/home/monish/WEEK-6[MONISH]/FinalSubmission/fileCharacterReversing.py"))



if __name__ == '__main__':
    unittest.main()
