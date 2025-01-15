x=int(input("enter a number::"))
y=x
while x>9:
  sum=0
  while x>0:
    sum+=x%10
    x//=10
  x=sum
if x==1:
  print(f"{x} is a magic number::")
else:
  print(f"{x} is not a magic number::")