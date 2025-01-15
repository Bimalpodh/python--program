# x=100815 #1085
# y=str(x)
# c=0
# z=""
# print(y)
# print(type(y))
# for i in y:
#   if i not in z:
#     z=z+i
# print(z)
# t=int(z)
# print(type(t))
x=10088765
y=[]
z=0
while(x>0):
  r=x%10
  y.append(r)
  
for i in y:
    if i not in y:
      z=z*10+i
print(z) 
   