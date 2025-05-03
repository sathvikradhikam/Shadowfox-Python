import requests
from bs4 import BeautifulSoup

# Target website
url = "https://quotes.toscrape.com"

# Send a request to the website
response = requests.get(url)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote containers
quotes = soup.find_all('div', class_='quote')

# Extract and print each quote and its author
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" - {author}')