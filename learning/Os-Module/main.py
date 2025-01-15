import os

# if(not os.path.exists("data")):
#   os.mkdir("data") #this code is written to create a directory name data 
  
# for i in range(0,100):
#   # os.mkdir(f"data/Day{i+1}")  #this code is written to create a directory name Day1 to Day100
#   os.rename(f"data/tutorial{i+1}", f"data/tutorial {i+1}")
  # syntax-of-rename //os.rename("source ","destinantion")
folders=os.listdir("data")
print(folders)

x=os.path
print("path",x)
# print(os._exit())
print(os.getcwd())
print(os.name)

# how to delete remove  directory
