import hashlib

# i don't know what this does or why it is here. but it stays because everytime i remove it my programme breaks
import os
print(os.getcwd())

def create_password():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    username = hashlib.sha256(username.encode('utf-8')).hexdigest()
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    with open('password.txt', 'w', encoding='utf-8') as file: # use 'w' mode to wipe the file
        file.write(username)
        file.write('\n')
        file.write(password)
    
    print('Password created successfully.')


def login():
    alive_username = input('Enter your username: ')
    alive_password = input('Enter your password: ')
    alive_username = hashlib.sha256(alive_username.encode('utf-8')).hexdigest()
    alive_password = hashlib.sha256(alive_password.encode('utf-8')).hexdigest()

    with open('password.txt', 'r') as file:
        username = file.readline().strip()
        password = file.readline().strip()

    if alive_password == password and alive_username == username:
        
        print('Login successful!')
        while True:
            choice = input('Choose an option:\n1. View document\n2. Edit document\n3. Logout\n')
            if choice == '1':
                with open('document.txt', 'r', encoding='utf-8') as file:
                    print(file.read())
            elif choice == '2':
                with open('document.txt', 'a', encoding='utf-8') as file:
                    text = input('Enter text to add to document: ')
                    file.write('\n' + text)
            elif choice == '3':
                print('Logging out...')
                break
            else:
                print('Invalid choice. Please try again.')
            
    else: 
        print('Wrong password')




#user = hig
#pass = highig

main_menu = input('press - 1 to login    press - 2 to create a password: ')
if main_menu == '1':
    login()
elif main_menu == '2':
    create_password()
else:
    pass