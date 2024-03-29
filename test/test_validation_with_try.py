import unittest
from input_validation import validation_with_try
import unittest.mock as mock


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(validation_with_try.average(85, 90, 95), 90)

    def test_average_exception_one(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

    def test_average_exception_two(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)

    def test_average_exception_three(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
