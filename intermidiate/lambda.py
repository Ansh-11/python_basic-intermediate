# LAMBDA arguements: expressions
from functools import *

point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

#   DEFAULT it will sort according the first element in the tuple i.e[x coordinate]
point2D.sort()
print(point2D)
#   To sort the function according the y cordinates
point2D.sort(key=lambda X: X[1])
print(point2D)
#   To sort the function according the sum of coordinates
point2D.sort(key=lambda X: X[0]+X[1])
print(point2D)

#  ---> MAP(function,list)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
# list comprehension with [for loop]is the little better.
c = [x*2 for x in a]
print(list(c))

# ---> FILTER(function,list)
a = [1, 2, 3, 4, 5]
b = filter(lambda x: x % 2 != 0, a)
print(list(b))
# list comprehension with [for loop using (if)]is the little better.
c = [x for x in a if x % 2 != 0]
print(list(c))

# ---> REDUCE(function,list)
a = [1, 2, 3, 4, 5, 6]
b = reduce(lambda x, y: x+y, a)
print(b)
