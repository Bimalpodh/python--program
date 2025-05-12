str="A Quick Brown Fox"
c=0
l=0
print(len(str))
for i in (str):
  if i.isupper():
    c=c+1
  elif i.islower():
    l=l+1

print(c, l)
