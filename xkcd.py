import requests as req
from bs4 import BeautifulSoup
import random as rand

xkcd_base_url = "http://xkcd.com/"
archive_url = "archive"

r = req.get(xkcd_base_url + archive_url)
soup = BeautifulSoup(r.text, 'html.parser')
max_article_number = int(soup.find('div', id='middleContainer').find('a')['href'].replace('/', '').encode())
num = rand.randint(1, max_article_number)
print xkcd_base_url + str(num)
