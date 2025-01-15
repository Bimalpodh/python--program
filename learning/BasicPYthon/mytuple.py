# Tuples are the order collection of items.
# Tuples are immutable, meaning they cannot be changed after creation.
# Tuples are defined by enclosing items in parentheses ().
# Tuples are faster than lists because they are immutable.
# Tuples are useful when you need to store a collection of items that should not be changed.
# Tuples are also useful when you need to store a collection of items that should be treated as a single unit.
# Tuples are also useful when you need to store a collection of items that should be passed to a function or method that expects a tuple as an argument.
tup=(4,5,8,95,89,90)
print(type(tup),tup)
print(tup[-1])
if  8 in tup:
  print("present in tup ")

tup2=tup[1:4]
print(tup2)