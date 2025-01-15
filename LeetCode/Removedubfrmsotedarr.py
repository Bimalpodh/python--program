# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# class solution:
#   def removDublicatefromsortedArray(self,arr):
#     arr3=[]
#     arr4=[]
#     l1=len(arr)
#     for i in arr:
#       if i not in arr3:
#         arr3.append(i)
#       else:
#         arr4.append("_")
#     return len(arr3),arr3+arr4
    
  

# arr=[1,1,2,2,3,4,4,5,5,]
# ob=solution()
# l1,l2=ob.removDublicatefromsortedArray(arr)
# print(f"{l1} {l2}")

# class Solution:
#     def removeDuplicates(self, nums):
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
    
    
# nums=[1,1,2,2,3,3,4,4,6]
# ob=Solution()
# res=ob.removeDuplicates(nums)
# print(res)

# =================================
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Initialize the index for unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()
nums = [1, 1, 2, 2, 3, 4, 4]
k = solution.removeDuplicates(nums)
print(k)          # Output: 4
print(nums[:k])