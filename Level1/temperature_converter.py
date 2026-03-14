"""
Level 1 Task 2: Temperature Converter
Convert between Celsius and Fahrenheit.
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def main():
    print("Temperature Converter")

    value = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F): ").upper()

    if unit == "C":
        result = celsius_to_fahrenheit(value)
        print("Temperature in Fahrenheit:", result)

    elif unit == "F":
        result = fahrenheit_to_celsius(value)
        print("Temperature in Celsius:", result)

    else:
        print("Invalid unit entered")


if __name__ == "__main__":
    main()