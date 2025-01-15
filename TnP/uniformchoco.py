arr=[3,7,2,10]
l=len(arr)
sum=0
need=[]
for i in range(0,l):
  sum+=arr[i]
print(sum)
avg=sum//l
print(avg)
for i in range(0,l):
  if(arr[i]>avg):
    need.append(arr[i]-avg)
    
    
  else:
    need.append(avg-arr[i])
    
  
print(need)

  