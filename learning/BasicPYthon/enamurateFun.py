# Enamurate function return a tuple containig the index and value of each element in the sequence .
# we can use the for loop  to unpack these tuples  and assign them to  variables.

marks=[23,6,5,78,89,88,56,78,99]
# for index ,mark in enumerate(marks[4:6]):
#   print(f"{index} :: {mark}")

set1={568,789,977,101}
print(type(set1))
for i,k in enumerate(set1,start=0):
  print(f"{i} :: {k}")
print("--------------------------------")
for index, mark in enumerate(marks,start=0):
  print(f"{index} :: {mark}")