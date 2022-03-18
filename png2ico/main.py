# -----------------------------------------------------------------------------
# Copyright (c) 2022, DARKSOUL
# Distributed under the GNU General Public License v3.0
# -----------------------------------------------------------------------------

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
import getpass

user_name= getpass.getuser()
SAVE_PATH= "C:/Users/"+user_name+"/Pictures/Png to Ico/"

if not os.path.exists(SAVE_PATH):
    try:
        os.mkdir(SAVE_PATH)
    except:
        pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 391, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 46, 81, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 80, 151, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.browse)
        self.pushButton_2.clicked.connect(self.convert)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PNG to ICO Converter"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))

    def browse(self):
        filename, _= QtWidgets.QFileDialog.getOpenFileName(None, "Open .png image", '', '*.png')
        global image_path
        image_path= str(filename.replace("/", "\\"))
        self.lineEdit.setText(image_path)
        
        raw_name= os.path.basename(image_path)
        global image_name
        image_name= str(SAVE_PATH+raw_name+".ico")

    def convert(self):
        try:
            img= Image.open(image_path)
            img.save(image_name)

            success_msg= QMessageBox()
            success_msg.setText("Image convert successfully!")
            success_msg.setWindowTitle("Completed!")
            success_msg.setStandardButtons(QMessageBox.Ok)
            success_msg.exec_()
        except:
            error_msg= QMessageBox()
            error_msg.setText("Image convert Failed!")
            error_msg.setWindowTitle("Failed!")
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
