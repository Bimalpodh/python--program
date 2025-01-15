x=7
k=3

if x&1:
  print("odd number")
else:
  print("even number")
print((1<<(k-1)^x)&x)