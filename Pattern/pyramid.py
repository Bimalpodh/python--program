x=5
# for i in range(1,x+1):
#  print("x"*i)
 
# #  reverse
# for j in range(x,0,-1):
#   print("x"*j)
# print()

# for i in range(x):
#   print(" ",end=" ")
#   for j in range((2*i)-1):
#     print(" x",end=" ")
#   print()
  
# for i in range(1, x + 1):
#   print(' ' * (x - i) + '*' * (2 * i - 1))


# for i in range(x):
#   print(' '*(x-i)+"x"*(2*i-1))

# for j in range(x-2,0,-1):
#   print(' '*(x-i)+"x"*(2*j-1))
n = 5

# Upper part
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# Lower part
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
