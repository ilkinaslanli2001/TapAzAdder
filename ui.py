# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Fri Oct 11 23:17:49 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 480)
        MainWindow.setMaximumSize(QtCore.QSize(764, 480))
        MainWindow.setStyleSheet("QLabel\n"
"{\n"
"font-size:15px;\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 100, 161, 22))
        self.comboBox.setStyleSheet("comboBox\n"
"{\n"
"width:auto;\n"
"\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 430, 201, 16))
        self.label_11.setStyleSheet("Qlabel{\n"
"width:auto;\n"
"}")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(130, 341, 31, 20))
        self.toolButton.setObjectName("toolButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 10, 251, 111))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 20, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 50, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(50, 80, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 61, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 80, 141, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 420, 121, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:green;\n"
"border-radius:40px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover\n"
"\n"
"{\n"
"background-color:#00B241;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 340, 581, 21))
        self.label_10.setStyleSheet("label10\n"
"{\n"
"width:auto;\n"
"}")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 140, 341, 171))
        self.textEdit.setStyleSheet("QTextEdit\n"
"{\n"
"font-size:13px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 150, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(570, 150, 141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(664, 430, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 60, 161, 22))
        self.comboBox_2.setStyleSheet("comboBox\n"
"{\n"
"width:auto;\n"
"\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Description", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Product Type", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "User haqqin da melumat", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Mail:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Number:", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Product name", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Sekiller:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Interval:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Min:3s", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Creator contact", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Product Category", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

