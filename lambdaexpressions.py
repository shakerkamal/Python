def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)



def first_last(first_name, last_name):
    return f"{first_name} {last_name}"

def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John

#   instead of writing two different fucntions
#   a lambda expression can be used

full_name = get_full_name('John', 'Doe',
                          lambda first_name,last_name: f"{first_name} {last_name}")
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', 
                          lambda first_name, last_name: f"{last_name}, {first_name}")
print(full_name) #  Doe, John





# a fuction that retuns a function
def times(n):
    return lambda x: x * n


double = times(2)

result = double(2) #    prints 4
result = double(4) #    prints 8




# lambda in a loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())





