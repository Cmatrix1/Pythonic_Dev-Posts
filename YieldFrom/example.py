l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]


def flat(l):
    if isinstance(l, list):
        for i in l:
            yield from flat(i)
    else:
        yield l


print(list(flat(l)))