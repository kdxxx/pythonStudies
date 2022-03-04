print("""**************
ATM  makinesine hoşgeldiniz

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

**************
""")

bakiye = 1000
while True:
    işlem = input("İşlemi seçiniz: ")

    if(işlem =="q"):
        print("yine bekleriz")
        break
    elif(işlem =="1"):
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif(işlem =="2"):
        miktar = int(input("Miktarı girin: "))
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Miktarı girin: "))
        if(miktar>bakiye):
            print("yetersiz bakiye")
            continue
        bakiye -= miktar
    else:
        print("geçersiz işlem")
