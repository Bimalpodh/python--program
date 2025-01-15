def articTemptrack(len,arr):
  x=0
  c=1
  for temp in range(1,len):
    if arr[temp]<arr[temp-1]:
      c+=1
    else:
      if c>=3:
        x=max(x,c)
      c=1
  if c>=3:
      x=max(x,c)
  return x
        
arr=[36,40,42,25,24,23,40]
x=len(arr)
print(articTemptrack(x,arr)) 