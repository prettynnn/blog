from bs4 import BeautifulSoup
import requests

url = "https://realpython.com/"

online = requests.get(url)
print(online.status_code)

filterNews = []
allNews = []

check = BeautifulSoup(online.text, "html.parser")

allNews = check.find_all('a', class_="btn stretched-link")
   
for data in allNews:
    print(data.get_text())
        
