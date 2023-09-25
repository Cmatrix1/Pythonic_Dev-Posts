

# 
# def is_good(prices):
#     def for_buy(index):
#         return any([price > prices[index] for price in prices[index:]])

#     def when_sell_it(index):
#         sell_index = False
#         profit = 0
#         last_price = prices[index]
#         for p_index, price in enumerate(prices[index:]):
#         new_profit = price   last_price 
#             if profit < new_profit:
#                 profit = new_profit
#                 sell_index = p_index + index
#         return sell_index, profit
        
#     return for_buy, when_sell_it


# buy_method, when_sell_it = is_good(prices)

# buy_indexs = [] 

# for i, price in enumerate(prices):
#     is_buyable = buy_method(i)
#     sellable = when_sell_it(i)
#     if is_buyable:
#         buy_indexs.append(i)

# print("I want Buy This Days", buy_indexs)
# usesdays = []
# profit_all = 0
# profit_list = []
# for buy_index in buy_indexs:
#     price = prices[buy_index]
#     if when_sell_it(buy_index) and buy_index not in usesdays:
#         day, profit = when_sell_it(buy_index)
#         profit_all += profit
#         print(f"I can Buy on {price} and sell in on {prices[day]} profit is", profit)
#         usesdays.extend(list(range(buy_index, day)))
#         # usesdays.append(buy_index)

# print("PROFIT ALL", profit_all)



prices = [7,1,3,5,3,6,4]

value = prices[0]
profit = 0
for v in prices:
    if v < value:
        value = v
        print("Man ", v, "bekhar")
    if v > value:
        print("Man ", v, "befrosh")
        profit += v - value
        value = v
print(profit)