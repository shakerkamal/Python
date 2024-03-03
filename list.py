numbers = [1, 3, 2, 7, 9, 4]

numbers.append(100) # appends to the end of the list

last = numbers.pop() # removes the last element of the list and returns that element

second = numbers.pop(1) # removes the 2nd element element of the list and returns that element

numbers.insert(2, 10) # inserts a new element at any positon in the list

del numbers[0] # remove an element from a list by specifying the position of the element

numbers.remove(9) # removes the first element it encounters in the list  [1, 4, 4, 2]   remove(4) => [1, 4, 2]

print(numbers)