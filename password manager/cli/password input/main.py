import hashlib

array = [
    ['user1', 'password1'],
    ['user2', 'password2'],
    ['user3', 'password3']
]

def main():
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
                return
            else:
                print("Incorrect password")
                return

    print("Username not found")

main()
