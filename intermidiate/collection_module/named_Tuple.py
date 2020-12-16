# NAMED TUPLE: it almost creste the function will with field of your choice
from collections import namedtuple

point = namedtuple("point", 'x,y,z')
pt = point(1, -4, 5)
print(type(pt))
print(pt.x, pt.y, pt.z)

# adding the two namedtuple is tuple containing both elements.
ptr = point(3, 3, 3)
npt = pt + ptr
print(type(npt), npt)
