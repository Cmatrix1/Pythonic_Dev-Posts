
def cnt(len, index):
    if index >= len:
        index -= len
    return index

def check_the_travel(index):
    gasl = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    enough = gasl[index] - cost[index]
    if enough < 0:
        return -1
    
    tank = gasl[index]
    while True:
        index = cnt(len(cost), index)

        tank = tank - cost[index] + gasl[cnt(len(gasl), index+1)]
        print(tank)

        index += 1

check_the_travel(3)