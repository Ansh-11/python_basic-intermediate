#  # Sets : unordered , mutuable, no duplicates allowed
import copy
# Assinging the value to the set or creating the set
myset = set("Ansh Roshan")
print(myset)
myset = set([4, 2, 6])  # coverting the dictionaries into the set
print(myset)
myset = set([4, 2, 6])  # Converting the list into the set
print(myset)
myset = set((4, 2, 6))  # Converting the tuple into the set
print(myset)
myset = set()  # for the empty set

# Add the values to the set
myset.add(23)
myset.add(454)
myset.add(276)
print(myset)

# Remove the values from the set using [REMOVE] it will raise exception if element is not present
try:
    myset.remove(34)
except Exception as e:
    print(e)

# Remove the element using the [DISCARD] method ,it willnot return error incase of absence of the element
myset.discard(34)
print(myset)

# Pop the element
print(myset.pop())
print(myset)

# itterate in the set
for x in myset:
    print(x)

# OPERATIONS on the set
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {1, 2, 3, 5, 7}

# Union
union = odd.union(even)  # using method
print(union)
union = odd | even  # using symbol
print(union)
union.clear()   # using clear to clear the set and then update the set
union.update(odd)
union.update(even)
print(union)

# intersection
interscn = odd.intersection(prime)  # using method
print(interscn)
interscn = odd & prime  # using symbol
print(interscn)
interscn = odd | prime   # using intersection update to update
interscn.intersection_update(odd)
interscn.intersection_update(even)
print(interscn)

# difference
diff = odd.difference(prime)
print(diff)
diff = odd - prime
print(diff)
diff = odd.symmetric_difference(prime)
print(diff)

# subset
print(union.issubset(odd))
print(union.issuperset(even))
print(odd.isdisjoint(even))


# Clear the set
myset.clear()

myset = {23, 45, 67, 89}
# Copying the set like this will [SHALLOW COPY] and change in one will be refelected in other too
copy1 = myset    # shallow copy by direct assignment
copy2 = copy.copy(myset)  # shallow copy using copy method of the copy package
copy1.update({33})
print(myset)
myset.update({99})
print(myset)
print(copy1)

# creating the [DEEP COPY] in which change in one in not reflected to other
copy0 = myset.copy()  # deep copy using copy method not from copy package
copy1 = set[myset]  # deep copy using set
copy3 = copy.deepcopy(myset)  # deep copy using method in copy method
copy0.update({7899})
print(myset)
print(copy0)
myset.update({1099})
print(myset)
