"""
Level 1 Task 5: Palindrome Checker
Check whether a given word is a palindrome.
"""

def is_palindrome(text):
    """Return True if the text is a palindrome."""
    cleaned = text.lower()
    return cleaned == cleaned[::-1]


def main():
    word = input("Enter a word: ")

    if is_palindrome(word):
        print("It is a palindrome.")
    else:
        print("Not a palindrome.")


if __name__ == "__main__":
    main()