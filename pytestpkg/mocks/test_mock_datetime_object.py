from unittest.mock import Mock
import datetime as real # add name to datetime to resolve conflict with datetime object in mycode.py
import pytestpkg.mocks.mycode as mycode # import the whole module



# Save a couple of test days
today_object1 = real.datetime(year=2025, month=1, day=1)
today_object2 = real.datetime(year=2025, month=1, day=5)


"""
This function is test on the actual is_weekly() method and will fail if executed on weekends
Hence, to test the method we need to mock the datetime object
"""
"""def test_is_weekday():
    # Test if today is a weekday
    assert is_weekday()
"""

# In this case, you can mock datetime and set the .return_value for .today() to a day that you choose
def test_is_weekday_mock():
    # Mock datetime to control today's date
    # Mock .today() to return Wednesday - mocked the behavior of today method
    mycode.datetime = Mock()
    mycode.datetime.today.return_value = today_object1
    # Test Wednesday is a weekday
    print(mycode.is_weekday()) # calls actual method from mycode
    assert mycode.is_weekday()

def test_is_not_weekday_mock():
   # Mock .today() to return Sunday
    mycode.datetime = Mock()
    mycode.datetime.today.return_value = today_object2
    print(mycode.is_weekday())
    # Test Sunday is not a weekday
    assert not mycode.is_weekday()
