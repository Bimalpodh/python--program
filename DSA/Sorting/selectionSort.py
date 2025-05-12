# Selection Sort
def selectionSort(arr):
  n=len(arr)
  for i in range(n):
    min_index=i
    for j in range(i+1,n):
      if(arr[j]<arr[min_index]):
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr
arr=[3,1,898,67,34,9,34,890]
print(selectionSort(arr))

# selection Sort problems
# 1.Q what will the array look like after the first iteration of selection sort[2,3,1,6,4]
print(":::::::: practise ::::::::")
def selectionSort1(arr):
  n=len(arr)
  for i in range(n):
    minIndex=i
    for j in range(i+1,n):
      if arr[j]<arr[minIndex]:
        minIndex=j
    arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr
  
arr1=[2,3,1,6,4]
print(selectionSort1(arr1))