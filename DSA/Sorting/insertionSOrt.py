# Insertion Sort

def insertionSort(arr):
  n=len(arr)
  for i in range(n-1):
    j=i+1
    while(j>=1 and arr[j]<arr[j-1]):
      arr[j],arr[j-1]=arr[j-1],arr[j]
      j=j-1
  return arr
arr=[9,14,46,43,27,57,41,45,21,70]
print(insertionSort(arr))