# Character Count:
def charCount(length,string,fav):
  x=0
  for i in range(length):
    if string[i].lower() == fav.lower():
      x=x+1
  return x
    

s="you are good and very good but not at good at aLL"
fav="g"
length=len(s)

print(charCount(length,s,fav))