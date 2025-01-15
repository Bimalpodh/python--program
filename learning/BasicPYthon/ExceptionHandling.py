# Exception Handing

# a=int(input("Enter the Number  "))
# print(f"multiplication of table of {a} is :")
# try:
#   for  i in range(1,11):
#     print(f"{(a)} X {i}= {int(a)*i}")
# except Exception as e:
#   print("invalid input ")
  
# print("Some imp lines of code")
# print("end of program")

# ---------------------------
# try:
#   num=int(input("enter an Integer:: "))
#   a=[6,8]
#   print(a[num])
# except ValueError:
#   print("Number Enter is not an Integer :")
# except IndexError:
#   print("index error ::")
  
# Finally Keyword is used in exception handling ::
# finally keyaword Always excute ,it means if some error occure then also it execute
# try:
#   l=[1,5,68,9]
#   i=int(input("Enter the index :"))
#   print(l[i])
# except:
#   print("some errror occured")
# finally:
#   print("I'm Always execute ::")
  
  
# user define Exception: 

# class WithdrawalError(Exception):
#     """Exception raised for errors in withdrawal operations."""
#     def __init__(self, amount, balance):
#         self.amount = amount
#         self.balance = balance
#         message = f"Cannot withdraw {amount}. Available balance: {balance}"
#         super().__init__(message)

# # Usage
# try:
#     balance = 1000
#     withdraw_amount = 1500
#     if withdraw_amount > balance:
#         raise WithdrawalError(withdraw_amount, balance)
# except WithdrawalError as e:
#     print(f"Error: {e}")
#     print(f"Attempted to withdraw: {e.amount}, Balance: {e.balance}")
#   #  Invalid age error 
# class InvalidAgeError(Exception):
#     """Exception raised for invalid age input."""
#     def __init__(self, message="Age must be between 0 and 120"):
#         self.message = message
#         super().__init__(self.message)

# # Usage
# try:
#     age = int(input("Enter your age: "))
#     if age < 0 or age > 120:
#         raise InvalidAgeError()
# except InvalidAgeError as e:
#     print(f"Error: {e}")


class creditException(Exception):
  def __init__(self, credit):
    self.credit=credit
    if credit>170:
      message="Degree with specialization"
    elif credit>150 and credit<170:
      message="Degree with honour"
    else:
      message=" Normal Degree "
    super().__init__(message)
    
    
try:
  credit=0
  raise creditException(credit)
except creditException as e:
  print(e)


# User-defined exception class
# class DegreeException(Exception):
#     """Exception for different degree classifications based on credits."""
#     def __init__(self, message):
#         super().__init__(message)

# # Function to classify degree based on credits
# def classify_degree(credits):
#     try:
#         if credits > 170:
#             raise DegreeException("Degree with Specialization")
#         elif 150 <= credits <= 170:
#             raise DegreeException("Degree with Honors")
#         elif credits < 150:
#             raise DegreeException("Normal Degree")
#     except DegreeException as e:
#         print(f"Exception: {e}")

# # Test cases
# classify_degree(67)  # Should raise "Degree with Specialization"
# classify_degree(160)  # Should raise "Degree with Honors"
# classify_degree(140)  # Should raise "Normal Degree"

# with open("file.txt","r") as f:
#   content=f.read()
# with open("file2.txt","w") as f1:
#   f1.write(content)
# with open("file2.txt","r") as f3:
#   c=f3.read()
#   print(c)
import os 
fname=input("Enter File name:: ")
if os.path.isfile(fname):
  with open(fname,"r") as f:
    content=f.read()
    print(content)
    lc=0
    cc=0
    wc=0
    for lines in content:
      lc=lc+1
      word=lines.split()
      wc+=len(word)
      cc=cc+len(lines)
  print("lc",lc)
  print("wc",wc)
  print("cc",cc)