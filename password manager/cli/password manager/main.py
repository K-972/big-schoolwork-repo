import time
import hashlib
import sys


def edit():
    pass


def exploring():
    pass


password = 'e5dfed079b2bb64718bb391046739a3e342145baa274d5290f4099566531c4ee'
# hashed_password = hashlib.sha256(str.encode(pasword)).hexdigest()

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
    if password_input == password:
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
        print("wrong password you sussy imposter.")
        time.sleep(5)
        sys.exit()





if __name__ == "__main__":
    main()
