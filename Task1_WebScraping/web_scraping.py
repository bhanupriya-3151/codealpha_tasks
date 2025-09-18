import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Get the website content
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all quotes
quotes = soup.find_all("div", class_="quote")

# Step 3: Save to CSV
with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        writer.writerow([text, author])

print("✅ Scraping complete! quotes.csv created.")
