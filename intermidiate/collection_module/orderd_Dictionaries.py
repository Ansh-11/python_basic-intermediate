# ORDERED  DICTIONARIES : maintain the order even after the deletion of key and reinserting it
from collections import OrderedDict
from collections import defaultdict

order = OrderedDict()
order = {'a': 45, ' b': 56, 'e': 45, 'd': 66}
print(order)

# DEFAULT DICTIONARIES : if key are not present it will return the default value of dictionary
defaul = defaultdict(float)
# it is only way to assign in the default dictionary
defaul["alpha"] = 2.0
defaul["beta"] = 5.890
print(type(defaul))
print(defaul['gamma'])
