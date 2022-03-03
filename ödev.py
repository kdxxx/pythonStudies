
print("problem 1: çarpım bulma")
a = int(input("ilk sayıyı gir: "))
b = int(input("ikinci sayıyı gir: "))
c = int(input("üçüncü sayıyı gir: "))
print("sayıların çarpımı:{} ".format(a*b*c))
print("{} x {} x {} = {} dir".format(a,b,c,format(a*b*c)))


print("problem 2: beden kitle indeksi hesaplama ")
boy = float(input("boyunu gir: "))
kilo = int(input("kilonu gir: "))
bedenKitleİndeksi  = kilo/(boy**2)
print("beden kitle indeksin: ", bedenKitleİndeksi)


print("problem 3: araç yakıt hesaplama ")
kilometrede = float(input("kilometrede ne kadar yakıyor: "))
kilometre = int(input("kaç kilometre yaptın: "))
neKadar = kilometrede*kilometre
print("ödemen gereken tutar: ",neKadar)
print("Tutar: {} tl".format(kilometrede * kilometre))



print("problem 4: kullanıcı bilgileri ")
ad = input("adın: ")
soyad = input("soyadın: ")
numara = input("numaran: ")
bilgiler = [ad,soyad,numara]
print("Bilgilerin:\nad {}\nsoyad {}\nnumara {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))



print("problem 5: değişiklik")
x = int(input("ilk sayıyı gir "))
y = int(input("ikinci sayıyı gir "))
print("ilk sayı ",y,"ikinci sayı ",x)


print("problem 6: hipotenüs")
a = int(input("a kenarını gir "))
b = int(input("b kenarını gir "))
print("hipotenüs: {}".format(int((a**2+b**2)**0.5)))
