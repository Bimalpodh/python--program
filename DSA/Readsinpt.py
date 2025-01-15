# Day1:
# Description:
# Write a program that reads three integers from the standard input and prints them to the standard output. Each integer should be printed on a new line.
# 'x,y,j=map(int,input("Enter number and separate them by comma :: ").split(","))'
# print(x)
# print(y)
# print(j)
# s,t,p=map(str,input("Enter string and separate them by - ::" ).split("-"))
# print(s)
# print(t)
# print(p)

# 2.Write a  program that swaps two numbers without using a third variable. 
#  xample 1:
# Input:
# a=10 20
# b=20 10
# x=70
# y=20
# x,y=y,x # c=x,x=b,b=c, ::a=a^b, b=a^b,a=a^b
# print(x,y) 

# 3.If lengths of three sides of a triangle are input through the keyboard, write a program to find the area of the triangle.
# import math
# a=45   #int(input("enter side length of a:: "))
# b=48   #int(input("second side length of b:: "))
# c=44   #int(input("third side length of c:: "))
# s=(a+b+c)//2
# area1=(s*(s-a)*(s-b)*(s-c))**0.5
# area=math.sqrt((s*(s-a)*(s-b)*(s-c)))

# print(f"{area:.3f}","   ",f"{area1:.4f}")

# 4.Write a  program that accepts two item’s weight (floating points' values ) and number of purchases (floating points' values) and calculate the average value of the items.

item1=float(input("enter ist item weight:: "))
p1=int(input("how much/many you purchage:: "))
item2=float(input("enter 2nd item weight:: "))
p2=int(input("how much/many you purchage:: "))

avgVal=float((item1*p1)+(item2*p2))//(p1+p2)
print(avgVal)
