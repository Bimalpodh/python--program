# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
     
        
      
#sol=Solution()
s="abcabcbbabcd"
set1=set(s)
l=len(s)
c=0
s1=""

for i in range(l):
  if s[i] not in s1:
    s1+=s[i]
  else:
    print(s[i])
    break
  print(s1)


# print(s1)
print(len(s1),"len of ",c)