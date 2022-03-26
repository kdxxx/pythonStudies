import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.radio_yazisi = QLabel("hangisi daha güzel")
        self.elma = QRadioButton("elma")
        self.kiraz = QRadioButton("kiraz")
        self.şeftali = QRadioButton("şeftali")

        self.yazi_alani = QLabel("")
        self.buton = QPushButton("gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.elma)
        v_box.addWidget(self.kiraz)
        v_box.addWidget(self.şeftali)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.elma.isChecked(),self.kiraz.isChecked(),self.şeftali.isChecked(),self.yazi_alani))

        self.setWindowTitle("Radio Button")

        self.show()

    def click(self,elma,kiraz,şeftali,yazi_alani):
        if elma:
            yazi_alani.setText("elma")
        if kiraz:
            yazi_alani.setText("kiraz")
        if şeftali:
            yazi_alani.setText("şeftali")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
