from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(67, 68, 67);\n"
"color: rgb(220, 220, 221);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -30, 501, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(45, 39, 39);\n"
"border-radius: 10px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 151, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(170, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(parent=self.tab)
        self.radioButton.setGeometry(QtCore.QRect(150, 180, 251, 24))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(13)
        font.setBold(True)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("")
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 230, 181, 24))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(13)
        font.setBold(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 280, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(13)
        font.setBold(True)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 140, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(13)
        font.setBold(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(50, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(50, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"background-color: rgb(45, 39, 39);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(40, 270, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(8)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(180, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(40, 140, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(13)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(40, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 140, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(13)
        font.setBold(True)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setCurrentText("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(20)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(40, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(40, 260, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(13)
        font.setBold(True)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setCurrentText("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.tab_6)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 330, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(20, 90, 171, 171))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_15.setGeometry(QtCore.QRect(210, 60, 261, 111))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(40, 290, 91, 18))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(200, 230, 281, 18))
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(140, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(22)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 320, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ethiopic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"background-color: rgb(110, 112, 112);\n"
"border-radius: 20px;   \n"
"color: rgb(220, 220, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iso flash"))
        self.pushButton_2.setText(_translate("MainWindow", "about"))
        self.label.setText(_translate("MainWindow", "Select option"))
        self.radioButton.setText(_translate("MainWindow", "Downlad and write"))
        self.radioButton_2.setText(_translate("MainWindow", "Write from iso"))
        self.radioButton_3.setText(_translate("MainWindow", "Format disk"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_6.setText(_translate("MainWindow", "Previous"))
        self.label_5.setText(_translate("MainWindow", "Options"))
        self.pushButton_7.setText(_translate("MainWindow", "Yes"))
        self.label_9.setText(_translate("MainWindow", "Drive"))
        self.label_10.setText(_translate("MainWindow", "Iso image"))
        self.pushButton_8.setText(_translate("MainWindow", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.pushButton_3.setText(_translate("MainWindow", "Yes"))
        self.pushButton_4.setText(_translate("MainWindow", "Previous"))
        self.label_3.setText(_translate("MainWindow", "Are you ready to erase all data?"))
        self.label_4.setText(_translate("MainWindow", "Options"))
        self.label_7.setText(_translate("MainWindow", "Drive"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_12.setText(_translate("MainWindow", "Drive"))
        self.pushButton_9.setText(_translate("MainWindow", "Previous"))
        self.pushButton_10.setText(_translate("MainWindow", "Yes"))
        self.label_6.setText(_translate("MainWindow", "Options"))
        self.label_14.setText(_translate("MainWindow", "Distro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.pushButton_11.setText(_translate("MainWindow", "Previous"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ISO FLASH - A free and simple program <br/>based on QT for burning images to disk, for formatting disks, <br/>for downloading GNU/LINUX <br/>distributions </p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "version:0.01"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><a>https://github.com/nedoninja/ISO-FLASH</a></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.label_8.setText(_translate("MainWindow", "Pleas wait ..."))
        self.pushButton_5.setText(_translate("MainWindow", "Finish"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
