import hashlib
import time
#from hashlib import *

print('welcome to my password manager')
time.sleep(1)

def main_menu_no_login():
    decicion = input('Enter: 1 - to log in, 2 - to quit and 3 - to to be called tony')
    if decicion == 1:
        log_in()
    elif decicion == 2:
        quit()
    elif decicion == 3:
        print('hi tony')
        time.sleep(3)
        main_menu_no_login()
    else:
        print('invalid input')
        time.sleep(2)
        main_menu_no_login()

array = [
    ['user1', 'password1'],
    ['user2', 'password2'],
    ['user3', 'password3']
]

def add_password():

    # new username and encode
    new_username = input('Enter the new password')
    new_username = hashlib.sha256(new_username.encode('utf-8')).hexdigest()

    # new password and encode it
    new_password = input('Enter the new password')
    new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()

    array.append([new_username, new_password])


                        

def log_in():
    print("Please log in")

    # Enter user and password and create hash
    entered_user = input("Enter username: ")
    entered_user_hash = hashlib.sha256(entered_user.encode('utf-8')).hexdigest()
    entered_password = input("Enter password: ")
    entered_password_hash = hashlib.sha256(entered_password.encode('utf-8')).hexdigest()

    # Check if username and password match with the elements of the array
    for i in range(len(array)):
        if entered_user_hash == hashlib.sha256(array[i][0].encode('utf-8')).hexdigest():
            if entered_password_hash == hashlib.sha256(array[i][1].encode('utf-8')).hexdigest():
                print("Login successful")
                pass
            else:
                print("Incorrect password")
                pass


log_in()

def main_menu_login():
    