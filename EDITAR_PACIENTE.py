# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\agendamento\telas\EDITAR_PACIENTE.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 239)
        MainWindow.setStyleSheet("background-color: rgb(152, 253, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.label.setObjectName("label")
        self.c_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.c_nome.setGeometry(QtCore.QRect(60, 70, 141, 31))
        self.c_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_nome.setObjectName("c_nome")
        self.botao_editar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_editar.setGeometry(QtCore.QRect(370, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.botao_editar.setFont(font)
        self.botao_editar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.botao_editar.setObjectName("botao_editar")
        self.c_contato = QtWidgets.QLineEdit(self.centralwidget)
        self.c_contato.setGeometry(QtCore.QRect(690, 70, 141, 31))
        self.c_contato.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_contato.setObjectName("c_contato")
        self.c_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.c_endereco.setGeometry(QtCore.QRect(220, 70, 201, 31))
        self.c_endereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_endereco.setObjectName("c_endereco")
        self.aviso = QtWidgets.QLabel(self.centralwidget)
        self.aviso.setGeometry(QtCore.QRect(270, 110, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.aviso.setFont(font)
        self.aviso.setText("")
        self.aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.aviso.setObjectName("aviso")
        self.c_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.c_cpf.setGeometry(QtCore.QRect(450, 70, 201, 31))
        self.c_cpf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_cpf.setObjectName("c_cpf")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome                      Endereço                                    CPF                              contato"))
        self.botao_editar.setText(_translate("MainWindow", "Editar Dados"))
