def send(email, message):
    print(f'Sending "{message}" to {email}')

def _attach_file(filename):  # private method
    print(f'Attach {filename} to the message')



# another way of doing it
# mail.py

__all__ = ['send']  # send() function public and attach_file() function private

def send(email, message):
    print(f'Sending "{message}" to {email}')

def attach_file(filename):
    print(f'Attach {filename} to the message')
   