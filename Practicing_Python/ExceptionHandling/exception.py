import os

# a=5
# b=6
# print(a//b)

# l=[1,4,5, [45],[4,5,6]]
# print(l[4][1])

# Problem 1:
# Write a program that asks the user to enter a number and prints its square.
# If the user enters a non-number (like "hello"), catch the error and show a friendly message.

# try :
#   n=int(input("enter a number "))
#   d=100//n
#   p=n**2
#   print(p)
# except ZeroDivisionError as e:
#   print("a number is not divisible by 0 ")
# except ValueError as e:
#   print("enter a valid number ",e)
# finally:
#   print("keep coding")


# prob-2
# Create a program that opens a file named data.txt, reads the content, and prints it.
# Handle the case when the file does not exist using FileNotFoundError.
# Also, make sure the file is closed properly using finally.

try :
  
    with open("file.txt","r") as f:
      text=f.read()
      print(text)
except FileNotFoundError as e:
  print("file is not found",e)
finally:
  print("done")


# user define exception handling

class TooYoungAgeError(Exception):
  def __init__(self,age,msg=None):
    if msg is None:
      msg="you are too young to register the site"
    self.age=age
    self.msg=msg
    super().__init__(self.msg)
    
  def __str__(self):
    return f"{self.age} is {self.msg}"
  
def register_age(age):
  if age > 18:
    print("you are eligible ")
  else:
    return TooYoungAgeError(age)
  
try:
  age=int(input("Enter your  age "))
  register_age(age)
except TooYoungAgeError as e:
  print("just wait for you moments :",e)
