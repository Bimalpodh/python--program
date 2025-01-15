import os
fname=input("Enter File name ::")
if os.path.isfile(fname):
  f=open(fname,"r")
  print(f.readlines(3))
  wc=0
  lc=0
  cc=0
  # file=f.read()
  for lines in f:
    lc=lc+1
    # print(lines)
    
    words=lines.split()
    wc=wc+len(words)
    cc=cc+len(lines) 
    
  
  print("char of count :",cc) 
  print("word of count :",wc) 
  print("lines of code :",lc) 
  f.close()
else:
  print("file not found :")

