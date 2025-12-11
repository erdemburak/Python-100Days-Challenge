"""
Docstring for Day-8 Functions - with - Inputs.Ceasar Cipher.caesar_cipher
Bu uygulamada kullanıcının girdiği kelimeyi yine kullanıcının girdiği shift ile birlikte şifreliyoruz.
Aynı şekilde şifreli kodu da kullanıcının metnine çeviriyoruz.
"""
from encode import encrypt
from decode import decrypt

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

if direction == "encode":
    encrypt(alphabet)
elif direction == "decode":
    decrypt(alphabet)
else: 
    print("Wrong input.")