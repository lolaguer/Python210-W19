def string_match(a, b):
  min_len = min(len(a), len(b))
  count = 0
  for i in range(min_len):
    if (len(a[i:i+2]) == 2) and (a[i:i+2] == b[i:i+2]):
        count +=1
  return count