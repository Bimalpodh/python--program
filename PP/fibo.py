n=1000
a,b=0,1
sum=0
while(a<n):
  print(a,end=" ")
  a,b=b,a+b
  print(end=" ")
  if a%2==0:
    sum=sum+a
print(f"sum of even value{sum}")
print()
veg=['alu','baigan','kubi']
print(list(enumerate(veg)))
print(type(veg))

    