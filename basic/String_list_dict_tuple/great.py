large = 0.0
for i in range(4):
    num = int(input("enter the number"))
    if(large < num):
        large = num
print("largest number=", large)

#  sorting using list
large = [int(input("enter the number")) for i in range(4)]
large.sort(reverse=True)
print("largest number", large[0])

#  sorting using set
large = {int(input("enter the number")) for i in range(4)}
large = sorted(large)
print(large)
print(sorted(large, reverse=True))
