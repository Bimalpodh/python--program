# # Bubble sort 
def bubbleSort(arr):
  length=len(arr)
  for i in range(length-1):
    swap=False
    for j in range(length-i-1):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
      swap=True
    if swap==False:
      break
  return arr

arr=[3,6,1,89,336,95,948,6,1,8]
print(bubbleSort(arr))

# # Dsa Question of Bubble sort

# # Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# '''
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
# '''
# print("  Dsa Question ")
# class DsaBubble:
#   def MoveZeroes(self,arr):
#     l=len(arr)
#     for i in range(l-1):
#       for j in range(l-i-1):
#         if(arr[j]==0  ):
#           arr[j],arr[j+1]=arr[j+1],arr[j]
          
#     return arr
  
# arr1=[0,7,9,0,6,0,2,99,0,66]
# print(arr1.count(0))
# b=DsaBubble()
# print(b.MoveZeroes(arr1))

# s="pwwkew"
# l=len(s)
# s1=""
# s2=""
# for i in range(l):
  
#   if s[i] not in s1:
#     s1=s1+s[i]
#   else:
#     if len(s2)<=len(s1):
#       s2=s1
#     s1=""
#     s1=s1+s[i]

# print("substring",s2)
# print(len(s2))


    
    
  