print("problem 3--------------")
import requests
from bs4 import BeautifulSoup

url = "https://kur.doviz.com"
response = requests.get(url)
html_icerik = response.content
soup = BeautifulSoup(html_icerik,"html.parser")

birim = soup.find_all("span",{"class":"name"})
deger = soup.find_all("span",{"class":"value"})

liste_birim = []
liste_deger = []

for i in birim:
    liste_birim.append(i.text)
for j in deger:
    liste_deger.append((j.text).replace(",","."))

print(liste_deger)
print(liste_birim)

print("""***********
DÖVİZ UYGULAMASI

İşlemler:
1)Anlık Borsa:
2)EURO ---> TÜRK LİRASI
3)TÜRK LİRASI ---> EURO
4)DOLAR ---> TÜRK LİRASI
5)TÜRK LİRASI ---> DOLAR
6)EURO ---> DOLAR
7)DOLAR ---> EURO
8)Çıkış 

************""")

while True:
    işlem = input("Bir işlem seçin:")
    if işlem == "1":
        for i, j in zip(birim, deger):
            print(i.text, ":", j.text)
    elif işlem == "2":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar * float(liste_deger[2])
        print("{} Euro, {} Türk Lirasına eşittir.".format(miktar, sonuç))
    elif işlem == "3":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar / float(liste_deger[2])
        print("{} Türk Lirası , {} Euro'ya eşittir.".format(miktar, sonuç))
    elif işlem == "4":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar * float(liste_deger[1])
        print("{} Dolar, {} Türk Lirasına eşittir.".format(miktar, sonuç))
    elif işlem == "5":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar / float(liste_deger[1])
        print("{} Türk Lirası , {} Dolar'a eşittir.".format(miktar, sonuç))
    elif işlem == "6":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar * float(liste_deger[2]) / float(liste_deger[1])
        print("{} Euro, {} Dolar'a eşittir.".format(miktar, sonuç))
    elif işlem == "7":
        miktar = float(input("Dönüştürülecek miktarı giriniz:"))
        sonuç = miktar * float(liste_deger[1]) / float(liste_deger[2])
        print("{} Dolar, {} Euro'ya eşittir.".format(miktar, sonuç))
    elif işlem == "8":
        print("Çıkış yapıldı.")
        break
    else:
        print("Lütfen geçerli bir işlem girin.")
