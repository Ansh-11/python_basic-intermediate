fruits=('alpha','beta','kappa','delta','gamma')
for i in fruits:
   print(i)

#--------------The else is also used with for loop else is executed if the if the foor condition is false or if the loop is finished--------
else:
   print("End of the lists")

for i in range(15):
   if( i==10):
      pass# --------------pass means [ TO DO NOTHING ]  it stop the program for throwing compilation error-----
   if(i%2==0):
      continue
   print(i)
else:
   print("Else of the for looop")
