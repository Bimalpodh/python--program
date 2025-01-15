for i in range(1,6):
  for j in range(1,6):
    if(i==1 and i<=5  or j==1 and j<=5 or i==5 and j<=5 or j==5 and i<=5):
      print(f"*",end=" ")
    else:
      print(" ",end=" ")
  print()
  
# Triangle pattern
n=6
print(" Triangle pattern ")
for i in  range(1,n):
  for j in  range(1,n):
    if(j<=i):
      print("x",end=" ")
  print()