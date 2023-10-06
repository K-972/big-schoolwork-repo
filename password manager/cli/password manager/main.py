import time
import hashlib
import sys
from cryptography.fernet import Fernet

key = ''

global password_list
password_list = []
def decrypt(thing_to_decrypt, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(thing_to_decrypt)
    return decrypted_text.decode()

def read_file():
    with open('/workspaces/big-schoolwork-repo/password manager/cli/password manager/dictionary.txt', 'r') as dictionary:
        lines = dictionary.readlines()
        return lines

def encrypt(thing_to_encrypt, key):
    f = Fernet(key)
    cipher_text = f.encrypt(thing_to_encrypt.encode())
    return cipher_text

def check_if_edit_parameters_correct(thing_to_check):
    pass_check = False
    while not pass_check:
        print('\n') 
        prompt = input(f"Is {thing_to_check} correct or not y/n >> ")
        print('\n') 
        if prompt.lower() == 'y':
            pass_check = True  # Set pass_check to True when the input is correct
            return thing_to_check
        elif prompt.lower() == 'n':
            thing_to_check = input("Enter the correct text >> ")
        else:
            print("Invalid input. Please try again.")

        thing_to_check = input("Enter the name >> ")
        corrected_thing = check_if_edit_parameters_correct(thing_to_check)
        print(f"The corrected name is: {corrected_thing}")
        return corrected_thing
        


    



def edit(key):
    true_statement_1 = True
    while true_statement_1:
        print("type \"add\" to add to your password list\n")
        time.sleep(1)
        print("type \"remove\" to remove from your list\n")
        time.sleep(1)
        print("or type \"modify\" to modify your list\n")
        time.sleep(1)
        print("or type \"exit\" to leave the programme\n")
        time.sleep(1)
        edit_decision = input('what do you want to do >> ')

        if edit_decision.lower() == "add":
            print('\n') 
            print("----------------------------------------")
            print('\n') 
            restart = True
            while restart == True:
                time.sleep(1)
                name_of_service = input("enter name of service >> ")
                print('\n')
                time.sleep(1)
                username = input("Enter username >> ")
                encrypted_username = encrypt(username, key)
                print('\n')
                time.sleep(1)
                email = input("Enter email >> ")
                encrypted_email = encrypt(email, key)
                print('\n')
                time.sleep(1)
                password = input("Enter password >> ")
                encrypted_password = encrypt(password, key)
                print('\n')
                time.sleep(1)
                invalid_input = True

                while invalid_input:
                    check_if_correct = input(f"Name of service = {name_of_service} \n\nUsername = {username}\n\nEmail = {email}\n\nPassword = {password}\n\nIs this correct? y/n >> ")
                    print("\n")
                    if check_if_correct.lower() == 'y':
                        with open('/workspaces/big-schoolwork-repo/password manager/cli/password manager/dictionary.txt', 'a') as dictionary:
                            dictionary.write(f"{name_of_service}|{encrypted_username}|{encrypted_email}|{encrypted_password}") 
                            dictionary.write('\n')      
                        invalid_input = False
                        restart = False
                    elif check_if_correct.lower() == 'n':
                        invalid_input = False
                    else:
                        print("Invalid input. Please try again.")
                        restart = False
                    print("----------------------------------------")
                    
                

            

            



        if edit_decision.lower() == "remove":
            break
        if edit_decision.lower() == "modify":
            break
        if edit_decision.lower() == "exit":
            sys.exit()

# need to build a way to search through and select a password from the list

def exploring():
    splurge_or_search = input("\nType \"s\" to search for a password or \"e\" to see all >> \n")
    if splurge_or_search.lower() == "s":
        with open('/workspaces/big-schoolwork-repo/password manager/cli/password manager/dictionary.txt', 'r') as dictionary:
            lines = dictionary.readlines()
            password_list = [line.strip().split('|') for line in lines]
        number_of_matrix_clos = len(password_list[0])

        print(password_list)

    


    print("----------------------------------------")




#################
### main menu ###
#################

def start_screen():
    print("----------------------------------------")
    print("\n    Welcome to K9's password manager.")
    print("                     Made by K972.\n")
    print("----------------------------------------")

############
### main ###
############

def login(allowed_access):
    password_input = input("\nPlease enter password >> ")
    password_input = hashlib.sha256(str.encode(password_input)).hexdigest()
    key = input("Enter encryption key >> ")
    key_hashed = key
    password = 'e5dfed079b2bb64718bb391046739a3e342145baa274d5290f4099566531c4ee'

    hashed_key = 'c6b34ed2e923b8670ff6f4c675f9e2c71565a5b7c88384d422e46c404652a5a3'
    key_hashed = hashlib.sha256(str.encode(key_hashed)).hexdigest()
    if password_input == password and key_hashed == hashed_key:
        allowed_access = True
        time.sleep(2)
        print("\nAccess Granted")
        return allowed_access, key
    else:
        allowed_access = False
        print("wrong password")
        time.sleep(5)
        sys.exit()
        
def main(edit, key):
    allowed_access = False
    start_screen()
    mode_select = input("\nd for developer mode or u for user >> ")
    if mode_select.lower() == "d":
        allowed_access = True
        key = b'l3vZ2XL6fsl2UTCYeq-00k162exuUIrBC3_y96xFN5M='
    elif mode_select.lower() == "u":
        allowed_access = login(allowed_access)

    else:
        allowed_access = False
        print("wrong password")
        time.sleep(5)
        sys.exit()

    while allowed_access:   
            
        print("\n----------------------------------------\n")
        what_to_do_loop = True
        while what_to_do_loop == True:
            time.sleep(1)
            print("type \"edit\" to edit your password list\n")
            time.sleep(1)
            print("type \"explore\" to see your list\n")
            time.sleep(1)
            print("or type \"exit\" to exit the programme\n")
            time.sleep(1)

            what_to_do = input("what do you want to do >> ")
            print("\n----------------------------------------\n")
            if what_to_do.lower() == "edit":
                edit(key)
            
            if what_to_do.lower() == "explore":
                print("exploring")
                exploring()
            elif what_to_do.lower() == "exit":
                sys.exit()





if __name__ == "__main__":
    main(edit, key)
