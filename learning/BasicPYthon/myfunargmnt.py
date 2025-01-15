"""There are five types of argument """
# 1.Default Arguments
# 2.Keyword Arguments
# 3.Variable length Arguments
# 4.Required Argument
# 5.positional  argumentss


#1.Default Argument 
"we can provide a default value when we create a function ,thos way it takes deafault value even we do not pass the value when we call the function"
# def average(a=67,b=1):
#   print("the average is ",(a+b)/2)
  
# average(b=45)

#2.Required Argument
"in this function we have to provide value of the 1st variable ,it is required other wise it show type error"
# def mul(a,b=1):
#   print("the product is ",a*b)

# mul(34)

#3.Variable Length Arguments
# def avg(*num):
#   sum=0
#   for i in num:
#     sum=sum+i
#   print("Average is :",sum//len(num))
# avg(23,4,5,7,67,6)
  
# 4.Variable length keywords arguments::
def avg(**num):
  sum=0
  for k,v in num.items():
    sum=sum+v
    print(k,"=",v)
  return sum//len(num)
c=avg(n1=12,n2=23,n3=34,n4=55)
print(c)