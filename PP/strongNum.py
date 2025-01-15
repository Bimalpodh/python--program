x=405
y=x
sum=0

while x>0:
  r=x%10
  fact=1
  while(r!=0):
    fact=fact*r
    r=r-1
  sum=sum+fact
  x=x//10
  
print(sum)
print(x)
if sum==y:
  print("strong Number")
else:
  print("not a strong Number")
  