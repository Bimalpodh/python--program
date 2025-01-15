import os
folder=os.listdir("data") #os.listdir("data") is used to fetch all the folder which are available in "data" folder

# print(folder)

for fl in folder:
  print(os.listdir(f"data/{fl}"))