"""
Level 1 Task 3: Email Validator
Validate whether a given email address is in correct format.
"""

import re


def is_valid_email(email):
    """Check if email matches basic email pattern."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def main():
    email = input("Enter an email address: ")

    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")


if __name__ == "__main__":
    main()