print("""
******************
Hesap Makinesi Programı

İşlemler:
1: Toplama
2: Çıkarma
3: Çarpma 
4: Bölme

******************

""")

a = int(input("İlk sayı: "))
b = int(input("İkinci sayı: "))

işlem = int(input("İşlem: "))

if(işlem ==1):
    print(" {} + {}  = {} ".format(a,b,a+b))
elif(işlem ==2):
    print(" {} - {}  = {} ".format(a,b,a-b))
elif(işlem ==3):
    print(" {} * {}  = {} ".format(a,b,a*b))
elif(işlem ==4):
    print(" {} / {}  = {} ".format(a,b,a/b))
else:
    print("geçersiz işlem")
