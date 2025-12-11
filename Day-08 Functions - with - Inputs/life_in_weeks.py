"""
Docstring for Day-8 Functions - with - Inputs.life_in_weeks
Bu kod temel fonksiyon kullanımıyla ilgili.
"""

def life_in_weeks():
    print("---- How Many Weeks Left? ----")
    age = int(input("How old are you?"))
    years_left = 90 - age
    weeks_left = 52 * years_left
    print(f"You have {weeks_left} weeks left.")

life_in_weeks()
