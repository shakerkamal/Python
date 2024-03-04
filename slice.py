colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

sub_colors = colors[:3]   # returns a list that includes the first three elements
print(sub_colors)  # ['red', 'orange', 'yellow']

sub_colors = colors[-3:]   # returns a list that includes the last 3 elements
print(sub_colors)  # ['blue', 'indigo', 'violet']


sub_colors = colors[::2]  # a sublist that includes every 2nd element
print(sub_colors) # ['red', 'yellow', 'blue', 'violet']


reversed_colors = colors[::-1]  # reverse the list
print(reversed_colors)  # ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']



#       to partially replace and resize a list

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f"The list has {len(colors)} elements")

colors[0:2] = ['black', 'white', 'gray']
print(colors)
print(f"The list now has {len(colors)} elements")

# The list has 7 elements
# ['black', 'white', 'gray', 'yellow', 'green', 'blue', 'indigo', 'violet']
# The list now has 8 elements


del colors[2:5]
print(colors) # ['red', 'orange', 'indigo', 'violet']
