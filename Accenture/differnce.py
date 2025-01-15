def differance(input1,input2):
  c1=input1.count(" ")
  c2=input2.count(" ")
  diff=abs(c1-c2)
  if diff%2==0:
    return f"Even{diff}"
  else:
    return f"Odd{diff}"


s="hello world"
s2="he ll o w or ld "
c=s.count(" ")
print(differance(s,s2))