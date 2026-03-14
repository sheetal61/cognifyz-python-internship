"""
Level 2 Task 3: Password Strength Checker
Checks whether a password is weak, medium, or strong.
"""

import re


def check_password_strength(password):

    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(uppercase), bool(lowercase), bool(digit), bool(special)])

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"


def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print("Password Strength:", strength)


if __name__ == "__main__":
    main()