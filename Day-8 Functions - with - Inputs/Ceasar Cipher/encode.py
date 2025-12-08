"""
Docstring for Day-8 Functions - with - Inputs.Ceasar Cipher.encode
"""
def encrypt(char_set_for_cryption):
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    encrypted_text_list = []
    char_set_length = len(char_set_for_cryption)
    

    for letter in text:
        letter_index = char_set_for_cryption.index(letter)

        if letter_index + shift < char_set_length:
            encrypted_letter_index = letter_index + shift
            encrypted_text_list.append(char_set_for_cryption[encrypted_letter_index])
        elif letter_index + shift >= char_set_length:
            encrypted_letter_index = shift - (char_set_length - letter_index)
            encrypted_text_list.append(char_set_for_cryption[encrypted_letter_index])

    # print(encrypted_text_list)
    
    encrypted_text = ""
    for letter in encrypted_text_list:
        encrypted_text += letter
    print("Encrypted text = " +encrypted_text)