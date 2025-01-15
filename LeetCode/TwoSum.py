class Solution:
    def twoSum(self, nums,target):
        l=len(nums)
        li=[]
        for i in range(l):
            sum=0
            for j in range(l):
                if i!=j:
                  sum=nums[i]+nums[j]
                  if sum==target:
                    li.append(i)
                    li.append(j)
                    return li        
nums=[2,90,11,15,7]
tar=9
x=Solution()
print(x.twoSum(nums,tar))