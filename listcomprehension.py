numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)


mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))
print(highest_mountains)

highest_mountains = [m for m in mountains if m[1] > 8600]
print(highest_mountains)

lowest_moutains = [m for m in mountains if m[1] < 8600]
print(lowest_moutains)