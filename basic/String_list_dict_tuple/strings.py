# # Strings = ordered ,mutable ,text representation.
from timeit import default_timer as timer
my_String = 'This is \t Ansh\'s "roshan" house '
print(my_String)
my_String = '''hello world \
good morning'''
print(my_String)

# taking out character of the my_String
char = my_String[0]
print(char)

# Forming the new substring [start index  : last index(excluded) : step ]
new_String = my_String[5]
print(new_String)
new_String = my_String[1:5]
print(new_String)
new_String = my_String[::-1]
print(new_String)

# concat the sring
fname = "ansh"
lname = "roshan"
name = fname + lname
print(name)

# acessing each of the character in the string
for x in name:
    print(x, end=" ")

# checking if the string or the substring in the string
print("present") if "sh" in name else print("Absent")

# triming the whitespace in the string [spaces at end or begining not between the letters]
my_String = "    Ansh    Rosha   n           "
my_String = my_String.strip()
print(my_String)

# changing the case of the string
print(name.upper())
print(name.lower())
print(name.capitalize())

# startinga and end
print(name.startswith("an"))
print(name.endswith("an"))

# count the occurence of the character or substring
print(name.count("an"))

# replace char or substring
print(name.replace("ansh", "Devil"))

# making list from the string and vice versa
mylist = my_String.split()
print(mylist)

# knowing the timer to know the spedd of the join method
start = timer()
new_String = " ".join(mylist)  # join is the best time,memory efficient method of concating
print(new_String)
stop = timer()
print(stop - start)

# Using the placeholder for  and using [F-STRING]
st = f" this is the {3.198456:.2f} and name is {'ansh'} and age is {19} "
print(st)
# Using the placeholder for  and using [FORMAT FUNCTION]
st = " this is the {:.2f} and name is {} and age is {} ".format(3.498567, "ansh", 19)
print(st)
# old method better not to use [NEAR TO C++] [%d -(int) ,%f -(float) %s-(string)]
st = " this is the %d and name is " % 78
print(st)
