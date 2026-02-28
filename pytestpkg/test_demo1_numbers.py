# rules to be followed for pytest
# Any pytest file starts with test_*.py or end with *_test.py
# pytest method names should start with test
# Any code should be wrapped inside a function

"""
To run all test files in the package
on terminal run: pytest -v
"""
import pytest

# python function to be tested
def calculate_sum_values(arg):
    total = 0
    for val in arg:
        total += val
    return total


def test_numbers():
    # Arrange
    a = 4
    b = 6
    # No act in this test
    # Assert
    assert a + b == 9, "Test of addition should be 9"

def test_calculate_sum():
    """
         Test that it can sum a list of integers
    """
    #Arrange
    data = [10, 20, 30]

    # Act
    result = calculate_sum_values(data)

    # Assert
    assert result == 15, "Test failed because lists do not match"


def test_sorted_vs_sort():
    # Arrange
    nums = [3, 1, 4, 1, 5, 9]
    #Act
    nums.sort(reverse=True)  # in-place
    # Assert
    assert nums == [9, 5, 4, 3, 1, 1]

