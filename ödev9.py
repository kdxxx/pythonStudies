print("problem 1")
def alan_hesapla(demet):
    return demet[0] * demet[1]
liste = [(3,4),(42,2),(13,2)]
print(list(map(alan_hesapla,liste)))


print("problem 2")
def üçgen_mi(demet):
    if(abs(demet[0]+demet[1])>demet[2] and abs(demet[0]+demet[2])>demet[1] and abs(demet[1]+demet[2])>demet[0]):
        return True
    else:
        return False
liste2 = [(1,2,3),(3,4,5),(3,10,7)]
print(list(filter(üçgen_mi,liste2)))

print("problem 3")
from functools import reduce
liste3 =   [1,2,3,4,5,6,7,8,9,10]
filtre = list(filter(lambda x: x%2 == 0,liste3))
print(reduce(lambda x,y: x+y,filtre))


print("problem 4")
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)
