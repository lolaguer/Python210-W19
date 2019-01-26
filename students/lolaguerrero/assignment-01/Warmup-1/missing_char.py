def missing_char(str, n):
  if n < 0:
    return 'Choose a index >= 0'
  else:
    return str[:n] + str[n+1:]