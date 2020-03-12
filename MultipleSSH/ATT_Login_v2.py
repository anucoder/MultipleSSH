from PyQt5 import QtCore, QtGui, QtWidgets

import fileinput
import os
import sys
Site_ID = []
ENM = []
Log = []
TAB = {}
LOG_DIR = os.path.join(os.path.expanduser('~/Desktop/'), 'Login')
LOG_FILE_TEMPLATE = os.path.join(LOG_DIR, "%s.log")

class Ui_MainWindow(object):
    def setupUi(self,MainWindow,nooftabs):
        margin_gbx = 20
        margin_gby = 20
        width_gb = 450
        height_gb = 100
        width = 700
        self.nooftabs = nooftabs
        height = (nooftabs+1)*20+(nooftabs*height_gb)
        enmlist = ["Select enm","vtc2e6enm","vtc2e7enm","vtc2e11enm","vtc2e12enm","akr1e3enm","akr1e5enm","akr1e6enm","all2e3enm","gai1e1enm","hou1e1enm","con1e2enm","van1e1enm"]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBoxes = [QtWidgets.QGroupBox(self.centralwidget) for i in range(nooftabs)]
        self.labelENMs = [QtWidgets.QLabel(self.groupBoxes[i]) for i in range(nooftabs)]
        self.labelSites = [QtWidgets.QLabel(self.groupBoxes[i]) for i in range(nooftabs)]
        self.comboBoxes = [QtWidgets.QComboBox(self.groupBoxes[i]) for i in range(nooftabs)]
        self.checkBoxes = [QtWidgets.QCheckBox(self.groupBoxes[i]) for i in range(nooftabs)]
        self.lineEdits = [QtWidgets.QLineEdit(self.groupBoxes[i]) for i in range(nooftabs)]
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(525, 40, 120, 40))
        self.OKButton.setText("OK")
        self.OKButton.clicked.connect(self.process_inputs)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(525, 90, 120, 40))
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.close_application)

        for i in range(nooftabs):
            self.groupBoxes[i].setGeometry(QtCore.QRect(margin_gbx, margin_gby, width_gb, height_gb))
            self.groupBoxes[i].setTitle("Tab{}".format(i+1))
            self.labelENMs[i].setGeometry(QtCore.QRect(10, 20, 60, 40))
            self.labelENMs[i].setAlignment(QtCore.Qt.AlignCenter)
            self.labelENMs[i].setWordWrap(True)
            self.labelENMs[i].setText("ENM")
            self.labelSites[i].setGeometry(QtCore.QRect(210, 20, 60, 40))
            self.labelSites[i].setAlignment(QtCore.Qt.AlignCenter)
            self.labelSites[i].setWordWrap(True)
            self.labelSites[i].setText("SiteID")
            self.lineEdits[i].setGeometry(QtCore.QRect(275, 20, 130, 40))
            self.checkBoxes[i].setGeometry(QtCore.QRect(75, 65, 170, 30))
            self.checkBoxes[i].setText("Start Logging")
            self.comboBoxes[i].setGeometry(QtCore.QRect(75, 20, 130, 40))
            for enm in enmlist:
                self.comboBoxes[i].addItem(enm)
            margin_gby = margin_gby + height_gb + 20

        margin_gby = margin_gby + 20
        MainWindow.resize(width,margin_gby)

    def close_application(self):
        sys.exit()

    def process_inputs(self):
        for i in range(self.nooftabs):
            Site_ID.append(self.lineEdits[i].text())
            ENM.append(self.comboBoxes[i].currentText())
            if self.checkBoxes[i].isChecked():
                Log.append("true")
            else:
                Log.append("false")

        fname = "tablist"
        file_path = LOG_FILE_TEMPLATE % fname
        filep = open(file_path, 'w+')
        for tab in range(self.nooftabs):
            filep.write("{} {} {}".format(Site_ID[tab],ENM[tab],Log[tab])+os.linesep)
        filep.close()

        sys.exit()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     nooftabs = 5
#     ui.setupUi(MainWindow,nooftabs)
#     MainWindow.show()
#     sys.exit(app.exec_())
