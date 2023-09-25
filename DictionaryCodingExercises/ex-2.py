

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}


def get_common_values(dict1: dict, dict2: dict):
    return {key: (dict1[key], dict2[key]) for key in dict1.keys() & dict2.keys()}


print(get_common_values(d1, d2))