import random

print("--------- Guess The Number ---------")

difficulty = input("Type 'easy' or 'hard'").lower()
random_number = random.randint(1,101)
print("I picked a number between 1-100")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts > 0:
    users_guess_str = input(f"Try to guess you have {attempts} attempts: ")
    users_guess = int(users_guess_str)

    if users_guess == random_number:
        print("Congratulations. You Guess is Currect")
        attempts = 0
    elif (users_guess - random_number) > 25:
        print("Too High")
    elif (users_guess - random_number) >= 1:
        print("High")
    elif (random_number - users_guess) > 25:
        print("Too low")
    elif (random_number - users_guess) >= 1:
        print("Low")
    attempts -= 1
    if attempts == 0:
        print(f"You failed the number was: {random_number}")

