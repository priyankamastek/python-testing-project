# if you want to run setup or teardown methods
# mark mwthod with @pytest.fixture()
# To run - py.test -v -s pytestpkg/test_pytest_fixtures.py
# use conftest.py file to generalize fixtures for other test cases
# You need to make fixture available in the testcase method test_<method>(setup)
# Convert test cases into a class, if you want to pass setup fixture to all methods

import pytest


# @pytest.fixture()
# def setup():
#     print ("I will be executed first")
#     yield
#     print ("I will be executed last")

def test_fixture_methods(setup):
    print ("I will be execute steps in fixture methods")

@pytest.fixture()
def teardown():
    pass

