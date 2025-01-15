import time
greet=time.strftime('%H:%M:%S')
timestamp2=time.time()
locTm=time.ctime(678473)
print(timestamp2) # get the current time in seconds since the epoch
print(greet)
if greet>="4" and greet<"12":
  print("Good Morning ")
elif greet>="12" and greet<"17":
  print("Good afternoon ")
elif greet>="17" and greet<"20":
  print("Good Evening")
elif greet>="20" and greet<= "24":
  print("good ninght")
  