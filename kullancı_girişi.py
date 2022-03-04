print("""
************
kullanıcı girişi 

************
""")

def_kullanıcı_adı = "kdxxx"
def_parola = "1234"


kullanıcı_adı = input("kullanıcı adı ")
parola = input("parola ")

if(kullanıcı_adı == def_kullanıcı_adı and def_parola != parola):
    print("parola hatalı")
elif(kullanıcı_adı != def_kullanıcı_adı and def_parola == parola):
    print("kullanıcı adı hatalı")
elif(kullanıcı_adı != def_kullanıcı_adı and def_parola != parola):
    print("kullanıcı adı ve parola hatalı")
else:
    print("giriş başarılı")



