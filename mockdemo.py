import demoTEST

import unittest
import mock

class MyTest(unittest.TestCase):
    def test_instantiation(self):
        m=mock.Mock()
        demoTEST.MyObj(m)
        print(m.connect.assert_called_with("hello"))

    def test_setup(self):
        external_obj = mock.Mock()
        obj = demoTEST.MyObj(external_obj)
        obj.setup()
        external_obj.setup.assert_called_with(cache=True, max_connections=256)


if __name__ == '__main__':
    unittest.main()
