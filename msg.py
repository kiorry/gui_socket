from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class msg(QMessageBox):
    def __init(self):
        supeer(msg,self).__init()
        self.infomation(self,"标题","我就是个大叙事",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ms = msg()
    ms.show()
    sys.exit(app.exec_())