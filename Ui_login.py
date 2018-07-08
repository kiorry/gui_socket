# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\PY_PROJECT\socket_project\login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import userDB


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        # 设置背景图片
        # palette1 = QtGui.QPalette()
        # palette1.setColor(Form.backgroundRole(), QColor(192, 253, 123))
        # palette1.setBrush(Form.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./BG.png')))
        # Form.setPalette(palette1)


        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)
        self.label_account = QtWidgets.QLabel(Form)
        self.label_account.setObjectName("label_account")
        self.horizontalLayout.addWidget(self.label_account)
        self.lineEdit_account = QtWidgets.QLineEdit(Form)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.horizontalLayout.addWidget(self.lineEdit_account)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)

        self.pushButton_submit = QtWidgets.QPushButton(Form)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout_3.addWidget(self.pushButton_submit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.pushButton_submit.clicked.connect(self.login)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登陆"))
        self.label_account.setText(_translate("Form", "帐号"))
        self.label_password.setText(_translate("Form", "密码"))
        self.pushButton_submit.setText(_translate("Form", "登录"))

    def login(self):
        name, password = userDB.searchDB()
        input_account = self.lineEdit_account.text()
        input_password = self.lineEdit_password.text()

        if input_account == name and input_password == password:
            self.lineEdit_account.clear()
            self.lineEdit_password.clear()
            print("well doen!")

        else:
            # print("请输入正确的用户名及密码!")
            self.lineEdit_account.clear()
            self.lineEdit_password.clear()
            msg = QtWidgets.QMessageBox()
            msg.critical(Form,"帐号密码输入错误!","请输入正确的帐号及密码!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

