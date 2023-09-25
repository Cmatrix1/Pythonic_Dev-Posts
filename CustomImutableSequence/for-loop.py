from exerisise import Arithmetic


sequence = Arithmetic(10)


index = 0
lst = []
while True:
    try:
        sequence.__getitem__(index)
        lst.append(index)
        index += 1
    except IndexError:
        break

