# ex2

import random


def number_game(guess):
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Check if the guess matches the random number
    if guess == random_number:
        print("Congratulations!")
    else:
        print("Sorry, your guess did not match the number. Try again.")


number_game(4)
