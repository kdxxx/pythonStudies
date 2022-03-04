print("problem 1")

a = int(input("sayıyı girin "))
i = 1
toplam = 0
while(i<a):
    if(a%i==0):
        toplam += i
    i +=1

if(toplam == a):
    print(a,"mükemmel sayı")
else:
    print(a,"mükemmel sayı değil")


print("problem 2")

sayı2= input("sayıyı girin: ")
basamak_sayısı = len(sayı2)
sayı2 = int(sayı2)
basamak = 0
toplam = 0

gecici_sayı = sayı2
while(gecici_sayı>0):
    basamak = gecici_sayı%10
    toplam += basamak ** basamak_sayısı
    gecici_sayı  //= 10

if(toplam == sayı2):
    print(sayı2, "bir Armstrong sayısı")
else:
    print(sayı2, "bir Armstrong sayısı değil")


print("problem 3")
for i in range(1,11):
    print("-------------------------------")
    for j in range(1,11):
        print("{} * {} = {}".format(i,j,i*j))


print("problem 4")
toplam = 0
while True:
    sayı3 = input("Sayıyı girin ")
    if(sayı3 =="q"):
        break
    sayı3 = int(sayı3)
    toplam += sayı3
print("Sayıların toplamı: ",toplam)


print("problem 5")
for i in range(1,101):
    if(i%3!=0):
        continue
    print(i)



print("problem 6")
liste = [x for x in range(1,101) if x%2 == 0]
print(liste)
