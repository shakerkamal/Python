# When a function has a parameter preceded by an asterisk (*), it can accept a variable number of arguments. 
# And you can pass zero, one, or more arguments to the *args parameter.


# Use Python *arg arguments for a function that accepts a variable number of arguments.
# The *args argument exhausts positional arguments so you can only use keyword arguments after it.

def add(x, y, *args):   
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)   # args = [30, 40]
print(result)