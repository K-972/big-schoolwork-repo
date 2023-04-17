import hashlib
from hashlib import sha256

# i don't know what this does or why it is here. but it stays because everytime i remove it my programme breaks
import os
print(os.getcwd())

def create_password():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    username = hashlib.sha256(username.encode('utf-8')).hexdigest()
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open('password.txt', 'a', encoding='utf-8') as file:
        file.write(username)
        file.write('\n')
        file.write(password)

def login():
    alive_username = input('Enter your username: ')
    alive_password = input('Enter your password: ')
    alive_username = hashlib.sha256(alive_username.encode('utf-8')).hexdigest()
    alive_password = hashlib.sha256(alive_password.encode('utf-8')).hexdigest()

    with open('password.txt', 'r') as file:
        username = (file.readline())
        print(alive_username)
        print(username)
        password = (file.readline())
        print(password)
        print(alive_password)

    if alive_password == password and alive_username == username:
        with open('document.txt', 'r', encoding='utf-8') as file:
            print('#to do')
            pass
    else: 
        print('wrong password')




#user = hig
#pass = highig

main_menu = input('press - 1 to login    press - 2 to create a password: ')
if main_menu == '1':
    login()
elif main_menu == '2':
    create_password()
else:
    pass