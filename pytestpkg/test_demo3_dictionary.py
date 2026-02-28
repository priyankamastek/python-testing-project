import pytest
# Check if all keys exists in dictionary
def test_dict_has_required_keys():
    data = {"name": "Alice", "age": 30, "city": "Mumbai"}

    required_keys = {"name", "age"}

    # Check that all required keys exist in the dictionary
    assert required_keys.issubset(data.keys())

# Parameterized test
@pytest.mark.parametrize(
    "data, expected",
    [
        ({"name": "Alice", "age": 30}, True),
        ({"name": "Bob"}, False),
        ({}, False),
    ],
)
def test_dict_contains_keys(data, expected):
    required_keys = {"name", "age"}
    result = required_keys.issubset(data.keys())
    assert result is expected



# Assert basic dictionary operations
def test_dict_basic_ops():
    sample_dict = {"name": "Alice", "age": 30}

    # Act + Assert together
    assert sample_dict["name"] == "Alice"

    # Graceful default read
    assert sample_dict.get("city") is None
    assert sample_dict.get("city", "Mumbai") == "Mumbai"

    # Insert/Update
    sample_dict["city"] = "Mumbai"
    sample_dict["age"] += 1
    assert sample_dict["city"] == "Mumbai"
    assert sample_dict["age"] == 31


def test_dict_iteration_orders_insertion():
    d = {}
    d["a"] = 1
    d["b"] = 2
    d["c"] = 3
    assert list(d.keys()) == ["a", "b", "c"]
    assert list(d.values()) == [1, 2, 3]
    assert list(d.items()) == [("a", 1), ("b", 2), ("c", 3)]



def test_dict_popitem_lifo_behavior():
    d = {"a": 1, "b": 2, "c": 3}
    # popitem removes the last inserted item (LIFO)
    k, v = d.popitem()
    assert (k, v) == ("c", 3)
    k, v = d.popitem()
    assert (k, v) == ("b", 2)
    k, v = d.popitem()
    assert (k, v) == ("a", 1)
    assert d == {}

