"""
Level 3 Task 1: Web Scraper
Scrapes book titles, prices, and ratings from books.toscrape.com
"""

import requests
from bs4 import BeautifulSoup


def scrape_books():

    url = "https://books.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("Books on the page:\n")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Rating: {rating}")
        print("-" * 40)


def main():
    scrape_books()


if __name__ == "__main__":
    main()