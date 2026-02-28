import pytest

def test_sum():
    assert sum([1, 2, 3]) == 10, "Should be 6"

def test_string():
    message = "hello"
    assert message == "hello world", "Actual string not match with expected string 'hello'"

def test_string_startswith():
    text = "Python"
    assert text.startswith("Py")

def test_string_endswith():
    text = "Python"
    assert text.endswith("thon")


def test_string_lowercase():
    text = "HELLO"
    assert text.lower() == "hello"


def test_string_length():
    text = "hello"
    assert len(text) == 5


def test_sum_with_negative_numbers():
    numbers = [-1, 5, -4]
    assert sum(numbers) == 0


def test_float_basic_comparison():
    value = 3.14
    assert value > 3


def test_float_addition():
    a = 1.5
    b = 2.5
    assert a + b == 4.0

# Using pytest.approx avoids floating‑point equality issues.
def test_float_precision():
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)

# type checks
def test_value_is_float():
    value = 2.75
    assert isinstance(value, float)


def test_boolean_expression():
    a = 10
    b = 20
    assert (a < b) is True
    assert (a == b) is False


def test_boolean_logical_operations():
    assert (True and False) is False
    assert (True or False) is True
    assert (not False) is True


def test_boolean_type():
    value = True
    assert isinstance(value, bool)


def test_bool_from_expression():
    assert bool(1) is True
    assert bool(0) is False
    assert bool("") is False
    assert bool("hello") is True

# Assignments:
# Check if a substring is present in the given string
# Check two string concatenation
# Check if float multiplication gives correct result
# Check if a value is float using isinstance(
# Check if a value is exactly False
# Check if two variables refer to the same object

