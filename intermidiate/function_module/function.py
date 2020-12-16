def greatest(a,b,c):
   if(a>b):
      if(a>c):
         return a
      else:
         return b
   elif(b>c):
      return  b
   else:return c

def grt(a,b,c):
   large=a
   if(large<b):
      large=b
   if(large<c):
      large=c
   return large

def great(a,b,c):
   list=[a,b,c]
   list.sort(reverse=True)
   return list[0]

def greater(a,b,c):
   set={a,b,c}
   set=sorted(set,reverse=True)
   return set[0]

print (grt(34,4,12))
print (great(34,4,12))
print (greater(34,4,12))
print (greatest(34,4,12))

