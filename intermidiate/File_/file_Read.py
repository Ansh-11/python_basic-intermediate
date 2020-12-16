# 'r'- reading ,
# 'w'-writing ,
# 'a'- appending ,
# 'x'- create the file if it not exists
# 't'- updating(text mode)
# 'r+'- read and write
# 'b'- binary mode
# 'rt'-read in text mode
# 'rb'-read in binary mode

# the syntax is (file name , mode of execution[default is 'r'])
f = open('sample.txt', 'r')

#  read(no of character) by default it read complete file.
data = f.read(3)
print(data)
data = f.read()
print(data)
f.close()

# [ METHOD-1 ]for reading the complete line in the file
fil = open("sample.txt", "r")
for line in fil:
    print(line, end="")
fil.close()

# [ METHOD-2 ] for reading the complete lines in the file using readline
file = open("sample.txt", "r")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), )
file.close()

# [ METHOD-3 ] for reading the complete lines in the file using readline[s] return the list of all the lines as elements[ line1 , line2 , line3]
files = open("sample.txt", "r")

# join the elements and remove the list
print("".join(map(str, files.readlines())))
# -------SHORTCUT FOR THE ABOVE-------------
# print("".join(files.readlines()))
files.close()
