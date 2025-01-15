# Methods of Tuple
# Tuple can be changed when we convert it into list and perform the changing task

country=("germany","aus","usa","uk","spain","india")
temp=list(country)
# print(temp)
temp.append("radhe")
# print(temp)
temp.pop()
country2=("italy","indonesia","afganistan")
c=country+country2  
print(c)
# Tuples methods
t=(2,4,5,6,2,35,2,5,2,5,8,8)
print(t.count(8))  #count Method 
print(t.index(4))
print(t.index(2,5,8))
 