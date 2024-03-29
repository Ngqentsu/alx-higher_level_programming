#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Declare class TestMaxInteger for def max_integer function"""

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        result = max_integer(empty)
        self.assertIsNone(result)

    def test_one_element_list(self):
        """Test a list with a single element."""
        number = [2]
        result = max_integer(number)
        self.assertEqual(result, 2)

    def test_duplicate_numbers(self):
        """Test a list with duplicate numbers."""
        numbers = [7, 5, 7, 2, 0, 2]
        result = max_integer(numbers)
        self.assertEqual(result, 7)

    def test_floats(self):
        """Test a list of floats."""
        numbers = [1.1, 1.2, 1.3, 1.4, 1.5]
        result = max_integer(numbers)
        self.assertEqual(result, 1.5)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        numbers = [2, 1.5, -9, 3, 6]
        result = max_integer(numbers)
        self.assertEqual(result, 6)

    def test_positive_numbers(self):
        """Test a list of positive numbers."""
        numbers = [2, 4, 6, 8, 10]
        result = max_integer(numbers)
        self.assertEqual(result, 10)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        numbers = [-2, -4, -6, -8, -10]
        result = max_integer(numbers)
        self.assertEqual(result, -2)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        numbers = [1, 2, 3, 4, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        numbers = [3, 1, 5, 4, 2]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_max_at_begginning(self):
        """Test a list with max value first value."""
        numbers = [5, 4, 3, 2, 1]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_mixed_values(self):
        """Test a list with mixed integer and string values."""
        chars = [1, 5, 'navy', 'blue', 2]
        with self.assertRaises(TypeError):
            max_integer(chars)

    def test_string_values(self):
        """Test a list with string values."""
        values = ['apple', 'banana', 'orange', 'pear']
        result = max_integer(values)
        self.assertEqual(result, 'pear')

    def test_empty_string(self):
        """Test an empty string."""
        empty = ""
        result = max_integer(empty)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
