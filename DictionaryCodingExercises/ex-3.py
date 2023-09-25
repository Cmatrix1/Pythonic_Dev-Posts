from collections import defaultdict

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


def word_count_combine(*words):
    dct = defaultdict(int)
    for word in words:
        for key, value in word.items():
            dct[key] += value
    return dct

print(word_count_combine(d1, d2, d3))