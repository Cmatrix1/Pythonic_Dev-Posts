d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}


dn = {}
for key in d1.keys() & d2.keys():
    dn.update({key: (d1.get(key), d2.get(key))})

print(dn)



d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}


dn = {}
for key in d1.keys() ^ d2.keys():
    dn.update({key: (d1.get(key) or d2.get(key))})

print(dn)