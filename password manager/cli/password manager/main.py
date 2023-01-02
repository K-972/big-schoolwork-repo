from cryptography.fernet import Fernet
import time
key = Fernet.generate_key()
cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
PASSWORD = b'gAAAAABjsxMwxBTFdQ9_tFMYv-Ko1Ja7t5afvMiJBehRMqJyp-OapyRbP2IPBsboI-rZilgXhcIIpWWXq1Bwo732st7celJvX52Ahxten8lbF0LMzw7ND9Q9r2UFPeTyJjOp9Dr0mqhd'
password_decrypted = cipher_suite.decrypt(PASSWORD)

#################
### main menu ###
#################

def main_menu():
    print("----------------------------------------")
    print("\n    Welcome to K9's password manager.")
    print("                     Made by K972.\n")
    print("----------------------------------------")

############
### main ###
############

def main():
    main_menu()
    password_input = input("\n\n\nPlease enter password >> ")
    if password_input == password_decrypted:
        allowed_access = True
        while allowed_access:
            print("login sucessful")
    else:
        allowed_access = False
        print("wrong password you sussy imposter.")
        time.sleep(5)
        quit()






if __name__ == "__main__":
    main()
    