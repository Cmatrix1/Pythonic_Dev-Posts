from collections import defaultdict, OrderedDict, Counter, ChainMap, UserDict

# defaultdict example
d = defaultdict(int)
d['a'] += 1
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})

# OrderedDict example
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Counter example
c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(c)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

# ChainMap example
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
cm = ChainMap(d1, d2)
print(cm['a'])  # Output: 1
print(cm['c'])  # Output: 3

# UserDict example
ud = UserDict({'a': 1, 'b': 2})
print(ud)  # Output: {'a': 1, 'b': 2}
