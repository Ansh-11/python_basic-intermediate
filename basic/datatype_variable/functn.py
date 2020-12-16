from functools import partial

def email(idd,domian,extension):
	print(idd+domian+extension)
#useless as it will assign it in last variable
idk=partial(email,domian="@google",extension=".com")
print(idk("AnshRoshan"))

idk1=partial(email,idd="@google",domian=".com")
print(idk1("AnshRoshan"))

idd=partial(email,"Ansh")
dom=partial(idd,"@gooogle")
print(dom(".com"))

# def add(a,b,c,d):
# 	return 1000*a+100*b+10*c+d


# jo=partial(add,)
# add10=partial(jo,d=9)
# add110=partial(add10,8)
# print(jo(7))