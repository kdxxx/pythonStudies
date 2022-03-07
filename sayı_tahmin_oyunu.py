import random
import time

print("""
*************************

SAYI TAHMİN OYUNU

*************************

1 ile 40 arasında sayıyı tahmin edin
""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmin girin"))

    if(tahmin<rastgele_sayı):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(1)
        print("Daha yüksek tahmin girin")

        tahmin_hakkı -= 1
    elif(tahmin>rastgele_sayı):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(1)
        print("Daha düşük tahmin girin")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(1)
        print("Tebriklerrr")
        break
    if(tahmin_hakkı == 0):
        print("Tahmin hakkın bitti.....")
        time.sleep(1)
        print("Sayı",rastgele_sayı)
        break
