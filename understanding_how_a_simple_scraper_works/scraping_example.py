import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.example.com/')
soup = BeautifulSoup(page.content, 'html.parser')

print(page.content)
print(soup.find('p').string)
print(soup.select_one('p a').attrs['href'])