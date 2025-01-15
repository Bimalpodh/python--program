# Dictionary Methods ::
# update() :: is used to update data in dict
ep1={122:45,566:90}
ep2={222:67,568:90}
ep1.update(ep2)
print(ep1)

# clear() :: is used to remove all the elements of the dictionary
# ep1.clear()
# print(ep1)

# popitem():: is used to remove the last value pair element of the list
# ep1.popitem()
# print(ep1)

# del :: keyword is used to delete the dictionary:
# del ep1
del ep1[122]
print(ep1)