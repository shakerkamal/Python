def greet(name, message='Hi'):
    return f"{message} {name}"




print(greet("Harry", "Hello"))
print(greet("john"))



def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet('Hello')
print(greeting) # ===> returns Hi Hello

#fix
greeting = greet(message="Hello")
print(greeting) ### ===> returns Hello there