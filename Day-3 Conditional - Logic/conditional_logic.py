"""
    if condition:
     do this
    else:  
     do this
"""

water_level = 50

if water_level >80:
    print("Drain water")
else:
    print("Continue")

print("\n -------------------------------------------- \n")

print("Welcome to the RollerCoaster")
height = float(input("What is your height(cm): "))
bill = 0

if height >= 120:
    age = int(input("You can ride but what is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")

    if wants_photo == "y":
        bill += 3 # add 3 dolar to their bill
    print(f"Your total bill is {bill}")
else:
    print("You can't ride")

print("\n -------------------------------------------- \n")

number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")