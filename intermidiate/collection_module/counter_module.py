# Counter : organizes the item in the descending as dictionaries [key-value pair]
from collections import Counter

# using counter with string
print("\nusing counter with strings ")
st = "aaaabbbbbbbbbbbbbbbcccddddddd"
mycount = Counter(st)
print(mycount)

# displaying the function of the  counter similar to dictionaries
print(mycount.keys())
print(mycount.values())
print(mycount.items())
print(mycount.most_common(2))

# using counter with list
print("\nusing counter with list")
lis = [3, 45, 5, 3, 4, 23, 3, 45, 3, 4, 3]
mycount = Counter(lis)
print(mycount)

# displaying the function of the  counter similar to dictionaries
print(mycount.keys())
print(mycount.values())
print(mycount.items())
print(mycount.most_common(2))

# using counter with tuple
print("\nusing counter with dictionaries")
dic = (3, 45, 5, 3, 4, 23, 3, 45, 3, 4, 3)
mycount = Counter(dic)
print(mycount)

# displaying the function of the  counter similar to dictionaries
print(mycount.keys())
print(mycount.values())
print(mycount.items())
print(mycount.most_common(2))

# using counter with set
print("\nusing counter with set ")
myset = {3, 45, 5, 3, 4, 23, 3, 45, 3, 4, 3}
mycount = Counter(myset)
print(mycount)

# displaying the function of the  counter similar to dictionaries
print(mycount.keys())
print(mycount.values())
print(mycount.items())
print(mycount.most_common(2))
