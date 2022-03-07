
print("problem 1")
def mukemmelSayı(sayı):
    toplam = 0
    for i in range(1,sayı):
        if(sayı % i == 0):
            toplam += i
    return toplam == sayı

for i in range(1,1001):
    if(mukemmelSayı(i)):
        print("mükemmel sayı:",i)


print("problem 2")
def ebobBul(sayı1,sayı2):
    çarpan = 1
    ebob = 1
    while (çarpan<=sayı1 and çarpan<=sayı2):
        if(not (sayı1 % çarpan) and not(sayı2 %çarpan)):
            ebob = çarpan
        çarpan += 1
    return ebob
sayı1 = int(input("sayı1: "))
sayı2 = int(input("sayı2: "))

print("ebob: ",ebobBul(sayı1,sayı2))


print("problem 3")
def ekokBul(sayı1,sayı2):
    i = 2
    ekok = 1
    while True:
        if(sayı1 %i == 0 and sayı2 % i == 0):
            ekok *= i
            sayı1 //=i
            sayı2 //=i
        elif(sayı1 %i == 0 and sayı2 % i != 0):
            ekok *=i
            sayı1 //= i
        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i
            sayı2 //= i
        else:
            i += 1
        if(sayı1 == 1 and sayı2 == 1):
            break
    return  ekok

sayı3 = int(input("sayı3"))
sayı4 = int(input("sayı4"))

print("ekok",ekokBul(sayı3,sayı4))


print("problem 4")

birler = ["","bir","iki",",üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def oku(sayı):
    birincibas = sayı % 10
    ikincibas = sayı // 10

    return onlar[ikincibas] + " "+birler[birincibas]

sayı5  = int(input("sayı:"))
print(oku(sayı5))


print("problem 5")
def pisagorBulma():
    pisagor = list()
    for kenar1 in range(1,101):
        for kenar2 in range(1,101):
            hipotenüs = (kenar1 **2 +kenar2**2)**0.5

            if(hipotenüs == int(hipotenüs)):
                pisagor.append((kenar1,kenar2,int(hipotenüs)))
    return pisagor

for i in pisagorBulma():
    print(i)
