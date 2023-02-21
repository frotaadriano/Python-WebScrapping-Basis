import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find an element on the page
heading = soup.find('h1')

# Print the text of the element
print(heading.text)