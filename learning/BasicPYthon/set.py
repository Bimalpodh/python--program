# set is an unodered collection and immutable and unindexed data type.
#unordered means the items do not have a defined order.
#Unchangable means we can not change the items after the set has been declaire.
#set items are unchangable but we can add remove the item from the set.
#set does not allow dublicate value.
#in set the items are enclosed with curly braces.

s={1,2,4,5}
s1={3,4,9}
# union() is used to combine the element which are not in 1st set
print(s.union(s1))
# update(): is used to add the element which are not in set 1
s.update(s1)
print(s,s1)
set3={"kabul","america","usa","jamaica"}
set4={"aus","India","uk","jamaica"}
# intersection(): is used to find the common element between twoo set:
# intersection_update(): is used to update  the  set by add common element between two set:

# print(set3.intersection(set4))
# set3.intersection_update(set4)
# print(set3,set4)

#Symmetric(): is used to provide differance of two set and the union of rev differance of that 2set
# A△B=(A-B)U(B-A)
print(set3.symmetric_difference(set4))
# isdisjoint()and issuperset()  issubset() :it returns true if set is superset of another set


# add() is used in set to add value in set
# s.add("rama")
# print(s)

# remove() and discard() : is used to remove  element from the set
# diff between remove and discard is that , in remove() if element is not in set than it throw error but discard does not throw error
# s.remove("krishna")
# s.discard("krishna")

# pop() is used to remove last  element
# del setname : is used to del the entire set
# del set3
# print(set3)

# clear() : method is used to clear the  set 
# s1.clear()

if "india" in set4:
  print("true")
else:
  print("None")