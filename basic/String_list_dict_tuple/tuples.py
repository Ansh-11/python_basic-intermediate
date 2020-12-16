# Tuple= ordered ,imutable , allows duplicate elements [it is smaleer in sizein ]
import sys
import timeit

# creating the single tuple or multi elemnt in tuple
mytuple = ("Ansh", )  # parentesis () is optional
print(mytuple)
mytuple = "Ansh", "roshan", "is", "is"
print(mytuple)

# Unpacking the tuple but the [NUMBER OF VARIABLE = NUMBER OF ELEMENT] or use the (*)
a, b, c, d = mytuple
print(a, " ", b, " ", c, " ", d, " ")
a, *b, c = mytuple
print(a, " ", b, " ", c, " ")

# For creating the tuple to tuple and vice versa
lis = tuple(mytuple)
print(lis)
mytuple2 = tuple(lis)
print(mytuple2)

# aceesing any index of the tuple
item = mytuple[0]
print(item)
item = mytuple[-1]
print(item)

# To check if any element is present in the tuple
print("present") if "roshan" in mytuple else print("Absent")

# To know the length of the tuple
print(len(mytuple))

# To count the number of element in the tuple
print(mytuple.count("is"))

# To know the index of element in the tuple
print(mytuple.index("is"))

mytuple = 9, 45, 124, 524, 566, 125, 32, 45

# b soritng the tupleand creating the new tuple
lis = tuple(sorted(mytuple, reverse=True))
print(lis, " \n", mytuple)

# adding the two tuple
addlis = mytuple + lis
print(addlis)

# slicing the tuple[start index, end index, iteration(step index)]
slic_tuple = mytuple[0:4:1]
print(slic_tuple)

# reverse the tuple
slic_tuple = mytuple[::-1]
print(slic_tuple)

# TUPLE IS SMALERIN SIZE THAN LIST AND WORKING ON TUPLE IS TIME EFFICIENT
tup = tuple([i for i in range(100)])
print(sys.getsizeof(tup), "bytes")
lis = [i for i in range(100)]
print(sys.getsizeof(lis), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number=pow(10, 6)))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number=pow(10, 6)))
