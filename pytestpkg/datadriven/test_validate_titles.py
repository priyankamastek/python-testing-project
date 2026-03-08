import pytest

def test_validate_titles():

    expected_title = "Google.com"
    actual_title = "Gmail.com"

    # if actual_title == expected_title:
    #     print("Test case passed")
    # else:
    #     print("Test case failed")

    assert actual_title == expected_title