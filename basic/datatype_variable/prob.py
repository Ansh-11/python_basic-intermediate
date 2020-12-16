dic={
   "ansh":"particle",
   "anaj":"grain",
   "kargosh":"rabbit",
   "hati":"elephant"
}
print("options for dictionaries are\n",dic.keys())
a=input("Enter the words of your choice:\t")
# we usually dic.get[a] to aviod error from causing in the interface as it return null instead of the dic[a] which return error  if the element is absent in the code
print(" The meaning of the words is:",dic[a])