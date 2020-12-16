# ITERTOOLS : product,permutation,combination,combination with replacement
from itertools import *
from operator import *
from typing import List

# using product
a = [1, 2, 3]
b = ["a"]
pro = product(a, b, repeat=2)
print(pro)
print(list(pro))

# using permutation
a = [1, 2, 3]
permu = permutations(a, 2)
print(permu)
print(list(permu))

# using combination
a = [1, 2, 3]
comb = combinations(a, 2)
print(comb)
print(list(comb))

# using combination with replacement
a = [1, 2, 3]
comb_replace = combinations_with_replacement(a, 2)
print(comb_replace)
print(list(comb_replace))

# using accumulation (cumulative) default is cumulative sum of
a = [1, 2, 3, 4]
acc = accumulate(a)
print(acc)
print(list(acc))
name = ["Ansh", "roshan", "Khankitta"]
acc = accumulate(name)
print(list(acc))
acc = accumulate(a, func=mul)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))

# USING GROUP BY  function
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, val in group_obj:
    print(key, list(val))

# for the group by function to work properly the together values must be written together.
person = [{'name': 'Ansh', 'age': 19}, {'name': 'Anuj', 'age': 19}, {'name': 'Manish', 'age': 19}, {
    'name': 'Aman', 'age': 18}, {'name': 'Manav', 'age': 8}, {'name': 'Piyankesh', 'age': 18}]
group_obj = groupby(person, key=lambda x: x['age'])
for key, val in group_obj:
    print(key, list(val))
