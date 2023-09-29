import time
import hashlib
import sys
from cryptography.fernet import Fernet





def edit():
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
            break
        if edit_decision.lower() == "remove":
            break
        if edit_decision.lower() == "modify":
            break
        if edit_decision.lower() == "exit":
            sys.exit()

# need to build a way to search through and select a password from the list

def exploring():

    

    pass



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

def main():
    start_screen()
    password_input = input("\nPlease enter password >> ")
    password_input = hashlib.sha256(str.encode(password_input)).hexdigest()
    key = input("Enter encryption key: ")
    key_hashed = 'variable assignment'
    password = 'e5dfed079b2bb64718bb391046739a3e342145baa274d5290f4099566531c4ee'

    hashed_key = 'c6b34ed2e923b8670ff6f4c675f9e2c71565a5b7c88384d422e46c404652a5a3'
    key_hashed = hashlib.sha256(str.encode(key_hashed)).hexdigest()
    if password_input == password and key_hashed == hashed_key:
        allowed_access = True
        time.sleep(2)
        print("\nAccess Granted")
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
                    edit()
                
                if what_to_do.lower() == "explore":
                    print("exploring")
                    exploring()
                elif what_to_do.lower() == "exit":
                    sys.exit()

    else:
        allowed_access = False
        print("wrong password")
        time.sleep(5)
        sys.exit()





if __name__ == "__main__":
    main()
