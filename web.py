from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/Valorant"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')

# Extract and print all h1 titles
titles = soup.find_all('h1')
for title in titles:
    print(title.text)

# Pretty print the entire HTML structure of the page (if needed)
# print(soup.prettify())

# Extract and print all links (anchor tags <a>)
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
