cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)
# New York
# Beijing
# Cairo
# Mumbai
# Mexico
    
for item in enumerate(cities):
    print(item)

# (0, 'New York')
# (1, 'Beijing')
# (2, 'Cairo')
# (3, 'Mumbai')
# (4, 'Mexico')
    

# unpack the tuple
for index, city in enumerate(cities):
    print(f"{index}: {city}")

# 0: New York
# 1: Beijing
# 2: Cairo
# 3: Mumbai
# 4: Mexico
    
for index, city in enumerate(cities,1):
    print(f"{index}: {city}")

# 1: New York
# 2: Beijing
# 3: Cairo
# 4: Mumbai
# 5: Mexico