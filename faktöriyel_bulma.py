print("""
***********

Faktöriyel Bulma

Çıkmak için q tuşuna basın
***********
""")

while True:
    sayı = input("Sayı: ")
    if(sayı =="q"):
        print("program sonlandırıldı")
        break
    else:
        sayı = int(sayı)

        faktöriyel  = 1
        for i in range(2,sayı+1):
            faktöriyel *= i
        print("Faktöriyel ", faktöriyel)
