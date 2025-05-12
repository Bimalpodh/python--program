# 1.Description:
# Program to create a string S, and divided into ‘N’ equal parts. If string length cannot be divided into N equal parts print  False and else print equal parts of a string.

# Input Format:
# First , take a string S
# Second, take positive integer N
# Output format:

# Print N equal parts of string   (or) 'False'
# Constraints:
# N>=0
# Example:
# Input:

# String
# 3

# Output:
# St
# ri
# ng
    
# def divide_string(S: str, N: int):
#   def divide_string(S: str, N: int):
#     if len(S) % N != 0:
#         print(False)
#     else:
#         part_size = len(S) // N
#         for i in range(0, len(S), part_size):
#             print(S[i:i + part_size]) #slicing 

# # Example usage:
# S = "String"
# N = 2

# divide_string(S, N)
#----------------------------------------------------------
# 2.Description:
# Write a program to check if a given string S is a Pangram or not. A string is a pangram if it contains all the characters of the alphabet, ignoring the case of the alphabets.

# Input format:

# Take a string as input, S.
# Output format:

# Print 'Yes' if the string is a pangram.
# Print 'No' if the string is not a pangram.
# Constraints:
# The input should be a single word.
# The word should consist only of lowercase letters (a-z).
# Example:
# Input:
# abcdefghijklmnopqrstuvwxyz12
"""

def panagram(s):
  alpha=set("abcdefghijklmnopqrstuvwxyz")
  string=set(s)
  return alpha.issubset(string)

s=input("Enter string:: ")
if panagram(s):
  print("this is panagram string  ")

else:
  print("this is not panagram string  ")"""
    
#  3.Description:
# Write a program to create a string S and find the maximum occurring character in the given string. If no character is present then print the first character.

# Input format:

# Take a string as input, S.
# Output format:

# Print the maximum occurring character.
# Constraints:
# String length > 0
# Example:
# Input :   
# programming
# Output:
# r
x="programming"
c=0
l=[]
for i in x:
  y=x.count(i)
  if c<y:
    c=y
    char=i
  elif c==y:
    l.append(i)
print(char,set(l))