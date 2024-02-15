import requests 
from bs4 import BeautifulSoup 

# Making a GET request 

#response = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 
response = requests.get('http://quotes.toscrape.com')

if response.status_code == 200:
    # Parsing the HTML 
    soup = BeautifulSoup(response.content, 'html.parser') 
    # Getting the title tag 
    print(soup.title) 
    print(soup.title.name) 
    print(soup.title.parent.name) 
else:
    print(f"Geting different response code :{response.status_code}")
