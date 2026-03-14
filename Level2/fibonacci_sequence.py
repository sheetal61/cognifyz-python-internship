"""
Level 2 Task 4: Fibonacci Sequence
Generate Fibonacci numbers up to a given number of terms.
"""

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def main():
    terms = int(input("Enter number of terms: "))
    fibonacci(terms)


if __name__ == "__main__":
    main()