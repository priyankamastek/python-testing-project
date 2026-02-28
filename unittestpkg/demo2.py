"""
To run tests from the command line:
  python -m unittest -v unittestpkg.demo1

 Another command to run all test cases from the package
  python -m unittest discover -s unittestpkg -p "demo*.py" -v

"""

import unittest

"""
Code under test
"""
def add(a, b):
    return a + b

def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def is_even(n: int) -> bool:
    return isinstance(n, int) and (n % 2 == 0)

def average(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

class TestIntegerOpeartions(unittest.TestCase):
    def test_integer_addition(self):
        a = 10
        b = 5
        self.assertEqual(add(a, b), 15)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 0), 0)

    def test_integer_subtraction(self):
        a = 20
        b = 8
        self.assertEqual(a - b, 12)
        self.assertEqual(b - a, -12)

    def test_safe_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_div(10, 0)

class TestFloatOperations(unittest.TestCase):
    def test_float_addition(self):
        a = 1.0
        b = 2.0
        self.assertEqual(add(a, b), 3.0)

    def test_float_comparisons(self):
        a = 3.0
        b = 3
        self.assertTrue(a == b)
        self.assertIsNot(a, b)  # same value, different type/identity

if __name__ == '__main__':
    unittest.main()


# Assignments
# Add class with test cases for is_even and average functions