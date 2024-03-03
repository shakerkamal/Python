# The iterator is stateful. It means that once you consume an element from the iterator, it’s gone.

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)   # red

color = next(colors_iter)
print(color)  # green

color = next(colors_iter)
print(color)  # blue


# iterate over an iterator, the iterator is also an iterable object

colors = ['red', 'green', 'blue']
iterator = iter(colors)

for color in iterator:
    print(color)

# red
# green
# blue