# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

path = "./"
def read_conf():
    with open(path+"shadow.conf", 'r') as f:
        for line in f.readlines():
            info = line.strip().split(":")
            tag = info[0].strip()
            content = info[1].strip()
            if(tag == "name"):
                name = content
            elif tag == "email":
                email = content
            elif tag == "password":
                pwd = content
        return [name, email, pwd]


class Ui_Dialog_Main(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.appBox = QtWidgets.QGroupBox(Dialog)
        self.appBox.setGeometry(QtCore.QRect(5, 7, 391, 241))
        self.appBox.setObjectName("appBox")
        self.appLabel = QtWidgets.QLabel(self.appBox)
        self.appLabel.setGeometry(QtCore.QRect(117, 12, 200, 44))
        self.appLabel.setObjectName("appLabel")

        self.textEdit = QtWidgets.QTextEdit(self.appBox)
        self.textEdit.setGeometry(QtCore.QRect(40, 61, 311, 151))
        self.textEdit.setObjectName("textEdit")

        self.askBtn = QtWidgets.QPushButton(Dialog)
        self.askBtn.setGeometry(QtCore.QRect(60, 257, 75, 23))
        self.askBtn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.askBtn.setObjectName("ask")

        self.closeBtn = QtWidgets.QPushButton(Dialog)
        self.closeBtn.setGeometry(QtCore.QRect(270, 257, 75, 23))
        self.closeBtn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.closeBtn.setObjectName("close")

        self.retranslateUi(Dialog)
        self.closeBtn.clicked.connect(Dialog.close)
        self.askBtn.clicked.connect(Dialog.ask)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shadow"))
        self.appLabel.setText(_translate("Dialog", "Your Shadow is Running"))
        self.closeBtn.setText(_translate("Dialog", "??????"))
        self.askBtn.setText(_translate("Dialog", "??????"))



class Ui_Dialog_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.appBox = QtWidgets.QGroupBox(Dialog)
        self.appBox.setGeometry(QtCore.QRect(5, 7, 391, 241))
        self.appBox.setObjectName("appBox")
        self.appLabel = QtWidgets.QLabel(self.appBox)
        self.appLabel.setGeometry(QtCore.QRect(150, 20, 200, 27))
        self.appLabel.setObjectName("appLabel")

        self.nameLabel = QtWidgets.QLabel(self.appBox)
        self.nameLabel.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.nameLabel.setObjectName("nameLabel")

        self.name = QtWidgets.QLineEdit(self.appBox)
        self.name.setGeometry(QtCore.QRect(100, 70, 200, 27))
        self.name.setObjectName("name")


        self.emailLabel = QtWidgets.QLabel(self.appBox)
        self.emailLabel.setGeometry(QtCore.QRect(30, 120, 61, 21))
        self.emailLabel.setObjectName("emailLabel")

        self.email = QtWidgets.QLineEdit(self.appBox)
        self.email.setGeometry(QtCore.QRect(100, 120, 200, 27))
        self.email.setObjectName("email")


        self.pwdLabel = QtWidgets.QLabel(self.appBox)
        self.pwdLabel.setGeometry(QtCore.QRect(30, 170, 61, 21))
        self.pwdLabel.setObjectName("pwd_label")

        self.pwd = QtWidgets.QLineEdit(self.appBox)
        self.pwd.setGeometry(QtCore.QRect(100, 170, 200, 27))
        self.pwd.setObjectName("pwd")


        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setGeometry(QtCore.QRect(60, 257, 75, 23))
        self.loginBtn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.loginBtn.setObjectName("loginBtn")

        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setGeometry(QtCore.QRect(270, 257, 75, 23))
        self.clearBtn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.clearBtn.setObjectName("clearBtn")
        
        self.retranslateUi(Dialog)
        self.loginBtn.clicked.connect(Dialog.start)
        self.clearBtn.clicked.connect(Dialog.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shadow"))
        # self.appBox.setTitle(_translate("Dialog", "Shadow ?????????"))
        self.appLabel.setText(_translate("Dialog", "Shadow ?????????"))

        self.nameLabel.setText(_translate("Dialog", "??????"))
        self.emailLabel.setText(_translate("Dialog", "??????"))
        self.pwdLabel.setText(_translate("Dialog", "????????????"))

        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        conf = read_conf()
        self.name.setText(conf[0])
        self.email.setText(conf[1])
        self.pwd.setText(conf[2])


        self.loginBtn.setText(_translate("Dialog", "??????"))
        self.clearBtn.setText(_translate("Dialog", "??????"))