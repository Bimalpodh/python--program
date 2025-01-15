# I: Represents 1, V: Represents 5 ,X: Represents 10, L: Represents 50, C: Represents 100 ,D: Represents 500 ,M: Represents 1,000 

class Solution:
  def romanToInteger(self,s:str)->int:
    str1=str.upper()
    num=0
    roman={
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
    }
    for i in range (len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
    return num
str=input("Enter Roman Number :: ")
ob1=Solution()
num=ob1.romanToInteger(str)
print(num)

"""class Solution:
    def romanToInt(self, s: str) -> int:
        # str1=s.upper()
        num=0
        roman={
          "I": 1,
          "IV":4,
          "V": 5,
          "IX":9,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000,
        }
        for i in range (len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num """