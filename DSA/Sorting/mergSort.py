# Merge Sort

def merg(arr,left,mid,right):
  a=[]
  i=left
  j=mid+1
  while(i<=mid and j<=right):
    if(arr[i]<=arr[j]):
      a.append(arr[i])
      i=i+1
    else:
      a.append(arr[j])
      j=j+1

  # left half
  while(i<=mid):
    a.append(arr[i])
    i=i+1
  
  # right half
  while(j<=right):
    a.append(arr[j])
    j=j+1
     
  for k in range(len(a)):
    arr[k+left]=a[k]

  del a
  
  
def mergsort(arr,left,right):
  if(left<right):
    mid=left+(right-left)//2
    mergsort(arr,left,mid)
    mergsort(arr,mid+1,right)
    merg(arr,left,mid,right)
  return arr


def BinarySearch(arr, tar):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==tar):
            return mid
        elif arr[mid]<tar:
            left=mid+1
        else:
            right=mid-1
    return -1


arr=[1,70,37,9,56,67,3,78]
tar=9
print('eyeyeyeye')
# print(mergsort(arr,0,len(arr)-1))

print("BinarySearch::  ",BinarySearch(arr, tar))