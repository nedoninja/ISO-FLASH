import sys
from PyQt6 import QtWidgets
from window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
