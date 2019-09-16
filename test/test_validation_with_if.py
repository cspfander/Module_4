import unittest
from input_validation import validation_with_if
import unittest.mock as mock


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert validation_with_if.average() == 90

    def test_negative_one(self):
        with mock.patch('builtins.input', side_effect=[85, 90, -1]):
            assert validation_with_if.average() == -1


if __name__ == '__main__':
    unittest.main()
