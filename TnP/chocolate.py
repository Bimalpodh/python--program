a=[3,45,8,10,88,32]
a.sort()
b=[]
b.sort()
for i in range(0,len(a)-1):
    for j in range(1,len(a)):
       b.append(a[j]-a[i])
print(b[0])





  


