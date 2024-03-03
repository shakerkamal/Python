person = {
    'first_name':'John',
    'last_name':'Doe',
    'age':25,
    'favourite_colors':['green','blue'],
    'active':True
}

name = person.get('first_name')
# print(name)

person['age'] = 29

person['salary'] = 20000

# print(person)

del dict[key]

for k,v in person.items():
    print(v)

for key in person.keys(): # or just person
    print(key)

for val in person.values():
    print(val)



#  dictionary comprehension
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

newstocks = {}

for symbol, price in stocks.items():
    newstocks[symbol] = price * 1.02

print(newstocks)

newstocks = {symbol: price * 1.02 for(symbol, price) in stocks.items()}

selectedStocks = {symbol: price for(symbol, price) in stocks.items() if price > 200}