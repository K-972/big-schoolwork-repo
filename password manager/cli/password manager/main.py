import time
import hashlib
from hashlib import sha256
import sys


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
    password_input = input("\n\n\nPlease enter password >> ")
    password_input = hashlib.sha256(str.encode(password_input)).hexdigest()
    if password_input == password:
        allowed_access = True
        while allowed_access:
            print("login sucessful")
    else:
        allowed_access = False
        print("wrong password you sussy imposter.")
        time.sleep(5)
        sys.exit()





if __name__ == "__main__":
    main()
