"""
Level 2 Task 2: Number Guesser
User chooses a range and guesses the random number.
"""

import random


def number_guesser():
    print("Number Guessing Game")

    low = int(input("Enter the minimum number: "))
    high = int(input("Enter the maximum number: "))

    number = random.randint(low, high)

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
    number_guesser()


if __name__ == "__main__":
    main()