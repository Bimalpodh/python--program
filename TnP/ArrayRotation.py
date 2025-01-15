arr=[1,2,3,4,5,6,7]
arr2=[]
k=3
arr1=[]
for i in range(0,k+1):
  arr1.append(arr[i])
for j in range(k+1,len(arr)):
  arr2.append(arr[j])  
print(arr1,arr2) 
arr3=arr2+arr1
print(arr3)

# def rotate(arr,k):
#   n=len(arr)
#   k=k%n  
#   def reverse(arr,start,end):
#     while start<end:
#       arr[start],arr[end]=arr[end],arr[start]
#       start+=1
#       end-=1
#   reverse(arr,0,n-1)
#   reverse(arr,0,k-1)
#   reverse(arr,k,n-1)
#   return arr
# arr=[1,2,3,4,5,6,7]
# k=3
# rotate(arr,k)
# print(arr)