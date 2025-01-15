def charCount(len,s,fav):
  x=0
  for i in range(len):
    if s[i].lower()==fav.lower():
     x=x+1
  return x 


x="you are the worst in the world"
l=len(x)
fav="t"
print(charCount(l,x,fav))
