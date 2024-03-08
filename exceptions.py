# Use Python try...catch...finally statement to execute a code block whether an exception occurs or not.
# Use the finally clause to clean up the resources such as closing files.


try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('-Prior Period:'))
    current = float(input('-Current Period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales')
except ZeroDivisionError:
    print('Error! Please enter a number for net sales')
except Exception as error:
    print(error)

# handling multiple exceptions


# try:
#     # code that may cause an exception
# except Exception1 as e1:
#     # handle exception
# except Exception2 as e2:
#     # handle exception
# except Exception3 as e3:
#     # handle exception 

# except(Exception1, Exception2)
    

a = 10
b = 2

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')

# finally always gets executed and cleans up the resources
    



# Use the Python try...except...else statement provides you with a way to control the flow of the program in case of exceptions.
# The else clause executes if no exception occurs in the try clause.
# If so, the else clause executes after the try clause and before the finally clause.
    
fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')