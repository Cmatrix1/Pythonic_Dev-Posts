from collections import Counter, OrderedDict


d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


c = Counter()
for d in d1, d2, d3:
    c.update(d)

print(dict(c.most_common()))