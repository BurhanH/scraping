# libs

from urllib.request import urlopen
from bs4 import BeautifulSoup

# target site
q_page = 'https://phptravels.com/'

page = urlopen(q_page)

soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())  # Content checking

demo_section = soup.find('a', attrs={'class': 'text-primary'})

# print(dir(demo_section)) # An object attributes check

if demo_section:
    text = demo_section.text.strip()
    print("text: ", text)
