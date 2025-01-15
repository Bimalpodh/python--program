# import functools 
a=[2,3,4,2,3,4,5,6,4,7]
b=[]
c=[]
for i in range(len(a)):
  f=a.count(a[i])
  if f>1:
    b.append(a[i])
  else:
    c.append(a[i])
print(c)
m=1
for i in c:
  m=m*i
print(m) 
# y=functools.reduce(lambda x,y:x*y,c)
# print(y)