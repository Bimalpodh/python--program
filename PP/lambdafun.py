# lambda Function
x=lambda y,z:y*z
t=x(45,78)
print(t)

# Filter in la,bda function
def even(num):
  if num%2==0:
    return True
  else:
    return False

li=[1,3,7,14,1,2,4]
n=list(filter(even,li))
l2=list(filter(lambda x:x%2==0,li))
print(n)
print(l2)

# reduce
from functools import*
li=[1,2,3,4,5]
l2=reduce(lambda x,y:x+y,li)
l3=reduce(lambda x,y:x-y,li)
print(l2)
print(l3)

class MyClass:
    class_variable = "Shared data"

    @classmethod
    def class_method(cls):
        return f"Called class_method. Class data: {cls.class_variable}"

MyClass.class_method()
