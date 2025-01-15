# Longest common prefix

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
      if not strs:
        return ""
      prefix=strs[0]
      for string in strs[1:]:
        while string[:len(prefix)]!=prefix:
          prefix=prefix[:-1]
          if not prefix :
            return""
      return prefix



strs=["flower","flow","flight"]
obj1=Solution()

print(obj1.longestCommonPrefix(strs))