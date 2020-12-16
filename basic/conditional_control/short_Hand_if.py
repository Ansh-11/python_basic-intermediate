
n = int(input("Enter the age for voting"))
if n >= 18:
    print("You are eligilble")
else:
    print("You are not eligilble to vote")

# short hand use of the if else statement
print("You are eligilble") if n >= 18 else print("You are not eligilble to vote")

# short hand use of the if else statement for chosing the value between two
age = n**2 if n >= 18 else n
print(" age of the man", age)
