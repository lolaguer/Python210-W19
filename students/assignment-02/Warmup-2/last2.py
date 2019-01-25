def last2(str):
  if len(str) < 3:
    count = 0
  else:
    sub_str = str[-2:]
    count = 0
    for i in range(len(str)-2):
      print ('sub_str', sub_str)
      print(str[i:i+2])
      if sub_str == str[i:i+2]:
        count +=1
  return count