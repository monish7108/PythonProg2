import unittest
from RegularExpression import *

class MyTestCase(unittest.TestCase):

    def test_isvalid_ip(self):
        self.assertTrue(isvalidIP("101.101.230.230"))
    def test_isvalid_email(self):
        self.assertTrue(isvalidEmail("asfab@angsekng.sjdj"))
    def test_isvalid_phonenumber(self):
        self.assertTrue(isvalidPhoneNum("080-234-123"))
    def test_contains_onlyNumbers(self):
        self.assertTrue(containsOnlyNumbers("47826478"))
    def test_contains_onlyChar(self):
        self.assertTrue(containsOnlyCharacters("iehfwen sufhvsui sdvshdvui werufbwue"))
    def test_cotains_specialChar(self):
        self.assertTrue(containsSpecifiedSpecialCharacters("-()()()"))
if __name__ == '__main__':
    unittest.main()
