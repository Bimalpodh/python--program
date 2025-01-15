print("Enter number in range between 0-5")
x=int(input("Enter a number::"))
match x:
  case 1:
    print("One")
  case 2:
    print("Two")
  case 3:
    print("Three")
  case 4:
    print("Four")
  case _ if x%2==0:
    print("Even")
  case _:
    print("Enter valid number::")