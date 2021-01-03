ef abb(s, flag, bflag):
  if len(s) == 0:
    return flag

  elif s[0] == "a":
    flag = True
    bflag = False
    return abb(s[1:], flag, bflag)

  elif s[0] == 'b' and s[1] == 'b':
    if bflag == True:
      return False
    else:
      bflag = True
      return abb(s[2:], flag, bflag)
  
  else:
    return False



s = input()
flag = True
bflag = False
if s[0] == "a":
  x = abb(s, flag, bflag)
else:
  x = 0
if x:
  print("true")
else:
  print("false")
