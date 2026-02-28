"""
To run tests from the command line:
 python -m unittest -v unittestpkg.demo1
"""
import unittest

# Every class will act as a test cases
class MyTestCase(unittest.TestCase):
    def test_something(self):
        # assertEqual(Expected Result, Actual Result)
        self.assertEqual(True, True)  # add assertion here

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")



if __name__ == '__main__':
    unittest.main()
