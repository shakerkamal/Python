# Use the open() function with the 'r' mode to open a text file for reading.
# Use the read(), readline(), or readlines() method to read a text file.
# Always close a file after completing reading it using the close() method or the with statement.
# Use the encoding='utf-8' to read the UTF-8 text file.
# To specify the path to the file, you use the forward-slash ('/') even if you’re working on Windows.


# to close automatically use 'with' statement while opening the file
with open('virtualenviroments.txt') as f:
    lines = f.readlines()
    print(lines)

with open('virtualenviroments.txt') as f:
    [print(line) for line in f.readlines()]

s = open('the-zen-of-python.txt','r')   # for reading the file

s = open('the-zen-of-python.txt','w')   # for writing the file

s = open('the-zen-of-python.txt','a')   # for appending the file

# closing the file
s.close()



# reading file with encoding
with open('quotes.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())


# writing to file
with open('readme.txt', 'w') as f:
    f.write('readme')


# writing to file
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')