Notepad pointers:
Automation Testing
 
Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human.
 
Python already comes with a set of tools and libraries to help you create automated tests for your application.
 
Two type of testing
 
functional testing - Black-box , white-box
Black box - actual functionality of the code
white box -testing logic, code, structures to verify the behavior of the components (small unit - function..)
 
unit test can test - specific path, logic, branches (Control statements). Ensures maximum coverage identification, dead code.
 
test coverage plugin -> generate in form of HTML/ XML
 
If unit tests has depends (Working with file, database) -> mocking the dependencies.
A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
 
Integration Testing - testing multiple components
An integration test checks that components in your application operate with each other.
 
Each test should focus on a single piece of code and is not depend on the state of other tests.
Name your test functions clearly to indicate what your are testing
 
To test your APIs or Database, mock the dependencies using unitest-mock module
Integrate test with CI/CD pipeline to catch bugs early.
 
Frameworks:
- Unittest module - class based
 
- Pytest - function based
 
pip install pytest
 
testing steps (test case)
 
# Arrange - Setup inputs
 
# Act - Execute the actual code only for test environment
 
# Assert - Compare the actual result with the expected result
 
Open Python RPEL
==========================
assert sum([1, 2, 3]) == 6, "Should be 6"
 
If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6
 
assert sum([1, 1, 1]) == 6, "Should be 6"
In the REPL, you are seeing the raised AssertionError because the result of sum() does not match 6.
 
Run Tests With unittest
======================================
unittest has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.
 
unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.
 
unittest requires that:
 
1. You put your tests into classes as met1. hods
2. You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
 
To write the unittest code
==============================================
1. Import unittest from the standard library
2. Create a class called TestSum that inherits from the TestCase class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the self.assertEqual() method on the TestCase class
5. Change the command-line entry point to call unittest.main()

Run Tests With pytest
=================================================
pytest supports execution of unittest test cases.
 
The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.
 
pytest has some other great features:
 
1. Support for the built-in assert statement instead of using special self.assert*() methods
2. Support for filtering for test cases
3. Ability to rerun from the last failing test
4. An ecosystem of hundreds of plugins to extend the functionality
