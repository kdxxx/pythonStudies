class Dosya():

    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerik = file.read()

            kelimeler = dosya_icerik.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
            for i in self.sade_kelimeler:
                print(i)

    def tum_kelimeler(self):
        kelimeler_kümesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)

        print("Tüm Kelimeler............")

        for i in kelimeler_kümesi:
            print(i)
            print("********************")


    def kelime_frekans(self):
        kelime_sozlük = dict()
        for i in self.sade_kelimeler:
            if(i in kelime_sozlük):
                kelime_sozlük[i] += 1
            else:
                kelime_sozlük[i] = 1
        for kelime,sayı in kelime_sozlük.items():
            print("{} kelimesi {} defa geçiyor...".format(kelime,sayı))
            print("------------------")



dosya = Dosya()
dosya.tum_kelimeler()
print("heeeeeeeee")
dosya.kelime_frekans()
