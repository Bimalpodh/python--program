class Solution:
  def getSum(self,a:int,b:int)->int:
    while b !=0:
      sum=a^b
      c=(a&b)<<1
      a=sum
      b=c
    return a
s=Solution()
print(s.getSum(78,9))