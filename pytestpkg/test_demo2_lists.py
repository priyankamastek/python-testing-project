import pytest

# python function for testing
def is_list_of_any(obj, elem_types: tuple[type, ...]):
    if not isinstance(obj, list):
        return False
    return all(isinstance(x, elem_types) for x in obj)


def is_list_of(obj, elem_type):
    if not isinstance(obj, list):
        return False
    return all(isinstance(x, elem_type) for x in obj)

"""
  Test cases 
  Each function represents a test case with its own structure.
  #Arrange - Set of inputs for the test 
  #Act - execute the code
  #Assert - compare actual result with expected result
"""

def test_compare_two_list_equality():
    # Arrange
    a = [1, 2, 3]
    b = [1, 2, 3]

    # No Act

    # Assert
    assert a == b, "Test failed because lists do not match"


def test_list_methods_append_extend_insert_pop_remove():
    data = [1, 2]

    data.append(3)
    assert data == [1, 2, 3]

    data.extend([4, 5])
    assert data == [1, 2, 3, 4, 5]

    data.insert(0, 0)
    assert data == [0, 1, 2, 3, 4, 5]

    removed = data.pop()  # removes last
    assert removed == 5 and data == [0, 1, 2, 3, 4]

    data.remove(2)  # removes first occurrence of 2
    assert data == [0, 1, 3, 4]

    with pytest.raises(ValueError):
        data.remove(999)  # not present


def test_is_list_of_int_or_float():
    assert is_list_of_any([1, 2.0, 3], (int, float)) is True
    assert is_list_of_any([1, "2"], (int, float)) is False
    assert is_list_of_any([], (str, int)) is True  # empty list always passes



def test_type_check_for_list():
    assert is_list_of([1, 2, 3], int)
    assert not is_list_of([1, "2", 3], int)
    assert is_list_of([], int)  # empty list passes


"""
 @pytest.mark.parametrize("input_value, expected_output", [...])
 
Generic parametrized test template.

    This test uses pytest's parametrization mechanism to run the same test
    logic against multiple input–output combinations. Each tuple in the
    parameter set represents one test case, allowing the test function to be
    exercised with varied conditions without duplicating code.
    
 ----------
    input_value : Any
        The input data for the current test iteration.

    expected_output : Any
        The expected result corresponding to the given input. Each test case
        asserts that the function or expression under test behaves as expected
        for that specific scenario.
"""
@pytest.mark.parametrize(
    "value, expected",
    [
        ([1, 2, 3], True),
        ([], True),
        ((1, 2, 3), False),
        ("abc", False),
        (None, False),
    ],
)
def test_is_list_param(value, expected):
    assert isinstance(value, list) is expected


# Assignments
# Check that two separate lists are NOT the same object
# Check if an element is NOT present in a list
# Check the length of a list
# Check append() adds an element at the end
# Check pop() removes the last element
# Check if all elements in a list are integers
