def greet():
    print("------- Welcome to Greet Function -------")
    users_name = input("What is your name? ")
    print(f"Hello {users_name}")

greet()

# ---- same function with inputs ----

def greet_with_input (name_input):
    print("------- Welcome to Greet With Input Function -------")
    print(f"Hello {name_input}")
    
greet_with_input("Burak")

"""
    user_name = "Burak"
    parameter = argument

    Parameter = name of the data that been passed in
    Argument = the actual value of the data
"""

def greet_with_location(name, location):
    print(f"Welcome {name} from {location}")

greet_with_location(location="Burak", name="Ankara") # Parametreleri tanımladığımız durumda sıraya uymak zorunda değiliz.
greet_with_location(name="Burak", location="Ankara")