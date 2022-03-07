import random
import time

class Kumanda():
    def __init__(self, tv_durum ="Kapalı",ses = 0, kanal_listesi = ["trt"],kanal = "trt"):
        self.tv_durum = tv_durum
        self.ses = ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "açık"):
            print("Televizyon açık")

        else:
            print("televizyon açılıyor")
            self.tv_durum = "açık"

    def tv_kapat(self):
        if (self.tv_durum == "kapalı"):
            print("Televizyon kapalı")

        else:
            print("televizyon kapanıyor")
            self.tv_durum = "kapalı"


    def ses_açma(self):
        while True:
            cevap = input("sesi azalt '<'\nsesi artır 'n'\n çıkış: çıkış")
            if (cevap == '<'):
                if (self.ses != 0):
                    self.ses -= 1
                    print("ses: ", self.ses)
            elif (cevap == '>'):
                if (self.ses != 25):
                    self.ses += 1
                    print("ses: ", self.ses)
            else:
                print("ses değişti", self.ses)
                break



    def kanal_ekle(self,isim):
        print("kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(isim)
        print("kanal eklendi.....")


    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şu anki kanal,",self.kanal)


    def __len__(self):
        return  len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu {}\nTv ses {}\nKanal Listesi {}\nŞu anki kanal {}\n".format(self.tv_durum,self.ses,self.kanal_listesi,self.kanal)



kumanda = Kumanda()


print("""
     ***************TV******************
     
     1. Tv aç
     2. Tv kapa 
     3. ses ayarları
     4. kanal ekle
     5. kanal sayısı
     6. rastgele kanal
     7. tv bilgileri
     
     çıkmak için q 
    
    
    """)



while True:
        işlem = input("işlem seç")

        if(işlem =="q"):
            print("program sonlandırılıyor")
            break
        elif(işlem == "1"):
            kumanda.tv_ac()
        elif(işlem == "2"):
            kumanda.tv_kapat()
        elif(işlem == "3"):
            kumanda.ses_açma()
        elif(işlem == "4"):
            kanal_isimleri = input(", ile ayırarak girin")
            kanal_listesi = kanal_isimleri.split(",")
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
        elif(işlem == "5"):
            print("kanal sayısı: ",len(kumanda))
            kumanda.tv_ac()
        elif(işlem == "6"):
            kumanda.rastgele_kanal()
        elif(işlem == "7"):
            print(kumanda)

        else:
            print("geçersiz işlem")
