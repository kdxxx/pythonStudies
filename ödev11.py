import sqlite3
import time


class Şarkı():
    def __init__(self, şarkı_ismi, sanatçı, albüm, prodüksiyon_şirketi, dakika, saniye):
        self.şarkı_ismi = şarkı_ismi
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.dakika = dakika
        self.saniye = saniye

        self.süre = str(self.dakika) + ":" + str(self.saniye)

    def __str__(self):
        return "{}/ {}/ {}/ {}/ {}\n".format(self.şarkı_ismi, self.sanatçı, self.albüm, self.prodüksiyon_şirketi,
                                             self.süre)


class Kütüphane():
    def __init__(self):

        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):

        self.bağlantı = sqlite3.connect("Şarkı_Kütüphanesi.db")
        self.imleç = self.bağlantı.cursor()

        self.imleç.execute(
            "CREATE TABLE IF NOT EXISTS Şarkılar(İsim TEXT, Sanatçı TEXT, Albüm TEXT, P_Şirketi TEXT, Dakika_Süre INT, Saniye_Süre INT)")
        self.bağlantı.commit()

    def bağlantı_kapat(self):

        self.bağlantı.close()

    def bilgileri_göster(self):

        self.imleç.execute("SELECT * FROM Şarkılar")
        a = self.imleç.fetchall()

        print("(Sıralama: Şarkı İsmi/ Sanatçı/ Albüm/ Prodüksiyon Şirketi/ Şarkı Süresi)\n")
        for i in a:
            print(Şarkı(i[0], i[1], i[2], i[3], i[4], i[5]))

    def şarkı_ekle(self):

        print("(Lütfen sizden istenilen bilgileri uygun yerlere yazın.)")
        time.sleep(2)

        şarkı_ismi = input("Şarkı İsmi:")
        if (şarkı_ismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return

        sanatçı = str(input("Sanatçı Adı:"))
        if (şarkı_ismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        albüm = str(input("Albüm Adı:"))
        if (şarkı_ismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        prodüksiyon_şirketi = str(input("Prodüksiyon Şirketi:"))
        if (şarkı_ismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        try:
            şarkı_süresi_dakika = int(input("Şarkı Süresi(Dakika):"))
            if (şarkı_ismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            şarkı_süresi_saniye = int(input("Şarkı Süresi(Saniye):"))
            if (şarkı_ismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
        except (ValueError):
            print("Lütfen rakam giriniz.\n")
            return kütüphane.şarkı_ekle()

        print("Şarkı Ekleniyor...")
        time.sleep(2)

        self.imleç.execute("INSERT INTO Şarkılar Values(?, ?, ?, ?, ?, ?)",
                           (şarkı_ismi, sanatçı, albüm, prodüksiyon_şirketi, şarkı_süresi_dakika, şarkı_süresi_saniye))
        self.bağlantı.commit()

        print("Şarkı Eklendi")

    def şarkı_sil(self):

        print("Şarkılar;")
        self.imleç.execute("SELECT İsim FROM Şarkılar")
        a = self.imleç.fetchall()
        if (len(a) == 0):
            print("Şarkı Listesi Boş")
            return
        for i in a:
            print("-" + i[0])

        for i in a:
            isim = input("Silmek istediğiniz şarkının ismini giriniz:")

            if (isim == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            elif (i[0] == isim):
                print("Şarkı siliniyor...")
                time.sleep(2)
                self.imleç.execute("DELETE FROM Şarkılar WHERE İsim = ?", (isim,))
                self.bağlantı.commit()
                print("Şarkı silindi.")
            elif (i[0] != isim):
                print("(Öyle bir isimde şarkı kütüphanede yok.)")
                continue

    def toplam_süre(self):
        self.imleç.execute("SELECT Dakika_Süre, Saniye_Süre FROM Şarkılar")
        a = self.imleç.fetchall()
        genel_toplam_dakika = 0
        genel_toplam_saniye = 0

        for i in a:
            genel_toplam_dakika += i[0]
            genel_toplam_saniye += i[1]

        while True:
            if (genel_toplam_saniye >= 60):
                x = genel_toplam_saniye // 60
                genel_toplam_saniye %= 60
                genel_toplam_dakika += x
                print(genel_toplam_dakika, "dakika", genel_toplam_saniye, "saniye")
            else:
                return False

    def yardım(self):
        print(
            "İşlemler;\n\tKütüphanedeki şarkıları görmek için: (Şarkıları göster),\n\tKütüphaneye şarkı eklemek için: (Şarkı ekle),\n\tKütüphaneden şarkı silmek için: (Şarkı sil),\n\tKütüphanedeki toplam şarkı süresini görmek için: (Toplam süreyi göster) yazınız.")


kütüphane = Kütüphane()

print("\tŞarkı Kütüphanesi v1.0")
time.sleep(1)
print("\n\t    Hoşgeldiniz\n\n(Yardım almak istiyorsanız (h), çıkmak istiyorsanız (q) tuşuna basın.)")

while True:
    print(
        "*************************************************************************************************************************\n")
    işlem = input("--->")
    print(
        "-------------------------------------\nİşlem yapılıyor, lütfen bekleyiniz...\n-------------------------------------")
    time.sleep(2)

    if (işlem == "q" or işlem == "Q"):
        print("Uygulamadan Çıkılıyor...")
        time.sleep(2)
        print("\t    Hoşçakalın")
        break
    elif (işlem == "h" or işlem == "H"):
        kütüphane.yardım()
    elif (işlem == "Şarkıları göster" or işlem == "ŞARKILARI GÖSTER" or işlem == "şarkıları göster"):
        print("Şarkılar;")
        kütüphane.bilgileri_göster()
    elif (işlem == "Şarkı ekle" or işlem == "ŞARKI EKLE" or işlem == "şarkı ekle"):
        kütüphane.şarkı_ekle()
    elif (işlem == "Şarkı sil" or işlem == "ŞARKI SİL" or işlem == "şarkı sil"):
        kütüphane.şarkı_sil()
    elif (işlem == "Toplam süreyi göster" or işlem == "TOPLAM SÜREYİ GÖSTER" or işlem == "toplam süreyi göster"):
        kütüphane.toplam_süre()
    else:
        print("Geçersiz İşlem")
