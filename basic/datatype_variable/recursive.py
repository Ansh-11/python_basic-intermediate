def sum(a):
    if(a == 0):
        return 0
    return a+sum(a-1)


print(f"the sum of the number till it\t", sum(4))
