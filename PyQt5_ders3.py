import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Bu bir buton")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("hehh")
    etiket.move(200,30)
    buton.move(180,90)



    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
