import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Güzel mi")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("tıkla")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))

        self.show()

    def click(self,checkBox, yazi_alani):
        if checkBox:
            yazi_alani.setText("güzelmiş")
        else:
            yazi_alani.setText("değilse neden")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())
