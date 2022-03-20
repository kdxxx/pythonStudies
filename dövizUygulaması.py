"""This code is not suitable for this website since it became paid."""

import sys
import requests

url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci döviz: ")
ikinci_doviz = input("İkinci döviz: ")
miktar = float(input("miktar: "))

response = requests.get(url+birinci_doviz)
json_verisi = response.json()

try:
    print(json_verisi["rates"][ikinci_doviz]*miktar)
except KeyError:
    sys.stderr.write("yanlış para birimi")
    sys.stderr.flush()
