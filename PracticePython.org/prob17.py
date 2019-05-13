"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""
from bs4 import BeautifulSoup
import requests

# Get the HTML code of the website
url = 'https://www.google.com/'
r = requests.get(url)
htmlVersion = r.text

# Parse the code for titles
soup = BeautifulSoup(htmlVersion, features="html.parser")
title = soup.find('span', 'css-truncate css-truncate-target').title
print(title)

# Print the titles

# IN PROGRESS
