import utils
import unittest

class TestUtilsFunctions(unittest.TestCase):
    def setUp(self):
        self.utils = utils.Utils

    def test_reversed_string(self):
        self.assertRaises(TypeError, self.utils.reversed, '123')

    def test_reversed_float(self):
        self.assertRaises(TypeError, self.utils.reversed, 12.3)

    def test_reversed_int(self):
        self.assertEqual(self.utils.reversed(123), 321)

    def test_formatter_string(self):
        self.assertRaises(TypeError, self.utils.formatter, '123')

    def test_formatter_float(self):
        self.assertRaises(TypeError, self.utils.formatter, 12.3)

    def test_formatter_int(self):
        self.assertEqual(self.utils.formatter(123), ('0b1111011', '0o173'))


if __name__ == '__main__':
    unittest.main()