

def asal(sayı):
    if(sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı%2==0):
                return False
        return True

while True:
    sayı = input("Sayı: ")
    if(sayı=="q"):
        break
    else:
        sayı = int(sayı)

        if(asal(sayı)):
            print(sayı, "Asal sayı")
        else:
            print(sayı, "Asal sayı değil")
