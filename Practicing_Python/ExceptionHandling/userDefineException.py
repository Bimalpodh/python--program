# Task:
# Create a program that simulates a bank withdrawal.

# Ask the user for their account balance and withdrawal amount.

# If the withdrawal amount is more than the balance, raise a custom exception InsufficientFundsError.

# Else, show the remaining balance.


# class insufficientFundError(Exception):
#   def __init__(self, bal, wbal, msg="you are basically poor dear"):
#     self.bal=bal
#     self.wbal=wbal
#     self.msg=msg
#     super().__init__(self.msg)
    
#   def __str__(self):
#     return f"{self.msg}, you have only {self.bal} "
  
# def withdrawRequest(bal,wbal):
#   if wbal>bal:
#     raise insufficientFundError(bal,wbal)
#   else :
#     bal=bal-wbal
#     return f"you have succesfully withdrawl RS::{wbal} \n and you have remaining Rs::{bal}"
  
# try:
#   bal=float(input("enter your account balance: "))
#   wbal=float(input("enter your withdrawal amount "))
#   mssg=withdrawRequest(bal,wbal)
# except insufficientFundError as e:
#   print (e)

# except ValueError:
#     print("❌ Please enter a valid number.")
# else:
#   print (mssg)

# finally:
#     print("🏦 Thank you for banking with us!")
    
# Problem:
# Write a program that asks the user to enter a number.
# If the number is negative, raise a custom exception NegativeNumberError.
# Otherwise, print the square root of the number.

# import math 
# class NegativeNumberError(Exception):
#   def __init__(self,num  ,msg="enter valid possitive number "):
#     self.num=num
#     self.msg=msg
#     super().__init__(self.msg)
  
#   def __str__(self):
#     return f"{self.msg}"

# def numberCheck(num):
#   if num<0:
#     raise NegativeNumberError(num)
#   else:
#     sqrt=math.sqrt(num)
#     return sqrt
# try:
#   num=int(input("enter a number: "))
#   res=numberCheck(num)
# except NegativeNumberError as e:
#   print(e)
# except ValueError as e:
#   print(e)
# else:
#   print("The sqr root is ",res)
  

# Problem:
# Create a program that checks if a person is eligible to vote.
# If the age is less than 18, raise a NotEligibleToVoteError with a message.
# Otherwise, say "You can vote!".

# Bonus: Handle wrong inputs like "twenty" too.

class NotEligibleToVoteError(Exception):
  def __init__(self,age,msg="You are not eligible for vote :"):
    self.age=age
    self.msg=msg
    super().__init__(self.msg)
  def __str__(self):
    return f'{self.msg}, come after become 18 '
  
def ageValidate(age):
  if age<18:
    raise NotEligibleToVoteError(age)
  else:
    return f"you can vote |"

try:
  age=int(input("enter your age: "))
  mssg=ageValidate(age)
except NotEligibleToVoteError as e:
  print(e)
except ValueError as e:
  print(e)
else:
  print(mssg)
finally:
  print("thank you ")