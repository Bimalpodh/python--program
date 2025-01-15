def mergesort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    larr=arr[0:mid]
    rarr=arr[mid:] 
    mergesort(larr) 
    mergesort(rarr)
    
  i=j=k=0
  while i<len(larr)and j<len(rarr):
    if larr[i]<rarr[j]:
      arr[k]=larr[i]
      i=i+1