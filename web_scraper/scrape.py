import requests
from bs4 import BeautifulSoup

URL  = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
req = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

