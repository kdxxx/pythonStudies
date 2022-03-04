print("""
***********************
Kullanıcı Girişi Programı
***********************
""")

def_kullanıcı_adı = "kdxxx"
def_parola = "1234"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı ")
    parola = input("Parola ")

    if(kullanıcı_adı != def_kullanıcı_adı and parola == def_parola):
        print("Kullanıcı adı hatalı")
        giriş_hakkı -=1
    elif(kullanıcı_adı == def_kullanıcı_adı and parola != def_parola):
        print("Parola hatalı")
        giriş_hakkı -=1
    elif(kullanıcı_adı != def_kullanıcı_adı and parola != def_parola):
        print("hatalı giriş")
        giriş_hakkı -=1
    else:
        print("sisteme giriş yapıldı")
        break
    if(giriş_hakkı == 0):
        print("giriş hakkı bitti")
        break
