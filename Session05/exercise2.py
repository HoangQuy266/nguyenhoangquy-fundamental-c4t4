prices = {
    "banana" : 4,
    "apple" : 2,
    "orange":1.5,
    'pear' : 3
}
stock = {
    "banana":6,
    "apple": 0,
    'orange':32,
    'pear': 15
}

# for key, value in prices.items():
#     print(key)
#     print("price : {}".format(value))
#     print ("stock: {}".format(stock[value])
total=0.0
for key in prices:
    print(key)
    print("Price : {}".format(prices[key]))
    print("Stock : {}".format(stock[key]))
    
    total += prices[key]*stock[key]
    
    print(prices[key]*stock[key])
    print()
print("Total :{}".format(total))