import pytest

# works like @BeforeALL
@pytest.mark.usefixtures("setup")
class TestClass:
    def test_fixture_method1(self):
        print ("I will be executed steps in fixture methods 1")

    def test_fixture_method2(self):
        print ("I will be executed steps in fixture methods 2")