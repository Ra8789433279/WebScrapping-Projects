import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('http://quotes.toscrape.com')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the page
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Print the quotes and authors
    for quote, author in zip(quotes, authors):
        print(f'Quote: {quote.text}')
        print(f'Author: {author.text}')
        print('---')
else:
    print(f'Error: Unable to fetch the page (Status code: {response.status_code})')
