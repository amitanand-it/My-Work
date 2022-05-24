"""
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example Code

>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
"""


from collections import OrderedDict

d = OrderedDict()

for _ in range(int(input())):
    *name, price = input().split()
    key = ' '.join(name) 
    if key not in d:
        d[key] = int(price)
    else:
        d[key] += int(price)

for k, v in d.items():
    print(k, v)

