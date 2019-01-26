def front_times(str, n):
  if n < 0:
    return 'Try with a positive number'
  else:
    return str[:3]*n


# Purposed solution:

def front_times(str, n):
  front_len = 3
  if front_len > len(str): #Why is this important? I mean if the len of the string is 2, string[:6] == string
    front_len = len(str)
  front = str[:front_len]

  result = ""
  for i in range(n):
    result = result + front
  return result