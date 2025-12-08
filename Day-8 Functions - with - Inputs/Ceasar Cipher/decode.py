"""
Docstring for Day-8 Functions - with - Inputs.Ceasar Cipher.decode
"""
def decrypt(char_set_for_decryption):
    crypted_text = input("Type your crypted message: ").lower()
    shift = int(input("Type the shift number: "))
    
    decrypted_text = ""
    char_set_length = len(char_set_for_decryption)

    for letter in crypted_text:
        letter_index = char_set_for_decryption.index(letter)

        if (letter_index - shift) >= 0:
            decrypted_letter_index = letter_index - shift
            decrypted_text += char_set_for_decryption[decrypted_letter_index]
        elif (letter_index - shift) < 0:
            decrypted_letter_index = char_set_length - (shift - letter_index)
            decrypted_text += char_set_for_decryption[decrypted_letter_index]

    print("Decrypted text: " + decrypted_text)