print("Problem 1: Beden Kitle İndeksi")

boy = float(input("Boyun: "))
kilo = int(input("Kilon: "))
bedenKitleİNdeksi = kilo / (boy ** 2)

if (bedenKitleİNdeksi < 18.5):
    print("zayıf")
elif (bedenKitleİNdeksi >= 18.5 and bedenKitleİNdeksi < 25):
    print("Normal")
elif (bedenKitleİNdeksi >= 25 and bedenKitleİNdeksi < 30):
    print("fazla kilolu")
elif (bedenKitleİNdeksi >= 30):
    print("obez")

print("problem 2: sıralama")

a = int(input("ilk sayı: "))
b = int(input("ikinci sayı: "))
c = int(input("üçüncü sayı: "))

if (a > b and a > c):
    print("en büyük ", a)
elif (b > a and b > c):
    print("en büyük ", b)
else:
    print("en büyük ", c)

print("problem 3: harf notu hesaplama ")
vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
vize3 = int(input("Vize 3: "))

ortalama = vize1*0.3 + vize2*0.3 + vize3*0.4

if(ortalama>=90):
    print("AA")
elif(ortalama>=85):
    print("BA")
elif (ortalama >= 80):
    print("BB")
elif(ortalama>=75):
    print("CB")
elif(ortalama>=70):
    print("CC")
elif(ortalama>=65):
    print("DC")
elif(ortalama>=60):
    print("DD")
elif(ortalama>=55):
    print("FD")
else:
    print("FF")


print("Problem 4")

şekil = input("şekli girin")
if(şekil == "Dörtgen"):

    kenar1 = int(input("kenar 1: "))
    kenar2 = int(input("kenar 2: "))
    kenar3 = int(input("kenar 3: "))
    kenar4 = int(input("kenar 4: "))

    if(kenar1 == kenar2 == kenar3 == kenar4):
        print("kare")
    else:
        print("dikdörtgen")


elif(şekil =="Üçgen"):

    kenar1 = int(input("kenar 1: "))
    kenar2 = int(input("kenar 2: "))
    kenar3 = int(input("kenar 3: "))


    if(abs(kenar1-kenar2)<=kenar3 <= abs(kenar1 +kenar2)):
        if (kenar1 == kenar2 == kenar3):
            print("eşkenar üçgen")
        elif (kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3):
            print("ikizkenar üçgen")
        else:
            print("çeşitkenar üçgen")

    else:
        print("Üçgen belirtmiyor")

