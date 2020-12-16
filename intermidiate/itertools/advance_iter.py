# ITERTOOLS : product,permutation,combination,combination with replacement
from itertools import *
from operator import *
from typing import List

#   COUNT is itertools in the parameter(start=0,step=1)by default
for x in count():
    print(x)
    if x == 11:
        break

#   CYCLE is itertools in the parameter( iterable)by default
a = [1, 2, 3, 4, 5]
for x in cycle(a):
    print(x)

#   REPEAT is itertools in the parameter( iterable)by default
a = [1, 2, 3, 4, 5]
for x in repeat(a, 2):
    print(x)

# using compress() selectively print data values
print("The compressed values in string are : ", end="")
print(
    list(compress('ANSH ROSHAN', [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1])))

# initializing list
li = [2, 9, 4, 0, 3, 8, 5, 7, 8]

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(dropwhile(lambda x: x != 0, li)))

# using filterfalse() to print false values
print("The values that return false to function are : ", end="")
print(list(filterfalse(lambda x: x % 2 == 0, li)))

# using islice() to slice the list [   islice(iterable, start, stop, step)  ]
print("The sliced list values are : ", end="")
print(list(islice(li, 1, 6, 2)))

# using takewhile() to print values till condition is false.
print("The list values till 1st false value are : ", end="")
print(list(takewhile(lambda x: x != 0, li)))

# using tee() to make a list of iterators makes list of 3 iterators having same values.
it = tee(iter(li), 3)
for i in range(3):
    print(list(it[i]))

# using zip_longest() to combine two iterables.
print("The combined values of iterables is  : ")
print(*(zip_longest('abcdefg', '0123456789', fillvalue='#')))

# initializing tuple list
li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]
# using starmap() for selection value acc. to function selects min of all tuple values
print("The values acc. to function are : ")
print(list(starmap(min, li)))
print(list(starmap(max, li)))
