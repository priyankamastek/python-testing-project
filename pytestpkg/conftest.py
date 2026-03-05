# declare fixtures in this file
import pytest

#@pytest.fixture()
@pytest.fixture(scope="class") # will be executed once for the class test cases
def setup():
    print ("I will be executed first")
    yield
    print ("I will be executed last")