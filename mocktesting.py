from demo import rm

import mock
import unittest


class RmTestCase(unittest.TestCase):
    @mock.patch('demo.os')
    def test_rm(self,os):
        rm("sample2.txt")
        # test that rm called os.remove with the right parameters
        os.remove.assert_called_with("sample2.txt")