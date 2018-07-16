# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys  
import FileServer
    
class QlabelDemo(QDialog):  
    def __init__(self ):  
        super().__init__()
        self.host = "127.0.0.1"
        self.port = 3214
         
        self.setWindowTitle('FTP服务器')
        self.host_label = QLabel('&Host', self)
        self.hostEd = QLineEdit( self )
        self.host_label.setBuddy(self.hostEd)
        self.hostEd.setText(self.host)
        
        self.port_label = QLabel('&Port', self)
        self.portEd = QLineEdit( self )
        self.port_label.setBuddy(self.portEd)
        self.portEd.setText("%d"%self.port)

        self.btnOk = QPushButton('&OK')
        self.btnOk.clicked.connect(self.Submit)
        self.btnCancel = QPushButton('&Cancel')

        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.host_label,0,0)
        self.mainLayout.addWidget(self.hostEd,0,1,1,2)
        self.mainLayout.addWidget(self.port_label,1,0)
        self.mainLayout.addWidget(self.portEd,1,1,1,2)
        self.mainLayout.addWidget(self.btnOk,2,1)
        self.mainLayout.addWidget(self.btnCancel,2,2)
    
    def Submit(self):
        s = FileServer.Server(self.hostEd.text(),int(self.portEd.text()))
        s.Run()
        

  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    labelDemo = QlabelDemo()  
    labelDemo.show()  
    sys.exit(app.exec_())
