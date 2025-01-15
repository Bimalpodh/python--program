x=289
sum=0
for i in range(1,x):
  if x%i==0:
    sum=sum+i
if sum==x:
  print("perfect No")
else:
  print("Not aperfect Number")
  