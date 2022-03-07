import math
from time import sleep
print("""
************************************
Hesap Makinesi Programı

İşlemler:
1: Toplama
2: Çıkarma
3: Çarpma 
4: Bölme
5: Kök alma
6: Faktöriyel
7: 10 tabanında Log alma
8: X tabanında y'nin log alma
9: Çıkış

************************************

""")

while True:
    işlem = int(input("İşlem seçin: "))
    if(işlem==9):
        print("Çıkış Yapılıyor........")
        sleep(1)
        print("Çıkış Yapıldı........")
        break
    elif(işlem == 1):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        ikinci_sayı = int(input("İkinci sayıyı girin: "))
        print("Toplama Yapılıyor")
        sleep(1)
        print("Sonuç: ",ilk_sayı+ikinci_sayı)
    elif (işlem == 2):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        ikinci_sayı = int(input("İkinci sayıyı girin: "))
        print("Çıkarma Yapılıyor")
        sleep(1)
        print("Sonuç: ", ilk_sayı - ikinci_sayı)
    elif (işlem == 3):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        ikinci_sayı = int(input("İkinci sayıyı girin: "))
        print("Çarpma Yapılıyor")
        sleep(1)
        print("Sonuç: ", ilk_sayı * ikinci_sayı)
    elif (işlem == 4):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        ikinci_sayı = int(input("İkinci sayıyı girin: "))
        print("Bölme Yapılıyor")
        sleep(1)
        print("Sonuç: ", ilk_sayı / ikinci_sayı)
    elif (işlem == 5):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        print("Kök alma Yapılıyor")
        sleep(1)
        print("Sonuç: ", math.sqrt(ilk_sayı))
    elif (işlem == 6):
        ilk_sayı = int(input("ilk sayıyı girin"))
        print("Faktöriyel yapılıyor")
        sleep(1)
        print("Sonuç: ",math.factorial(ilk_sayı))
    elif (işlem == 7):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        print("10 Tabanında log Yapılıyor")
        sleep(1)
        print("Sonuç: ", math.log10(ilk_sayı))
    elif (işlem == 8):
        ilk_sayı = int(input("İlk sayıyı girin: "))
        ikinci_sayı = int(input("İkinci sayıyı girin: "))
        print("log Yapılıyor")
        sleep(1)
        print("Sonuç: ",math.log(ikinci_sayı,ilk_sayı))
    else:
        print("Geçersiz işlem....")
