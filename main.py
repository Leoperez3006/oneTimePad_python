#Jose Leonardo Perez Gonzalez
#A01424133

# #algoritmo one time pad
import random


text = input("introduce el texto a cifrar: ").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def encrypt(text):
    otp = "".join(random.sample(alphabet, len(alphabet)))
    res = ""

    for char in text:
        if alphabet.find(char) == -1:
            res += char
        else: 
            res += otp[alphabet.find(char)]

    return otp, res 


encryptedText = encrypt(text) 

print("OTP key: " + encryptedText[0])
print("Encrypted: " + encryptedText[1])

