# write in the file [clean the file and write what you wish]
# ! it can also create the file if the name is not present in the folder
# f = open('sample2.txt', 'w')
# f.write(" My name is Ansh roshan\n")
# f.close()

# f = open('sample2.txt', 'a')
# f.write(" Ansh roshan\n" * 2)
# f.close()

f = open('sample2.txt', 'r+')
f.write(" Ansh \n" * 3)
f.read()
print(f)
f.close()

with open("sample2.txt")as fil:
    data = fil.read()
    print(data)
