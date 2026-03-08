# module level fixtures

import pytest

# By default any fuxtures in the py file along with test cases are called Module Level Fixtures
# Module level fixtures are called onluy once all testcases
def setup_module(module):
    print("Creating database connection")

def teardown_module(module):
    print("Tearing down database connection")

# Function level fixtures are called before and after every function
def setup_function(function):
    print("Setting up fixture")

def teardown_function(function):
    print("Tearing down fixture")


def test_db():
    assert True

