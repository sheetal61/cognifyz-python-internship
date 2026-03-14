"""
Level 1 Task 4: Basic Calculator
Perform arithmetic operations based on user input.
"""

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return None


def main():
    print("Simple Calculator")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+ - * / %): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, num2, operator)

    if result is None:
        print("Invalid operator")
    else:
        print("Result:", result)


if __name__ == "__main__":
    main()