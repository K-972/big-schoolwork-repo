# Fernet module is imported from the
# cryptography package
#from cryptography.fernet import Fernet
import time
import hashlib
import sys
from cryptography.fernet import Fernet

# key is generated
#key = Fernet.generate_key()

# value of key is assigned to a variable
#f = Fernet(key)

# the plaintext is converted to ciphertext
#token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
#print(token)

# decrypting the ciphertext
#d = f.decrypt(token)

# display the plaintext and the decode() method
# converts it from byte to string
#print(d.decode())

#key = Fernet.generate_key()


#password_input = input("\nPlease enter password >> ")
#password_input = hashlib.sha256(str.encode(password_input)).hexdigest()
#print(password_input)
key = b'l3vZ2XL6fsl2UTCYeq-00k162exuUIrBC3_y96xFN5M='

def encrypt(thing_to_encrypt, key):
    f = Fernet(key)
    cipher_text = f.encrypt(thing_to_encrypt.encode())
    return cipher_text
username = input("Enter username >> ")
encrypted_username = encrypt(username, key)
print(encrypted_username)