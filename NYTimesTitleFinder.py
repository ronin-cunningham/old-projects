
import requests
from bs4 import BeautifulSoup

url = ("https://www.nytimes.com")

q = requests.get(url)

w = BeautifulSoup(q.text, "lxml")



for x in w.find_all(class_="story-heading"):
        print (x.text.strip())
