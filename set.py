# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.

skills = {'Python', 'Database', 'System Design'}

skills = set(['Problem solving','Critical Thinking'])
print(skills)  # {'Critical Thinking', 'Problem solving'}

characters = set('letter')
print(characters)  #   {'r', 'l', 't', 'e'}


ratings = {1, 2, 3, 4, 5}
rating = 1

if rating in ratings:
    print(f'The set contains {rating}')


rating = 6

if rating not in ratings:
    print(f'The set contains {rating}')   # The set does not contain 6

ratings.add(7)

ratings.remove(7)

ratings.discard(7)   # does not raise an error if the element is not in the list

ratings.pop()   # remove and return an element from a set ===> returns an unspecified element

ratings.clear()  # removes all the elements from a set


frozenset(ratings) # makes a set immutable


skills = {'Problem solving', 'Software design', 'Python programming'}

for index, skill in enumerate(skills):
    print(f"{index}.{skill}")
# 0.Software design
# 1.Python programming
# 2.Problem solving
    

# upacking sets
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

numbers = (*odd_numbers, *even_numbers)
print(numbers) # (1, 3, 5, 2, 4, 6)