# map(function, iterables)


def double(bonus):
    return bonus * 2


bonuses = [100, 200, 300]

iterator = map(double, bonuses)


# or

bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus*2, bonuses)
print(list(iterator))


names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))   # ['David', 'Peter', 'Jenifer']



carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)

print(list(carts))