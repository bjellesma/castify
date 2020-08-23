def str_to_bool(string_value):
  """
  takes a string value and converts it to a boolean object
  """
  if string_value and (string_value.lower() == 'y' or string_value.lower() == "on"):
    return True
  return False