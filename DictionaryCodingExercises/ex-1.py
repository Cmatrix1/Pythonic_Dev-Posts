


def sort_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1]))


dictoinarys = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
result = sort_dictionary(dictoinarys)
print(result)