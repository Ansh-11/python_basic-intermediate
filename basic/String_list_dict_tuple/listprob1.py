
lis = [234, 587, 90, 8, 65924875, 99]
# OUTPUT =[23,45,87,.....]for K=2 && [ 23458, 790865 ,.....] for k=5
print("the original list", str(lis))

# taking k in input
k = 2
# join the code in python using the list comprehension
Temporary = ''.join([str(ele) for ele in lis])
print(Temporary)

# join the code in python using the map function
Temporary = ''.join(map(str, lis))
print(Temporary)


# using th complete loop for understanding
newlist1 = []
for x in range(0, len(Temporary), k):
    newlist1.append(int(Temporary[x:x + k]))
print(newlist1)


# using the list comprehension for the creation of the split list
newlis = [int(Temporary[x:x + k]) for x in range(0, len(Temporary), k)]
print(newlis)
