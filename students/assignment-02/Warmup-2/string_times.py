def string_times(str, n):
  if n < 0:
    return 'Try with a positive number'
  else:
    return str*n


# Purposed solution

def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result