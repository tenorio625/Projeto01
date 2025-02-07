# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\agendamento\telas\PACIENTE.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 637)
        MainWindow.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.consultas = QtWidgets.QPushButton(self.centralwidget)
        self.consultas.setGeometry(QtCore.QRect(40, 30, 191, 41))
        self.consultas.setObjectName("consultas")
        self.tabela_pacientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_pacientes.setGeometry(QtCore.QRect(40, 120, 721, 241))
        self.tabela_pacientes.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_pacientes.setObjectName("tabela_pacientes")
        self.tabela_pacientes.setColumnCount(4)
        self.tabela_pacientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pacientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pacientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pacientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pacientes.setHorizontalHeaderItem(3, item)
        self.tabela_pacientes.horizontalHeader().setVisible(True)
        self.tabela_pacientes.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_pacientes.horizontalHeader().setDefaultSectionSize(180)
        self.tabela_pacientes.horizontalHeader().setHighlightSections(True)
        self.tabela_pacientes.horizontalHeader().setSortIndicatorShown(False)
        self.tabela_pacientes.horizontalHeader().setStretchLastSection(False)
        self.tabela_pacientes.verticalHeader().setVisible(True)
        self.tabela_pacientes.verticalHeader().setCascadingSectionResizes(False)
        self.tabela_pacientes.verticalHeader().setHighlightSections(True)
        self.tabela_pacientes.verticalHeader().setSortIndicatorShown(False)
        self.tabela_pacientes.verticalHeader().setStretchLastSection(False)
        self.pacientes = QtWidgets.QPushButton(self.centralwidget)
        self.pacientes.setGeometry(QtCore.QRect(300, 30, 191, 41))
        self.pacientes.setObjectName("pacientes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-140, -10, 1571, 101))
        self.label.setStyleSheet("background-color: rgb(255, 220, 114);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.novo_paciente = QtWidgets.QPushButton(self.centralwidget)
        self.novo_paciente.setGeometry(QtCore.QRect(810, 130, 161, 31))
        self.novo_paciente.setObjectName("novo_paciente")
        self.att_paciente = QtWidgets.QPushButton(self.centralwidget)
        self.att_paciente.setGeometry(QtCore.QRect(790, 170, 211, 31))
        self.att_paciente.setObjectName("att_paciente")
        self.excluir_paciente = QtWidgets.QPushButton(self.centralwidget)
        self.excluir_paciente.setGeometry(QtCore.QRect(810, 210, 161, 31))
        self.excluir_paciente.setObjectName("excluir_paciente")
        self.excluir_duplicadas = QtWidgets.QPushButton(self.centralwidget)
        self.excluir_duplicadas.setGeometry(QtCore.QRect(810, 270, 161, 31))
        self.excluir_duplicadas.setObjectName("excluir_duplicadas")
        self.label.raise_()
        self.consultas.raise_()
        self.tabela_pacientes.raise_()
        self.pacientes.raise_()
        self.novo_paciente.raise_()
        self.att_paciente.raise_()
        self.excluir_paciente.raise_()
        self.excluir_duplicadas.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.consultas.setText(_translate("MainWindow", "Consultas"))
        item = self.tabela_pacientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "nome"))
        item = self.tabela_pacientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "endereço"))
        item = self.tabela_pacientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tabela_pacientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "contato"))
        self.pacientes.setText(_translate("MainWindow", "Pacientes"))
        self.novo_paciente.setText(_translate("MainWindow", "NOVO PACIENTE"))
        self.att_paciente.setText(_translate("MainWindow", "ATUALIZAR DADOS PACIENTE"))
        self.excluir_paciente.setText(_translate("MainWindow", "EXCLUIR PACIENTE"))
        self.excluir_duplicadas.setText(_translate("MainWindow", "EXCLUIR DUPLICADAS"))
