"""
Docstring for Day-14 Higher Lower Game.guess_the_higher_follower
This is my version of the game before i watch the course video.
"""

from game_data import data
import random

number_of_data = len(data)

def pick_random_data():
    random_data_index = random.randint(0,(number_of_data - 1))
    picked_data = data.pop(random_data_index)
    return picked_data

compare_data_a = pick_random_data()
score = 0
highest_score = 0


while number_of_data > 0:
    print("---------------------- Who Has More Followers -----------------------")
    print(f"Current Score = {score}")
    print(f"Compare A: {compare_data_a["name"]}, a {compare_data_a["description"]}, from {compare_data_a["country"]}")
    print("\n VS \n")
    compare_data_b = pick_random_data()
    print(f"Against B: {compare_data_b["name"]}, a {compare_data_b["description"]}, from {compare_data_b["country"]}")
    users_guess = input("Who has more followers? 'A' or 'B': ")
    print("\n"* 30)

    if users_guess == "A":
        if compare_data_a["follower_count"] > compare_data_b["follower_count"]:
            print("True")
            score += 1
        elif compare_data_a["follower_count"] < compare_data_b["follower_count"]:
            print(f"Wrong - {compare_data_b["name"]} has more followers!!!")
            compare_data_a = compare_data_b
            if score > highest_score:
                highest_score = score
            score = 0
    elif users_guess == "B":
        if compare_data_a["follower_count"] < compare_data_b["follower_count"]:
            print("True")
            compare_data_a = compare_data_b
            score += 1
        elif compare_data_a["follower_count"] > compare_data_b["follower_count"]:
            print(f"Wrong - {compare_data_a["name"]} has more followers!!!")
            compare_data_a = compare_data_b
            if score > highest_score:
                highest_score = score
            score = 0

    number_of_data = len(data)

    if number_of_data == 0:
        if score > highest_score:
            highest_score = score
        print(f"Highest score = {highest_score}")
        print("------ Game Over ------")