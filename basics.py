def main():
    i = 1
    while(i < 10):
        print(i)
        i+=1


main()

# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise


message = '"Beautiful is better than ugly.". Said Tim Peters'
message = 'It\'s also a valid string'  # escape quotes   \
message = r'C:\python\bin'  # using r to raw strings

# for multiple lines
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

# strings are immutable

name = 'Harry'         
m = 'Hi'

m = f'Hi {name}'     # f-strings to string interpolation like C#
print(m)

greeting = 'Good' ' ' 'Morning!'    # string concatenation
print(greeting)

str = "Python String"
print(len(str))
print(str[0])
print(str[1])
print(str[-1])
print(str[-2])


#  slicing
print(str[0:2])



# ** for double multiplication   3**3 = 27


is_active = True
is_admin = False

# 'a' < 'b' = True
# 'a' > 'b' = False

# ===> bool() returns false for these values

# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}



##### ===============>      Python does not support CONSTANTS


############# input function
value = input('Enter a value:')
print(value)





########## type casting
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = int(price) * int(tax) / 100
print(f'The tax amount is ${tax_amount}')

# float(str) – convert a string to a floating-point number.
# bool(val) – convert a value to a boolean value, either True or False.
# str(val) – return the string representation of a value. 


for i in range(1, 10, 2):
    print(i)