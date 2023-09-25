from collections import defaultdict

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

print()

def balancer(n1:dict, n2:dict, n3:dict):
    in_all = n1.keys() & n2.keys() & n3.keys()
    all_keys = n1.keys() | n2.keys() | n3.keys()
    return {key :(n1.get(key, 0), n2.get(key, 0), n3.get(key, 0))
            for key in all_keys - in_all}

print(balancer(n1, n2, n3))