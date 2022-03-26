import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cıkıs = QAction("Cıkıs", self)
        cıkıs.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cıkıs)


        ara_ve_degıstır = duzenle.addMenu("Ara ve Değiştir")
        ara = QAction("Ara",self)
        degıstır = QAction("Değiştir",self)
        temizle = QAction("Temizle",self)

        ara_ve_degıstır.addAction(ara)
        ara_ve_degıstır.addAction(degıstır)
        duzenle.addAction(temizle)

        cıkıs.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)


        self.setWindowTitle("Menüler")
        self.show()

    def cikis_yap(self):
        qApp.quit()

    def response(self,action):
        if action.text == "Dosya Aç":
            print("dosya açılıyor")
        elif action.text == "Dosya Kaydet":
            print("dosya kaydediliyor")
        elif action.text == "Cıkıs":
            print("çıkış yapılıyor")

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())
