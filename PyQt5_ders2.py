import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("burası bir yazı")
    etiket1.move(200,30)


    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setText("burası bir yazı")
    etiket2.setPixmap(QtGui.QPixmap("fcf.png"))
    etiket2.move(60,100)


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
