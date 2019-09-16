import unittest
from store import nested_if_statement


class MyTestCase(unittest.TestCase):
    def test_price_under_10_5_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 5, .10), 9.76)

    def test_price_under_10_5_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 5, .15), 9.54)

    def test_price_under_10_5_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 5, .20), 9.33)

    def test_price_under_10_10_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 10, .10), 5.95)

    def test_price_under_10_10_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 10, .15), 5.95)

    def test_price_under_10_10_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(8.99, 10, .20), 5.95)

    def test_price_10_to_under_30_5_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 5, .10), 22.26)

    def test_price_10_to_under_30_5_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 5, .15), 21.46)

    def test_price_10_to_under_30_5_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 5, .20), 20.67)

    def test_price_10_to_under_30_10_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 10, .10), 17.49)

    def test_price_10_to_under_30_10_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 10, .15), 16.96)

    def test_price_10_to_under_30_10_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(20, 10, .20), 16.43)

    def test_price_30_to_under_50_5_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 5, .10), 45.34)

    def test_price_30_to_under_50_5_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 5, .15), 43.48)

    def test_price_30_to_under_50_5_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 5, .20), 41.63)

    def test_price_30_to_under_50_10_off_10_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 10, .10), 40.57)

    def test_price_30_to_under_50_10_off_15_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 10, .15), 38.98)

    def test_price_30_to_under_30_50_off_20_percent(self):
        self.assertEqual(nested_if_statement.calculate_order(40, 10, .20), 37.39)


if __name__ == '__main__':
    unittest.main()
