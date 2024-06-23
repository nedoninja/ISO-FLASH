from PyQt6 import QtWidgets
from design import UIMainWindow
import os
import json
import subprocess
import sqlite3
import urllib.request


class MainWindow(QtWidgets.QMainWindow, UIMainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)

        self.pushButton.clicked.connect(self.nextTab)
        self.pushButton_3.clicked.connect(self.formatDisk)
        self.pushButton_2.clicked.connect(self.about)
        self.pushButton_5.clicked.connect(self.start)
        self.pushButton_4.clicked.connect(self.start)
        self.pushButton_6.clicked.connect(self.start)
        self.pushButton_9.clicked.connect(self.start)
        self.pushButton_7.clicked.connect(self.wrtiteIso)
        self.pushButton_8.clicked.connect(self.selectFile)
        self.pushButton_10.clicked.connect(self.settingInstall)
        self.pushButton_11.clicked.connect(self.start)



        self.comboBox.addItems(self.listDivices())
        self.comboBox_2.addItems(self.listDivices())
        self.comboBox_4.addItems(self.listDivices())
        self.comboBox_3.addItems(self.distoList())


    def nextTab(self):
        if self.radioButton.isChecked():
            self.tabWidget.setCurrentIndex(3)
        elif self.radioButton_2.isChecked():
            self.tabWidget.setCurrentIndex(1)
        elif self.radioButton_3.isChecked():
            self.tabWidget.setCurrentIndex(2)


    def about(self):
        self.tabWidget.setCurrentIndex(4)


    def listDivices(self):
        list_devices = []

        list_files = subprocess.run(["lsblk", "-o", "TYPE,SIZE,KNAME,HOTPLUG", "-J"], capture_output=True)  # lsblk -o TYPE,SIZE,KNAME,HOTPLUG -J
        disk_dict = json.loads(list_files.stdout.decode())

        for disks_info in disk_dict.values():
            for disk_info in disks_info:
                if disk_info["type"] == "disk" and "zram" not in disk_info["kname"]:
                    is_usb_drive  = "(USB drive)" if disk_info["hotplug"]  ==  True else "(not USB drive)" 
                    str_dev_info = f"{disk_info["kname"]}  {disk_info['size']}  {is_usb_drive}"
                    list_devices.append(str_dev_info)
        return list_devices


    def formatDisk(self):
        disk = self.comboBox.currentText().split()
        
        self.tabWidget.setCurrentIndex(5)

        self.label_8.setText("Formatting...")
        self.pushButton_5.hide()
        code_star = subprocess.run(["sudo", "dd", "if=/dev/zero", f"of=/dev/{disk[0]}", "b4=1M"],stdout=subprocess.PIPE).returncode
        if code_star == 0:
            self.pushButton_5.show()


    def start(self):
        self.tabWidget.setCurrentIndex(0)


    def selectFile(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "", "ISO Files(*.iso);;All Files (*)")
        if self.file_name:
            self.label_11.setText(self.file_name[0])


    def wrtiteIso(self):
        try:
            disk = self.comboBox_2.currentText().split()
            if self.file_name:
                file = self.file_name[0]
            self.tabWidget.setCurrentIndex(5)
            self.tabWidget.setCurrentIndex(5)
            #code_star = subprocess.run(["sudo", "dd", f"if={file}", f"of=/dev/{disk[0]}", "bs=4M"],stdout=subprocess.PIPE).returncode
            os.system(f"sudo dd if={file} of=/dev/{disk[0]} bs=4M && sync")
           # if code_star == 0:
            self.pushButton_5.show()

        except:
            print("No file selected")
            self.tabWidget.setCurrentIndex(1)

        
    def distoList(self):
        ret_lits = []

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute("SELECT NAME FROM BASE")
        for name in cur.fetchall():
            ret_lits.append(name[0])

        return ret_lits
    

    def settingInstall(self):
        name = self.comboBox_3.currentText()
        disk = self.comboBox_4.currentText().split()

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute(f"SELECT Link FROM BASE WHERE Name='{name}'")
        link = cur.fetchall()[0][0]
        
        self.tabWidget.setCurrentIndex(5)
        self.label_8.setText("Pleas Wait...")

        res = urllib.request.urlopen(link)

        file = link.split("/")[-1]
        self.pushButton_5.hide()
        #code_star = subprocess.run(["sudo", "dd", f"if={file}", f"of=/dev/{disk[0]}", "bs=4M"],stdout=subprocess.PIPE).returncode
        os.system(f"sudo dd if={file} of=/dev/{disk[0]} bs=4M && sync")
        # if code_star == 0:
        self.pushButton_5.show()