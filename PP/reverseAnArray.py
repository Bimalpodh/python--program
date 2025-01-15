def reversedSumofAnArray(input1,input2):
    max=0
    li=input1[::-1]
    for i in range(0,input2,2):
      max+=li[i]
    return max
        
input1=[10,20,30,40,50,60]
input=6
print(reversedSumofAnArray(input1,input))