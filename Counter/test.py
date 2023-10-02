from collections import Counter
import random
random.seed(0)

widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]


def max_counter(data: dict, cnt: Counter=None):
    cnt = cnt or Counter()
    for k, v in data:
        cnt.update({k: v})
    return cnt

refund_counter = max_counter(refunds)
order_counter = max_counter(orders)


result = order_counter - refund_counter
print(result)