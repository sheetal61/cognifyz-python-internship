"""
Level 3 Task 2: Data Visualization Tool
Visualizes sales data from a CSV file.
"""

import pandas as pd
import matplotlib.pyplot as plt


def visualize_sales(file):

    data = pd.read_csv(file)

    print("Dataset Preview:")
    print(data)

    plt.figure(figsize=(8,5))

    plt.plot(data["Month"], data["Sales"], marker="o")

    plt.title("Monthly Sales Data")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.show()


def main():

    file = input("Enter CSV file name: ")
    visualize_sales(file)


if __name__ == "__main__":
    main()