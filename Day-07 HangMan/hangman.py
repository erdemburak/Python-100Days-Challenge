import random
import hangman_ascii_art

word_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", 
         "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", 
         "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", 
         "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven",
         "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider",
         "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf", 
         "wombat", "zebra"]


lives = 0

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
placeholder = ""
for letter in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = [] 

while game_over == False:
    print(f"**************** {6-lives}/6 LIVES LEFT ***************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 6:
            game_over = True
            print(f"**************** IT WAS {chosen_word}! YOU LOSE ****************")

    if "_" not in display:
        game_over = True
        print("**************** YOU WIN ****************")

    print(hangman_ascii_art.HANGMANPICS[lives])