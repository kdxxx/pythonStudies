import requests
from bs4 import BeautifulSoup

url = "http://www.imbd.com/chart/top"

response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

a = float(input("Rating girin: "))

baslıklar = soup.find_all("td",{"titleColumn"})
ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})

for baslık, rating in(baslıklar,ratingler):
    baslık = baslık.text
    rating = rating.text

    baslık = baslık.strip()
    baslık = baslık.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if(float(rating) > a):
        print("Film ismi: {} Film rating: {} ".format(baslık,rating))
