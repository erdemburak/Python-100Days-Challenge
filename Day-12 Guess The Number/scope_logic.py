game_level = 4
enemies_list = ["Skeleton", "Zombie", "Alien"]
enemies = "Zombie"
enemies_number = 3
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
    
#     print(new_enemy)

# create_enemy()


# If you modify a variable in global scope with function it will be only modified in that function

def increase_enemies():
    enemies = "Skeleton"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def increase_enemies_number(enemy):
    # global enemies_number #to modify a number we need to specify it as global variable in the function
    # enemies_number += 1

    enemy += 1
    print(f"enemies inside function: {enemy}")

increase_enemies_number(enemies_number)
print(f"enemies outside function: {enemies_number}")
