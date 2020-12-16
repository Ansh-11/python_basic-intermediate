# Dictionary: Key-value pairs(), Unordered ,Mutable
import copy

# keys must be anything immutable or unhashable [NUMBER, TUPLE ,STRING] but values can be anything,
my_dict = {3: 6, 9: 7, 8: 67, (6, 7): [5, 6, 7, 8]}
print(my_dict)
value = my_dict[(6, 7)]
print(value)
my_dict = {"name": "Ansh", "age": 19, "city": "bhagalpur"}
print(my_dict)
my_dict = dict(name="Ansh roshan", age=19.5, city="Bhagalpur")
print(my_dict)

# Accesing the key of the dictionaries
for key in my_dict.keys():
    print(key)

# Accesing the keys and values of the dictionaries
for val in my_dict.values():
    print(val)

# Accesing the keys and values of the dictionaries
for ke, val in my_dict.items():
    print(ke, val)
print(my_dict["name"], "\t\t", my_dict["age"])


# Adding the new keys for the addition of the dictionaries.
my_dict["email"] = "anshroshan@gmail.com"
print(my_dict)

# Removing the keys from the dictionaries
my_dict.pop("city")
print(my_dict)

# Removing the last key from the dictionaries and return the tuple
item = my_dict.popitem()
print(item, my_dict)

# finding the ley in the the dictionaries
if "name" in my_dict:
    print(my_dict["name"])

# using the try and catchstatement in the python
try:
    print(my_dict["lastname"])
except Exception as e:
    print(e)

# Copying the dictionaires like this will [SHALLOW COPY] and change in one will be refelected in other too
copy1 = my_dict    # shallow copy by direct assignment
copy2 = copy.copy(my_dict)  # shallow copy using copy method of the copy package
copy1["email"] = "anshroshan@gmail.com"
print(my_dict)
my_dict["email"] = "Amazon.com"
print(my_dict)

# creating the [DEEP COPY] in which change in one in not reflected to other
copy0 = my_dict.copy()  # deep copy using copy method not from copy package
copy1 = dict[my_dict]  # deep copy using dictionaires
copy3 = copy.deepcopy(my_dict)  # deep copy using method in copy method
copy0["email"] = "anshroshan@gmail.com"
print(my_dict)
print(copy0)
my_dict["email"] = "Amazon.com"
print(my_dict)

# updating the dictionaries [updating the existing key or adding the new keys]
dic1 = {"name": "Ansh", "age": 19, "city": "bhagalpur"}
dic2 = dict(name="Ansh roshan", city="Bhagalpur", email="anshroshan@gmail.com")
dic1.update(dic2)
print(dic1)
