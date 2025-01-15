# Creating a custom error  :
# we can raise error by "raise"  Keyword  
a=int(input("enter any Value in between 5 and 9 "))
if(a<5 and a>9):
  raise ValueError("value should be between 5 and 9") # Syntax
