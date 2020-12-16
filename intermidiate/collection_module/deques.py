# DEQUE: it allows the opration from both the side
from collections import deque

# Deque of the element
d = deque("AnshRoshan")
print(d)

# appending from both the sides
d.append("@")
d.appendleft("#")
print(d)
print("".join(d))

# removing from both the sides.[pop]
print(d.pop(), d)
print("".join(d))
print(d.popleft(), d)
print("".join(d))

# extending from both the sides
d.extend(" is nice.")
d.extendleft(".rM")  # put them in opposite so it willl become ['M','r','.']
print(d)
print("".join(d))

# Rotate the element by the [number]
d.rotate(2)
print("".join(d))
