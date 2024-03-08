tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = {t.lower() for t in tags}

lowercase_tags = set(map(lambda t: t.lower(), tags))

new_tags = {t.lower() for t in tags if t!='Numpy'}   #  {'django', 'pandas'}





#  set union
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)
s = s1 | s2
print(s)


#  set intersection
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)
s = s1 & s2
print(s)


#  set difference
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.difference(s2)
s = s1 - s2
print(s)  # Python


# set symmetric difference
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.symmetric_difference(s2)
s = s1 ^ s2

print(s)  # {python , java}


# to check if a set is a subset of another
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores <= numbers
result = scores < numbers   # proper subset
print(scores.issubset(numbers))     # True
print(numbers.issubset(scores))     # False



#  disjoint sets
letters = {'A', 'B', 'C'}
alphanumerics = {'A', 1, 2}

result = letters.isdisjoint(alphanumerics)
print(result)   # False
