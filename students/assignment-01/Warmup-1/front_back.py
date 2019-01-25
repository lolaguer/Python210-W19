def front_back(str):
  if len(str) > 1:
    first_char = str[0]
    last_char = str[-1]
    return last_char + str[1:-1] + first_char
  else:
    return str