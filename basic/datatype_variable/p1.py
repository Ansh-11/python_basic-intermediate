num = int(input("Enter the number"))
#----------- range ( starting value,ending value,iteration )
for i in range(1,10,2):
   print(type(i))
   print(num*i )
#-------------------------------<generator object <genexpr> at 0x0000013C5A585970>
print((num*i)for i in range(1,10,2))
