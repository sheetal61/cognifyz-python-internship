"""
Level 2 Task 1: Guessing Game
The program generates a random number between 1 and 100.
The user must guess the number.
"""

import random


def guessing_game():
    number = random.randint(1, 100)

    print("Guess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print("Correct! You guessed the number.")
            break


def main():
    guessing_game()


if __name__ == "__main__":
    main()