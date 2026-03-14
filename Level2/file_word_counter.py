"""
Level 2 Task 5: File Word Counter
Counts occurrences of each word in a text file.
"""

def count_words(filename):

    word_count = {}

    with open(filename, "r") as file:
        text = file.read().lower()
        words = text.split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for word in sorted(word_count):
        print(word, ":", word_count[word])


def main():
    filename = input("Enter file name: ")
    count_words(filename)


if __name__ == "__main__":
    main()