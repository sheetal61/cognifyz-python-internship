"""
Level 1 Task 1: String Reversal
Reverse a user-provided string.
"""

def reverse_string(text):
    """Return reversed version of the input string."""
    return text[::-1]


def main():
    user_input = input("Enter a string: ")
    reversed_text = reverse_string(user_input)
    print("Reversed string:", reversed_text)


if __name__ == "__main__":
    main()