"""
This one is from the course video
"""

from game_data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user guess and the follower counts of each accounts and compare"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("\n VS \n")
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    users_guess = input("Who has more followers? 'A' or 'B': ").lower()
    print("\n"* 30)

    # Check if the user is correct.
    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(users_guess, a_follower_count, b_follower_count)

    # - Use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You're Right! Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score}")
