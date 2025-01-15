# If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits. (Hint: Use the modulus operator ‘%’)
# x=int(input("Enter number which digit >1"))
# l=len(str(x))
# sum=0
# print(type(x))
# while(x>0):
#   r=x%10
#   sum=sum+r
#   x=x//10
# print(sum)

# 2.Write a program to read an amount (integer value) and break the amount into the smallest possible number of bank notes.

# Note: The possible banknotes are 100, 50, 20, 10, 5, 2 and 1
# Example 1:
BankNotes=[100,50,20,10,5,2,1]
amt=1000
dict={}
x=0
c=0


for i in BankNotes:
  if x!=amt:
     dict[i]=c+1
     x=x+i
print(dict)
    