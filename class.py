# An object is container that contains state and behavior.
# A class is a blueprint for creating objects.
# In Python, a class is also an object, which is an instance of the type.


class Person:
    pass



person = Person()

print(id(person))

print(isinstance(person, Person))



class HtmlDocument:
    extension = 'html'
    version = '5'

print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5

extension = getattr(HtmlDocument, 'extension')   # class_name, variable_name
version = getattr(HtmlDocument, 'version')

print(extension)  # html
print(version)  # 5

media_type = getattr(HtmlDocument, 'media_type', 'text/html')  # To avoid the exception, you can specify a default value if the class variable doesn’t exist
print(media_type) # text/html


# setting attribute
HtmlDocument.version = 10
setattr(HtmlDocument, 'version', 10)


# deleting attribute
delattr(HtmlDocument, 'version')
del HtmlDocument.version