a="Bimal babu bolo juban keshari"
s="good girl !!!!!!!!!!!!!"
b=a.upper() #convert the string in Uppercase
print(b)
print(a)
print(s.strip("!")) #strip method remove the exclamatory sign it also can be removed the character which are present in sentence it does not strip the leading character
print(a.replace("Bimal","Ashutosh"))
print(a.capitalize())
print(a.split()) #split() method is used to convert the string or character or number into list
str="welcome to the console of mine  09"

print("Center method is used :",len(str.center(60)))
print(str.count("m"))
print(a.endswith("l"))
print(str.endswith("mo",0,13))
print(str.find("con"))
print(str.index("m"))
# print(str.index("mom"))
print(str.isalpha())
print(str.isalnum())
print(str.islower())
print(str.isprintable())
print(str.istitle())
print(str.swapcase())
print(str.startswith("hello"))
str2="Hello good girl"
print(str2.title())


