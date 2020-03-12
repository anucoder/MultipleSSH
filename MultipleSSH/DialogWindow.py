
from PyQt5 import QtCore, QtGui, QtWidgets
from ATT_Login_v2 import Ui_MainWindow


class Ui_FirstWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(240, 10, 80, 30))
        self.pushButtonOK.setObjectName("pushButton")
        self.pushButtonOK.clicked.connect(lambda: self.openWindow(self.lineEdit.text()))
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(240, 50, 80, 30))
        self.pushButtonCancel.setObjectName("pushButton_2")
        self.pushButtonCancel.clicked.connect(self.closeWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 180, 30))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonOK.setText(_translate("MainWindow", "OK"))
        self.pushButtonCancel.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "Enter the no. of tabs :"))

    def closeWindow(self):
        sys.exit()

    def openWindow(self,nooftabsstr):
        nooftabs = int(nooftabsstr)
        print(nooftabs)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window,nooftabs)
        MainWindow.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
