# reduce(fn,list)
from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

# a=75, b=65, 75 + 65 = 140
# a=140, b=80, 140 + 80 = 220
# a=220, b=95, 220 + 95 = 315
# a=315, b=50, 315 + 50 = 365
# 365

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)


