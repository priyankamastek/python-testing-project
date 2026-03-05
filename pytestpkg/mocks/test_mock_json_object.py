from unittest.mock import Mock

def test_mock1():
  json = Mock()
  print(json)
  # if you’re mocking the json library and you call dumps(),
  # the Python mock object will create the method so that its interface can match the library’s interface
  print(json.dumps())
  #print(json.loads())
  json.loads('{"key": "value"}')
   # Assertions - calling the mocked loads method
  # .assert_called(): Ensures that you called the mocked method.
  print(" Load called times - ", json.loads.call_count)  # Number of times you called loads()
 # json.loads.assert_called()
  # .assert_called_once(): Checks that you called the method exactly one time.
  #json.loads.assert_called_once()
  # .assert_called_with(*args, **kwargs): Ensures that you called the mocked method at least once with the specified arguments.
  #json.loads.assert_called_with('{"key": "value"}')
  # .assert_called_once_with(*args, **kwargs): Checks that you called the mocked method exactly one time with the specified arguments.
  #json.loads.assert_called_once_with('{"key": "value"}')
  # .assert_not_called(): Ensures that you never called the mocked method.




