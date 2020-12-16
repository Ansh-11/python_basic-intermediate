# LISTS - ORDERD,MUTABLE, ALLOWS DUPLICATE ENTRY
import copy

# using the list comprehension for the creation of the new list
mylist = [i**2 for i in range(1, 10)]
print(mylist)

# other way oof creating list
mylist = [34] * 8
print(mylist)
mylist = ["apple", "apple", "banana", "cherry", "lemon"]
print(mylist)

# to have access of any index element
print(mylist[2])

# To check if any element is present in the list
print("present") if "apple" in mylist else print("Absent")

# To know the length of the list
print(len(mylist))

# To count the number of element in the list
print(mylist.count("apple"))

# To know the index of element in the list
print(mylist.index("is"))

# to append the list [add at the end of the list]
mylist.append("jamun")
print(mylist)

# to insert the element at any posotion.
mylist.insert(0, "blueberry")       # make start
mylist.insert(-1, "strawberry")     # at 2nd last
mylist.insert(len(mylist), "mulberry")  # at last
print(mylist)

# To delete the element from pop[default its will give last value] and also return that value
item = mylist.pop()
print(item, mylist)

# To delete the element from pop using index
item = mylist.pop(0)
print(item, mylist)

# To delete the element from remove using element name it return none
item = mylist.remove("apple")
print(item, mylist)

# to clear the complete list and return none
item = mylist.clear()
print(item, mylist)

mylist = ["apple", "lemon", "banana", "cherry"]

# soritng the list
item = mylist.sort(reverse=False)
print(item, "\n", mylist)

# b soritng the listand creating the new list
lis = sorted(mylist, reverse=True)
print(lis, " \n", mylist)

# adding the two list
addlis = mylist + lis
print(addlis)

# slicing the list[start index, end index, iteration(step index)]
slic_list = mylist[0:4:1]
print(slic_list)

# reverse the list
slic_list = mylist[::-1]
print(slic_list)

# Copying the list like this will [SHALLOW COPY] and change in one will be refelected in other too
copy1 = mylist    # shallow copy by direct assignment
copy2 = copy.copy(mylist)  # shallow copy using copy method of the copoy package
copy1.append("extra")
print(mylist)
mylist.append("hello world")
print(copy1)

# creating the [DEEP COPY] in which change in one in not reflected to other
copy0 = mylist.copy()  # deep copy using copy method not from copy package
copy1 = list[mylist]  # deep copy using list
copy2 = mylist[:]  # deep copy using slicing of list
copy3 = copy.deepcopy(mylist)  # deep copy using method in copy method
copy0.append("extra")
print(mylist)
print(copy0)
mylist.append("hello world")
print(mylist)
