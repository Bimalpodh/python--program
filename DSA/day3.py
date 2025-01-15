# day3:
# Description:
# You are two positive integers upper and lower. Fins the sum of all the numbers that are even-valued in the given range of upper and lower where both are inclusive. Print -1 if upper and lower are less than zero.
# Constraints:
# upper, lower >= 0
# Example:
# Input:

# 10

# 20
# Output:
# 90

# Explanation:
# Sum of even-valued elements between 10 and 20 is 10+12+14+16+18+20 = 90


"""x,y=map(int,input("enter two range by giving space: ").split(" "))
sum=0
for i in range(x,y+1):
  if 1 !=i&1:
    sum=sum+i
print(sum)"""

#________________________________________________________________________________# 
"""2.Description:
Write a program to take input as a string from user and Task is to eliminate the given two letters from the given words or sentences and display the resultant words.

Constraints:
The input string may contain alphabetic characters (both uppercase and lowercase), numbers, symbols, or spaces.
The input string length can range from 1 to 10^5 characters.
The letters to eliminate can be any alphabetic characters (both uppercase and lowercase).
Example:
I/p:
Instacks
s

t
O/p:  Inack
"""
# def removeGivencharFromString(str1,x,y):
#   li=list(str1)
#   s=""
#   for i in li:
#     if i!=x and i!=y:
#       s=s+i
#   print(s)
# str1="Bimalbabu"
# x,y="i","a"
# removeGivencharFromString(str1,x,y)

"__________________________________________________________"
"""
3.Description:
Find if a number is a palindrome or not by following the below steps:

Read the number.
Find the sum of the number and the reverse of the number.
Check if the sum is a palindrome.
If it is a palindrome, print it; otherwise, repeat the steps until a palindrome is found.
Input Format:

An integer representing the number.
Output Format:

Print the palindrome sum.
Constraints:
N > 0
Example:
Input:
87

Output:

4884
"""

def revers(x):
  y=x
  rev=0
  while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
  return rev 

x=45647867
sum=x
print(revers(x))
while sum!=revers(x):
  y=revers(sum)
  if sum==y:
    print(sum," it is pollindrom")
    break
  sum=sum+y
  
  