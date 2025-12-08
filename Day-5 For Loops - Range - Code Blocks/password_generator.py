import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letter would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

# -------- Easy level ----------
# password = ""

# for char in range(0, number_of_letters):
#     password += random.choice(letters)
# for char in range(0, number_of_symbols):
#     password += random.choice(symbols)
# for char in range(0, number_of_numbers):
#     password += random.choice(numbers)

# ----------- Hard level -----------
password_list = []

for char in range(0, number_of_letters):
    password_list.append(random.choice(letters))
for char in range(0, number_of_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, number_of_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

strong_password = ""

# -- Aşağıda for döngüsü ile rastgele char alarak karıştırdık
# for char in range(0, len(password_list)):
#     choice = random.choice(password_list)
#     strong_password += choice
#     password_list.remove(choice)

# -- shuffle methoduyla da daha kısa şekilde yapabiliyormuşuz 

random.shuffle(password_list)
for char in password_list:
    strong_password += char

print(strong_password)