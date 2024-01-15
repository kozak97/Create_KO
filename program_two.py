import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from window_portal import *
import sqlite3 as sl
import random
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import FirefoxOptions



class Ui_MainWindow(object):
    number=0
    def setupUi(self, MainWindow):
        if Ui_MainWindow.number==0:
                Ui_MainWindow.number=1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(int(960*suma3/Ui_MainWindow.number), int(540*suma3/Ui_MainWindow.number))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(int(400*suma3/Ui_MainWindow.number), int(0*suma3/Ui_MainWindow.number)))
        MainWindow.setMaximumSize(QtCore.QSize(int(16777215*suma3/Ui_MainWindow.number), int(16777215*suma3/Ui_MainWindow.number)))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(int(567*suma3/Ui_MainWindow.number), int(0*suma3/Ui_MainWindow.number)))
        self.tableWidget.setMaximumSize(QtCore.QSize(int(3000*suma3/Ui_MainWindow.number), int(2000*suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(12/Ui_MainWindow.number))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
f"    border: {2*suma3/Ui_MainWindow.number}px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {2*suma3/Ui_MainWindow.number}%;\n"
"}\n"
"\n"
"QTableWidget::item:hover{\n"
"    background-color: rgb(41, 213, 202);\n"
"}")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        table = self.tableWidget
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        # форма1
        self.frame_create_kom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_create_kom.sizePolicy().hasHeightForWidth())
        self.frame_create_kom.setSizePolicy(sizePolicy)
        self.frame_create_kom.setMinimumSize(QtCore.QSize(int(300*suma3/Ui_MainWindow.number), int(540*suma3/Ui_MainWindow.number)))
        self.frame_create_kom.setMaximumSize(QtCore.QSize(int(800*suma3/Ui_MainWindow.number), int(16777215*suma3/Ui_MainWindow.number)))
        self.frame_create_kom.setStyleSheet("QFrame{\n"
                                            f"    border-radius: {2*suma3/Ui_MainWindow.number}%;\n"
                                            f"    border: {2*suma3/Ui_MainWindow.number}px solid;\n"
                                            "    border-color: rgb(41, 213, 202);\n"
                                            "}")
        self.frame_create_kom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_create_kom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_create_kom.setObjectName("frame_create_kom")
        self.frame_create_kom.hide()
        self.layoutWidget = QtWidgets.QWidget(self.frame_create_kom)
        self.layoutWidget.setGeometry(QtCore.QRect(int(18*suma3/Ui_MainWindow.number), int(14*suma3/Ui_MainWindow.number), int(262*suma3/Ui_MainWindow.number), int(509*suma3/Ui_MainWindow.number)))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nazva_metodulu = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nazva_metodulu.sizePolicy().hasHeightForWidth())
        self.nazva_metodulu.setSizePolicy(sizePolicy)
        self.nazva_metodulu.setPlaceholderText("Назва методики:")
        self.nazva_metodulu.setMinimumSize(QtCore.QSize(int(260*suma3/Ui_MainWindow.number), int(40*suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.nazva_metodulu.setFont(font)
        self.nazva_metodulu.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"    border: 1px solid;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"\n"
"    \n"
"}")
        self.nazva_metodulu.setObjectName("nazva_metodulu")
        self.verticalLayout.addWidget(self.nazva_metodulu)
        self.add_qestion = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_qestion.sizePolicy().hasHeightForWidth())
        self.add_qestion.setSizePolicy(sizePolicy)
        self.add_qestion.setPlaceholderText('Питання:')
        self.add_qestion.setMinimumSize(QtCore.QSize(int(260*suma3/Ui_MainWindow.number), int(40*suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_qestion.setFont(font)
        self.add_qestion.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"    border: 1px solid;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"\n"
"    \n"
"}")
        self.add_qestion.setObjectName("add_qestion")
        self.verticalLayout.addWidget(self.add_qestion)
        self.add_grup = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_grup.sizePolicy().hasHeightForWidth())
        self.add_grup.setSizePolicy(sizePolicy)
        self.add_grup.setMinimumSize(QtCore.QSize(int(260*suma3/Ui_MainWindow.number), int(40*suma3/Ui_MainWindow.number)))
        self.add_grup.setPlaceholderText('Група:')
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_grup.setFont(font)
        self.add_grup.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"    border: 1px solid;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"\n"
"    \n"
"}")
        self.add_grup.setObjectName("add_grup")
        self.verticalLayout.addWidget(self.add_grup)
        spacerItem = QtWidgets.QSpacerItem(int(20*suma3/Ui_MainWindow.number), int(13*suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.School = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.School.setFont(font)
        self.School.setObjectName("School")
        self.verticalLayout.addWidget(self.School)
        self.Doschilnul = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Doschilnul.setFont(font)
        self.Doschilnul.setObjectName("Doschilnul")
        self.verticalLayout.addWidget(self.Doschilnul)
        spacerItem1 = QtWidgets.QSpacerItem(int(20*suma3/Ui_MainWindow.number), int(13*suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.File_save = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.File_save.setFont(font)
        self.File_save.setObjectName("File_save")
        self.File_save.setText('Зберегти файлом?')
        self.verticalLayout.addWidget(self.File_save)
        spacerItem2 = QtWidgets.QSpacerItem(int(20*suma3/Ui_MainWindow.number), int(13*suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.add_to_metoduk = QtWidgets.QPushButton(self.layoutWidget)
        self.add_to_metoduk.setMinimumSize(QtCore.QSize(int(0*suma3/Ui_MainWindow.number), int(40*suma3/Ui_MainWindow.number)))
        self.add_to_metoduk.setMaximumSize(QtCore.QSize(int(260*suma3/Ui_MainWindow.number), int(16777215*suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_to_metoduk.setFont(font)
        self.add_to_metoduk.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"    border: 1px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"\n"
"    \n"
"}")
        self.add_to_metoduk.setObjectName("add_to_metoduk")
        self.verticalLayout.addWidget(self.add_to_metoduk)
        self.delete_qestion = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_qestion.setMinimumSize(QtCore.QSize(int(0*suma3/Ui_MainWindow.number), int(40*suma3/Ui_MainWindow.number)))
        self.delete_qestion.setMaximumSize(QtCore.QSize(int(260*suma3/Ui_MainWindow.number), int(16777215*suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.delete_qestion.setFont(font)
        self.delete_qestion.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"    border: 1px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(41, 213, 202);\n"
f"    border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"\n"
"    \n"
"}")
        self.delete_qestion.setObjectName("delete_qestion")
        self.verticalLayout.addWidget(self.delete_qestion)
        spacerItem3 = QtWidgets.QSpacerItem(int(20*suma3/Ui_MainWindow.number), int(150*suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.frame_create_kom, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(int(69*suma3/Ui_MainWindow.number), int(16777215*suma3/Ui_MainWindow.number)))
        self.widget.setStyleSheet(f"border-radius: {4*suma3/Ui_MainWindow.number}%;\n"
"background-color: rgb(41, 213, 202);")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_metoduk = QtWidgets.QPushButton(self.widget)
        self.add_metoduk.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.add_metoduk.setIcon(QIcon('к.png'))
        self.add_metoduk.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
        self.add_metoduk.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.add_metoduk.setText("")
        self.add_metoduk.setObjectName("add_metoduk")
        self.verticalLayout_4.addWidget(self.add_metoduk)
        self.potreba = QtWidgets.QPushButton(self.widget)
        self.potreba.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.potreba.setIcon(QIcon('п.png'))
        self.potreba.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
        self.potreba.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.potreba.setText("")
        self.potreba.setObjectName("potreba")
        self.verticalLayout_4.addWidget(self.potreba)
        self.rekomendacii = QtWidgets.QPushButton(self.widget)
        self.rekomendacii.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.rekomendacii.setIcon(QIcon('р.png'))
        self.rekomendacii.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
        self.rekomendacii.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.rekomendacii.setText("")
        self.rekomendacii.setObjectName("rekomendacii")
        self.verticalLayout_4.addWidget(self.rekomendacii)

        self.create_qestions = QtWidgets.QPushButton(self.widget)
        self.create_qestions.setMinimumSize(QtCore.QSize(int(55 * suma3 / Ui_MainWindow.number), int(55 * suma3 / Ui_MainWindow.number)))
        self.create_qestions.setIcon(QIcon('a.png'))
        self.create_qestions.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
        self.create_qestions.setStyleSheet("QPushButton{\n"
                                        "    border: 1px solid;\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        f"    border-radius: {27 * suma3 / Ui_MainWindow.number}%;\n"
                                        "    \n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(223, 223, 223);\n"
                                        "}")
        self.create_qestions.setText("")
        self.create_qestions.setObjectName("rekomendacii")
        self.verticalLayout_4.addWidget(self.create_qestions)

        self.chenge = QtWidgets.QPushButton(self.widget)
        self.chenge.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.chenge.setIcon(QIcon('chenge.png'))
        self.chenge.setIconSize(QSize(int(35 * suma3/Ui_MainWindow.number), int(35 * suma3/Ui_MainWindow.number)))
        self.chenge.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.chenge.setText("")
        self.chenge.setObjectName("chenge")
        self.verticalLayout_4.addWidget(self.chenge)
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.save.setIcon(QIcon('save.png'))
        self.save.setIconSize(QSize(int(40 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        self.save.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.save.setText("")
        self.save.setObjectName("save")
        self.verticalLayout_4.addWidget(self.save)
        self.delete_metoduk = QtWidgets.QPushButton(self.widget)
        self.delete_metoduk.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.delete_metoduk.setIcon(QIcon('del.png'))
        self.delete_metoduk.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
        self.delete_metoduk.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.delete_metoduk.setText("")
        self.delete_metoduk.setObjectName("delete_metoduk")
        self.verticalLayout_4.addWidget(self.delete_metoduk)

        self.update_btn_avto = QtWidgets.QPushButton(self.widget)
        self.update_btn_avto.setMinimumSize(
                QtCore.QSize(int(55 * suma3 / Ui_MainWindow.number), int(55 * suma3 / Ui_MainWindow.number)))
        self.update_btn_avto.setIcon(QIcon('internet.png'))
        self.update_btn_avto.setIconSize(
                QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
        self.update_btn_avto.setStyleSheet("QPushButton{\n"
                                          "    border: 1px solid;\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          f"    border-radius: {27 * suma3 / Ui_MainWindow.number}%;\n"
                                          "    \n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(223, 223, 223);\n"
                                          "}")
        self.update_btn_avto.setText("")
        self.update_btn_avto.setObjectName("update_btn_avto")
        self.verticalLayout_4.addWidget(self.update_btn_avto)

        self.error = QtWidgets.QPushButton(self.widget)
        self.error.setMinimumSize(
            QtCore.QSize(int(55 * suma3 / Ui_MainWindow.number), int(55 * suma3 / Ui_MainWindow.number)))
        self.error.setIcon(QIcon('error.png'))
        self.error.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.error.setStyleSheet("QPushButton{\n"
                                 "    border: 1px solid;\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 f"    border-radius: {27 * suma3 / Ui_MainWindow.number}%;\n"
                                 "    \n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    background-color: rgb(223, 223, 223);\n"
                                 "}")
        self.error.setText("")
        self.error.setObjectName("error")
        self.verticalLayout_4.addWidget(self.error)
        self.error.hide()

        spacerItem4 = QtWidgets.QSpacerItem(int(20*suma3/Ui_MainWindow.number), int(250*suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem4)
        self.plus = QtWidgets.QPushButton(self.widget)
        self.plus.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.plus.setIcon(QIcon('+.png'))
        self.plus.setIconSize(QSize(int(45 * suma3/Ui_MainWindow.number), int(45 * suma3/Ui_MainWindow.number)))
        self.plus.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.plus.setText("")
        self.plus.setObjectName("plus")
        self.verticalLayout_4.addWidget(self.plus)

        self.del_che = QtWidgets.QPushButton(self.widget)
        self.del_che.setMinimumSize(
                QtCore.QSize(int(55 * suma3 / Ui_MainWindow.number), int(55 * suma3 / Ui_MainWindow.number)))
        self.del_che.setIcon(QIcon('del.png'))
        self.del_che.setIconSize(QSize(int(45 * suma3 / Ui_MainWindow.number), int(45 * suma3 / Ui_MainWindow.number)))
        self.del_che.setStyleSheet("QPushButton{\n"
                                "    border: 1px solid;\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                f"    border-radius: {27 * suma3 / Ui_MainWindow.number}%;\n"
                                "    \n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "    background-color: rgb(223, 223, 223);\n"
                                "}")
        self.del_che.setText("")
        self.del_che.setObjectName("del_che")
        self.del_che.hide()
        self.verticalLayout_4.addWidget(self.del_che)

        self.minus = QtWidgets.QPushButton(self.widget)
        self.minus.setMinimumSize(QtCore.QSize(int(55*suma3/Ui_MainWindow.number), int(55*suma3/Ui_MainWindow.number)))
        self.minus.setIcon(QIcon('-.png'))
        self.minus.setIconSize(QSize(int(45 * suma3/Ui_MainWindow.number), int(45 * suma3/Ui_MainWindow.number)))
        self.minus.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
f"    border-radius: {27*suma3/Ui_MainWindow.number}%;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 223);\n"
"}")
        self.minus.setText("")
        self.minus.setObjectName("minus")
        self.verticalLayout_4.addWidget(self.minus)

        self.add_che = QtWidgets.QPushButton(self.widget)
        self.add_che.setMinimumSize(
                QtCore.QSize(int(55 * suma3 / Ui_MainWindow.number), int(55 * suma3 / Ui_MainWindow.number)))
        self.add_che.setIcon(QIcon('2.png'))
        self.add_che.setIconSize(QSize(int(45 * suma3 / Ui_MainWindow.number), int(45 * suma3 / Ui_MainWindow.number)))
        self.add_che.setStyleSheet("QPushButton{\n"
                                 "    border: 1px solid;\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 f"    border-radius: {27 * suma3 / Ui_MainWindow.number}%;\n"
                                 "    \n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    background-color: rgb(223, 223, 223);\n"
                                 "}")
        self.add_che.setText("")
        self.add_che.setObjectName("minus")
        self.add_che.hide()
        self.verticalLayout_4.addWidget(self.add_che)

        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)


        # форма2
        self.frame_create_potr = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_create_potr.sizePolicy().hasHeightForWidth())
        self.frame_create_potr.setSizePolicy(sizePolicy)
        self.frame_create_potr.setMinimumSize(QtCore.QSize(int(300 * suma3/Ui_MainWindow.number), int(540 * suma3/Ui_MainWindow.number)))
        self.frame_create_potr.setMaximumSize(QtCore.QSize(int(800 * suma3/Ui_MainWindow.number), int(16777215 * suma3/Ui_MainWindow.number)))
        self.frame_create_potr.setStyleSheet("QFrame{\n"
                                             f"    border-radius: {2 * suma3/Ui_MainWindow.number}%;\n"
                                             f"    border: {2 * suma3/Ui_MainWindow.number}px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             "}")
        self.frame_create_potr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_create_potr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_create_potr.setObjectName("frame_create_potr")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_create_potr)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_potreba = QtWidgets.QLabel(self.frame_create_potr)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_potreba.setFont(font)
        self.label_potreba.setStyleSheet("QLabel{\n"
                                               "    border: 0px;\n"
                                               "}")
        self.label_potreba.setObjectName("label_potreba")
        self.label_potreba.setText('Виберіть методику:')
        self.verticalLayout.addWidget(self.label_potreba)



        self.comboBox_potrebu_create = QtWidgets.QComboBox(MainWindow)
        self.comboBox_potrebu_create.setMinimumSize(QtCore.QSize(int(200 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        self.comboBox_potrebu_create.setMaximumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(16777215 * suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_potrebu_create.setFont(font)
        self.comboBox_potrebu_create.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                                  "")
        self.comboBox_potrebu_create.setObjectName("comboBox_potrebu_create")

        self.verticalLayout.addWidget(self.comboBox_potrebu_create)
        spacerItem = QtWidgets.QSpacerItem(int(20 * suma3/Ui_MainWindow.number), int(10 * suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.add_potrebu = QtWidgets.QLineEdit(self.frame_create_potr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_potrebu.sizePolicy().hasHeightForWidth())
        self.add_potrebu.setSizePolicy(sizePolicy)
        self.add_potrebu.setMinimumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_potrebu.setFont(font)
        self.add_potrebu.setStyleSheet("QLineEdit{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.add_potrebu.setObjectName("add_potrebu")
        self.verticalLayout.addWidget(self.add_potrebu)
        spacerItem1 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)

        self.Show_potreb = QtWidgets.QPushButton(self.frame_create_potr)
        self.Show_potreb.setMinimumSize(
                QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.Show_potreb.setMaximumSize(
                QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.Show_potreb.setFont(font)
        self.Show_potreb.setStyleSheet("QPushButton{\n"
                                        "    \n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                        "    border: 1px solid;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    border: 1px solid;\n"
                                        "    border-color: rgb(41, 213, 202);\n"
                                        f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                        "\n"
                                        "    \n"
                                        "}")
        self.Show_potreb.setObjectName("add_to_potrebu_recom")
        self.Show_potreb.setText('Завантажити групи')
        self.verticalLayout.addWidget(self.Show_potreb)
        self.Show_potreb.hide()

        self.comboBox_grup_potrebu = QtWidgets.QComboBox(MainWindow)
        self.comboBox_grup_potrebu.setMinimumSize(QtCore.QSize(int(200 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        self.comboBox_grup_potrebu.setMaximumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(16777215 * suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_grup_potrebu.setFont(font)
        self.comboBox_grup_potrebu.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                          "")
        self.comboBox_grup_potrebu.setObjectName("comboBox_grup_potrebu")
        self.verticalLayout.addWidget(self.comboBox_grup_potrebu)
        spacerItem2 = QtWidgets.QSpacerItem(int(20 * suma3/Ui_MainWindow.number), int(10 * suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.File_save_potrebu = QtWidgets.QCheckBox(self.frame_create_potr)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.File_save_potrebu.setFont(font)
        self.File_save_potrebu.setObjectName("File_save_potrebu")
        self.File_save_potrebu.setText('Зберегти файлом?')
        self.verticalLayout.addWidget(self.File_save_potrebu)
        spacerItem3 = QtWidgets.QSpacerItem(int(20 * suma3/Ui_MainWindow.number), int(13 * suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.add_to_potrebu = QtWidgets.QPushButton(self.frame_create_potr)
        self.add_to_potrebu.setMinimumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        self.add_to_potrebu.setMaximumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(16777215 * suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_to_potrebu.setFont(font)
        self.add_to_potrebu.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "    border: 1px solid;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    border: 1px solid;\n"
                                                "    border-color: rgb(41, 213, 202);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "\n"
                                                "    \n"
                                                "}")
        self.add_to_potrebu.setObjectName("add_to_potrebu")
        self.add_to_potrebu.setText('Додати')
        self.verticalLayout.addWidget(self.add_to_potrebu)



        self.delete_potrebu = QtWidgets.QPushButton(self.frame_create_potr)
        self.delete_potrebu.setMinimumSize(QtCore.QSize(int(0 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        self.delete_potrebu.setMaximumSize(QtCore.QSize(int(260 * suma3/Ui_MainWindow.number), int(16777215 * suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.delete_potrebu.setFont(font)
        self.delete_potrebu.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "    border: 1px solid;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    border: 1px solid;\n"
                                                "    border-color: rgb(41, 213, 202);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "\n"
                                                "    \n"
                                                "}")
        self.delete_potrebu.setObjectName("delete_potrebu")
        self.delete_potrebu.setText('Видалити')
        self.verticalLayout.addWidget(self.delete_potrebu)
        spacerItem4 = QtWidgets.QSpacerItem(int(20 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_create_potr, 0, 1, 1, 1)
        self.frame_create_potr.hide()



        # форма3
        self.frame_create_recom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_create_recom.sizePolicy().hasHeightForWidth())
        self.frame_create_recom.setSizePolicy(sizePolicy)
        self.frame_create_recom.setMinimumSize(QtCore.QSize(int(300* suma3/Ui_MainWindow.number), int(540* suma3/Ui_MainWindow.number)))
        self.frame_create_recom.setMaximumSize(QtCore.QSize(int(800* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        self.frame_create_recom.setStyleSheet("QFrame{\n"
                                              f"    border-radius: {2* suma3/Ui_MainWindow.number}%;\n"
                                              f"    border: {2* suma3/Ui_MainWindow.number}px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              "}")
        self.frame_create_recom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_create_recom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_create_recom.setObjectName("frame_create_recom")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_create_recom)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_recom = QtWidgets.QLabel(self.frame_create_recom)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_recom.setFont(font)
        self.label_recom.setStyleSheet("QLabel{\n"
                                               "    border: 0px;\n"
                                               "}")
        self.label_recom.setObjectName("label_recom")
        self.label_recom.setText('Виберіть методику:')

        self.verticalLayout.addWidget(self.label_recom)
        self.comboBox_recom_create = QtWidgets.QComboBox(MainWindow)
        self.comboBox_recom_create.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_recom_create.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_recom_create.setFont(font)
        self.comboBox_recom_create.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                                  "")
        self.comboBox_recom_create.setObjectName("comboBox_recom_create")
        self.verticalLayout.addWidget(self.comboBox_recom_create)
        spacerItem = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(10* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.add_recom = QtWidgets.QLineEdit(self.frame_create_recom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_recom.sizePolicy().hasHeightForWidth())
        self.add_recom.setSizePolicy(sizePolicy)
        self.add_recom.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_recom.setFont(font)
        self.add_recom.setStyleSheet("QLineEdit{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.add_recom.setObjectName("add_recom")
        self.verticalLayout.addWidget(self.add_recom)
        spacerItem1 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)

        self.Show_recom = QtWidgets.QPushButton(self.frame_create_potr)
        self.Show_recom.setMinimumSize(
                QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.Show_recom.setMaximumSize(
                QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.Show_recom.setFont(font)
        self.Show_recom.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "    border: 1px solid;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "\n"
                                              "    \n"
                                              "}")
        self.Show_recom.setObjectName("add_to_potrebu_recom")
        self.Show_recom.setText('Завантажити групи')
        self.verticalLayout.addWidget(self.Show_recom)
        self.Show_recom.hide()

        self.comboBox_grups_recomendacii = QtWidgets.QComboBox(MainWindow)
        self.comboBox_grups_recomendacii.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_grups_recomendacii.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_grups_recomendacii.setFont(font)
        self.comboBox_grups_recomendacii.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                          "")
        self.comboBox_grups_recomendacii.setObjectName("comboBox_grups_recomendacii")

        self.verticalLayout.addWidget(self.comboBox_grups_recomendacii)
        spacerItem2 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(10* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.File_save_recom = QtWidgets.QCheckBox(self.frame_create_recom)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.File_save_recom.setFont(font)
        self.File_save_recom.setObjectName("File_save_recom")
        self.File_save_recom.setText('Зберегти файлом?')
        self.verticalLayout.addWidget(self.File_save_recom)
        spacerItem3 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.add_to_recom = QtWidgets.QPushButton(self.frame_create_recom)
        self.add_to_recom.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.add_to_recom.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.add_to_recom.setFont(font)
        self.add_to_recom.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "    border: 1px solid;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    border: 1px solid;\n"
                                                "    border-color: rgb(41, 213, 202);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "\n"
                                                "    \n"
                                                "}")
        self.add_to_recom.setObjectName("add_to_recom")
        self.add_to_recom.setText('Додати')
        self.verticalLayout.addWidget(self.add_to_recom)
        self.delete_recom = QtWidgets.QPushButton(self.frame_create_recom)
        self.delete_recom.setMinimumSize(QtCore.QSize(int(0* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.delete_recom.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.delete_recom.setFont(font)
        self.delete_recom.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "    border: 1px solid;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    border: 1px solid;\n"
                                                "    border-color: rgb(41, 213, 202);\n"
                                                f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                "\n"
                                                "    \n"
                                                "}")
        self.delete_recom.setObjectName("delete_recom")
        self.delete_recom.setText('Видалити')
        self.verticalLayout.addWidget(self.delete_recom)
        spacerItem4 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_create_recom, 0, 1, 1, 1)
        self.frame_create_recom.hide()

        # форма4

        self.freme_chenge = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freme_chenge.sizePolicy().hasHeightForWidth())
        self.freme_chenge.setSizePolicy(sizePolicy)
        self.freme_chenge.setMinimumSize(QtCore.QSize(int(300* suma3/Ui_MainWindow.number), int(0* suma3/Ui_MainWindow.number)))
        self.freme_chenge.setMaximumSize(QtCore.QSize(int(540* suma3/Ui_MainWindow.number), int(2000* suma3/Ui_MainWindow.number)))
        self.freme_chenge.setStyleSheet("QFrame{\n"
                                        f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                        f"    border: {2* suma3/Ui_MainWindow.number}px solid;\n"
                                        "    border-color: rgb(41, 213, 202);\n"
                                        "}")
        self.freme_chenge.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.freme_chenge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freme_chenge.setObjectName("freme_chenge")
        self.widget = QtWidgets.QWidget(self.freme_chenge)
        self.widget.setGeometry(QtCore.QRect(int(17* suma3/Ui_MainWindow.number), int(11* suma3/Ui_MainWindow.number), int(270* suma3/Ui_MainWindow.number), int(570* suma3/Ui_MainWindow.number)))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_chenge = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_chenge.setFont(font)
        self.label_chenge.setStyleSheet("QLabel{\n"
                                   "    border: 0px;\n"
                                   "}")
        self.label_chenge.setObjectName("label_chenge")
        self.label_chenge.setText('Методика обстеження')
        self.verticalLayout.addWidget(self.label_chenge)
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.chenge_to_metoduk = QtWidgets.QPushButton(self.widget)
        self.chenge_to_metoduk.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.chenge_to_metoduk.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.chenge_to_metoduk.setFont(font)
        self.chenge_to_metoduk.setText('Показати методику')
        self.chenge_to_metoduk.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.chenge_to_metoduk.setObjectName("chenge_to_metoduk")
        self.verticalLayout.addWidget(self.chenge_to_metoduk)
        spacerItem1 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.label_potreba = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_potreba.setFont(font)
        self.label_potreba.setStyleSheet("QLabel{\n"
                                         "    border: 0px;\n"
                                         "}")
        self.label_potreba.setObjectName("label_potreba")
        self.label_potreba.setText('Потреби:')
        self.verticalLayout.addWidget(self.label_potreba)
        self.comboBox_potrebu = QtWidgets.QComboBox(MainWindow)
        self.comboBox_potrebu.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_potrebu.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_potrebu.setFont(font)
        self.comboBox_potrebu.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                            "")
        self.comboBox_potrebu.setObjectName("comboBox_potrebu")
        self.verticalLayout.addWidget(self.comboBox_potrebu)
        spacerItem2 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.show_potrebu = QtWidgets.QPushButton(self.widget)
        self.show_potrebu.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.show_potrebu.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.show_potrebu.setFont(font)
        self.show_potrebu.setText('Показати потреби')
        self.show_potrebu.setStyleSheet("QPushButton{\n"
                                        "    \n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                        "    border: 1px solid;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    border: 1px solid;\n"
                                        "    border-color: rgb(41, 213, 202);\n"
                                        f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                        "\n"
                                        "    \n"
                                        "}")
        self.show_potrebu.setObjectName("show_potrebu")
        self.verticalLayout.addWidget(self.show_potrebu)
        spacerItem3 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.label_recomendacii = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_recomendacii.setFont(font)
        self.label_recomendacii.setStyleSheet("QLabel{\n"
                                              "    border: 0px;\n"
                                              "}")
        self.label_recomendacii.setObjectName("label_recomendacii")
        self.label_recomendacii.setText('Рекомендації:')
        self.verticalLayout.addWidget(self.label_recomendacii)
        self.comboBox_recomendacii = QtWidgets.QComboBox(MainWindow)
        self.comboBox_recomendacii.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_recomendacii.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_recomendacii.setFont(font)
        self.comboBox_recomendacii.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                                 "")
        self.comboBox_recomendacii.setObjectName("comboBox_recomendacii")

        self.verticalLayout.addWidget(self.comboBox_recomendacii)
        spacerItem4 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)
        self.show_recomendacii = QtWidgets.QPushButton(self.widget)
        self.show_recomendacii.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.show_recomendacii.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.show_recomendacii.setFont(font)
        self.show_recomendacii.setText('Показати рекомендації')
        self.show_recomendacii.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.show_recomendacii.setObjectName("show_recomendacii")
        self.verticalLayout.addWidget(self.show_recomendacii)
        spacerItem5 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem5)

        self.label_grups = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_grups.setFont(font)
        self.label_grups.setStyleSheet("QLabel{\n"
                                       "    border: 0px;\n"
                                       "}")
        self.label_grups.setObjectName("label_grups")
        self.label_grups.setText('Грипи:')
        self.verticalLayout.addWidget(self.label_grups)
        self.comboBox_grups = QtWidgets.QComboBox(MainWindow)
        self.comboBox_grups.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_grups.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_grups.setFont(font)
        self.comboBox_grups.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                          "")
        self.comboBox_grups.setObjectName("comboBox_grups")

        self.verticalLayout.addWidget(self.comboBox_grups)
        spacerItem6 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem6)
        self.show_grups_metoduk = QtWidgets.QPushButton(self.widget)
        self.show_grups_metoduk.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.show_grups_metoduk.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.show_grups_metoduk.setFont(font)
        self.show_grups_metoduk.setText('Показати групи')
        self.show_grups_metoduk.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                              "    border: 1px solid;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                              "\n"
                                              "    \n"
                                              "}")
        self.show_grups_metoduk.setObjectName("show_grups_metoduk")
        self.verticalLayout.addWidget(self.show_grups_metoduk)

        self.label_anketa = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.label_anketa.setFont(font)
        self.label_anketa.setStyleSheet("QLabel{\n"
                                              "    border: 0px;\n"
                                              "}")
        self.label_anketa.setObjectName("label_recomendacii")
        self.label_anketa.setText('Анкета:')
        self.verticalLayout.addWidget(self.label_anketa)

        self.comboBox_anketa = QtWidgets.QComboBox(MainWindow)
        self.comboBox_anketa.setMinimumSize(QtCore.QSize(int(200 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.comboBox_anketa.setMaximumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.comboBox_anketa.setFont(font)
        self.comboBox_anketa.setStyleSheet(
            "QComboBox{\n"
            "    background-color: rgb(255, 255, 255);\n"
            f"    border-radius: {4 * suma3}%;\n"
            f"    border: 1px solid;\n"
            "}\n"
            "QComboBox:hover{"
            "border-color: rgb(41, 213, 202)"

            "}"
            "\n"
            "QAbstractItemView{\n"
            "  selection-color: black;\n"
            "  selection-background-color: #05F3CC ;\n"
            "  border: 0px ;\n"

            "}\n"
            "QComboBox::drop-down{\n"
            "  border: 0 ;\n"
            "}\n"
            "")
        self.comboBox_anketa.setObjectName("comboBox_anketa")
        self.verticalLayout.addWidget(self.comboBox_anketa)

        self.show_anketa = QtWidgets.QPushButton(self.widget)
        self.show_anketa.setMinimumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.show_anketa.setMaximumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.show_anketa.setFont(font)
        self.show_anketa.setText('Показати Анкету')
        self.show_anketa.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "    border: 1px solid;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "\n"
                                              "    \n"
                                              "}")
        self.show_anketa.setObjectName("show_anketa")
        self.verticalLayout.addWidget(self.show_anketa)


        self.gridLayout_2.addWidget(self.freme_chenge, 0, 1, 1, 1)
        self.freme_chenge.hide()

        # форма5
        self.frame_delete = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_delete.sizePolicy().hasHeightForWidth())
        self.frame_delete.setSizePolicy(sizePolicy)
        self.frame_delete.setMinimumSize(QtCore.QSize(int(300* suma3/Ui_MainWindow.number), int(540* suma3/Ui_MainWindow.number)))
        self.frame_delete.setMaximumSize(QtCore.QSize(int(800* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        self.frame_delete.setStyleSheet("QFrame{\n"
                                        f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                        f"    border: {2* suma3/Ui_MainWindow.number}px solid;\n"
                                        "    border-color: rgb(41, 213, 202);\n"
                                        "}")
        self.frame_delete.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_delete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_delete.setObjectName("frame_delete")
        self.frame_delete.hide()
        self.layoutWidget = QtWidgets.QWidget(self.frame_delete)
        self.layoutWidget.setGeometry(QtCore.QRect(int(19* suma3/Ui_MainWindow.number), int(9* suma3/Ui_MainWindow.number), int(271* suma3/Ui_MainWindow.number), int(527* suma3/Ui_MainWindow.number)))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    border: 0px;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.label_2.setText('Методика обстеження')
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_delete = QtWidgets.QComboBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_delete.sizePolicy().hasHeightForWidth())
        self.comboBox_delete.setSizePolicy(sizePolicy)
        self.comboBox_delete.setMinimumSize(QtCore.QSize(int(200* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.comboBox_delete.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.comboBox_delete.setFont(font)
        self.comboBox_delete.setStyleSheet(
                 "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                                           "")
        self.comboBox_delete.setObjectName("comboBox_delete")
        self.verticalLayout.addWidget(self.comboBox_delete)
        spacerItem = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.chenge_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.chenge_label.setFont(font)
        self.chenge_label.setText('Перейменувати методику')
        self.chenge_label.setStyleSheet("QLabel{\n"
                                        "    border: 0px;\n"
                                        "}")
        self.chenge_label.setObjectName("chenge_label")
        self.verticalLayout.addWidget(self.chenge_label)

        self.chenge_line_metoduk = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chenge_line_metoduk.sizePolicy().hasHeightForWidth())
        self.chenge_line_metoduk.setSizePolicy(sizePolicy)
        self.chenge_line_metoduk.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.chenge_line_metoduk.setFont(font)
        self.chenge_line_metoduk.setPlaceholderText('Нова назава:')
        self.chenge_line_metoduk.setStyleSheet("QLineEdit{\n"
                                               "    \n"
                                               "    background-color: rgb(255, 255, 255);\n"
                                               f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                               "    border: 1px solid;\n"
                                               "}\n"
                                               "QLineEdit:hover {\n"
                                               "    border: 1px solid;\n"
                                               "    border-color: rgb(41, 213, 202);\n"
                                               f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                               "\n"
                                               "    \n"
                                               "}")
        self.chenge_line_metoduk.setObjectName("chenge_line_metoduk")
        self.verticalLayout.addWidget(self.chenge_line_metoduk)

        spacerItem2 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.Doschilnul_chenge = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Doschilnul_chenge.setFont(font)
        self.Doschilnul_chenge.setObjectName("Doschilnul_chenge")
        self.Doschilnul_chenge.setText('Дошкільний вік')
        self.verticalLayout.addWidget(self.Doschilnul_chenge)
        self.School_chenge = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.School_chenge.setFont(font)
        self.School_chenge.setObjectName("School_chenge")
        self.School_chenge.setText('Шкільний вік')
        self.verticalLayout.addWidget(self.School_chenge)
        spacerItem3 = QtWidgets.QSpacerItem(int(20* suma3/Ui_MainWindow.number), int(13* suma3/Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.new_nazva_metoduk = QtWidgets.QPushButton(self.layoutWidget)
        self.new_nazva_metoduk.setMinimumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.new_nazva_metoduk.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.new_nazva_metoduk.setFont(font)
        self.new_nazva_metoduk.setText('Зберегти назву')
        self.new_nazva_metoduk.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.new_nazva_metoduk.setObjectName("new_nazva_metoduk")
        self.verticalLayout.addWidget(self.new_nazva_metoduk)
        self.delete_metoduk_for_db = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_metoduk_for_db.setMinimumSize(QtCore.QSize(int(0* suma3/Ui_MainWindow.number), int(40* suma3/Ui_MainWindow.number)))
        self.delete_metoduk_for_db.setMaximumSize(QtCore.QSize(int(260* suma3/Ui_MainWindow.number), int(16777215* suma3/Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        self.delete_metoduk_for_db.setFont(font)
        self.delete_metoduk_for_db.setText('Видалити методику')
        self.delete_metoduk_for_db.setStyleSheet("QPushButton{\n"
                                                 "    \n"
                                                 "    background-color: rgb(255, 255, 255);\n"
                                                 f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                 "    border: 1px solid;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    border: 1px solid;\n"
                                                 "    border-color: rgb(41, 213, 202);\n"
                                                 f"    border-radius: {4* suma3/Ui_MainWindow.number}%;\n"
                                                 "\n"
                                                 "    \n"
                                                 "}")
        self.delete_metoduk_for_db.setObjectName("delete_metoduk_for_db")
        self.verticalLayout.addWidget(self.delete_metoduk_for_db)

        spacerItem20 = QtWidgets.QSpacerItem(int(20 * suma3 / Ui_MainWindow.number),
                                            int(13 * suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem20)

        self.new_nazva_anketa = QtWidgets.QPushButton(self.layoutWidget)
        self.new_nazva_anketa.setMinimumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.new_nazva_anketa.setMaximumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.new_nazva_anketa.setFont(font)
        self.new_nazva_anketa.setText('Зберегти Назву Анкети')
        self.new_nazva_anketa.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.new_nazva_anketa.setObjectName("new_nazva_anketa")
        self.verticalLayout.addWidget(self.new_nazva_anketa)

        self.delete_anketa_for_db = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_anketa_for_db.setMinimumSize(QtCore.QSize(int(0 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.delete_anketa_for_db.setMaximumSize(QtCore.QSize(int(260 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.delete_anketa_for_db.setFont(font)
        self.delete_anketa_for_db.setText('Видалити Анкету')
        self.delete_anketa_for_db.setStyleSheet("QPushButton{\n"
                                                 "    \n"
                                                 "    background-color: rgb(255, 255, 255);\n"
                                                 f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                                 "    border: 1px solid;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    border: 1px solid;\n"
                                                 "    border-color: rgb(41, 213, 202);\n"
                                                 f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                                 "\n"
                                                 "    \n"
                                                 "}")
        self.delete_anketa_for_db.setObjectName("delete_anketa_for_db")
        self.verticalLayout.addWidget(self.delete_anketa_for_db)

        spacerItem4 = QtWidgets.QSpacerItem(int(20 * suma3 / Ui_MainWindow.number),
                                            int(40 * suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_2.addWidget(self.frame_delete, 0, 1, 1, 1)
        # авторедагування
        self.frame_avtozapovnena = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_avtozapovnena.sizePolicy().hasHeightForWidth())
        self.frame_avtozapovnena.setSizePolicy(sizePolicy)
        self.frame_avtozapovnena.setMinimumSize(QtCore.QSize(int(300 * suma3 / Ui_MainWindow.number), int(0 * suma3 / Ui_MainWindow.number)))
        self.frame_avtozapovnena.setMaximumSize( QtCore.QSize(int(300 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        self.frame_avtozapovnena.setStyleSheet("QFrame{\n"
                                               f"    border-radius: {2 * suma3 / Ui_MainWindow.number}%;\n"
                                               f"    border: {2 * suma3 / Ui_MainWindow.number}px solid;\n"
                                               "    border-color: rgb(41, 213, 202);\n"
                                               "}")
        self.frame_avtozapovnena.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_avtozapovnena.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avtozapovnena.setObjectName("frame")
        self.frame_avtozapovnena.hide()
        self.gridLayout_avto = QtWidgets.QGridLayout(self.frame_avtozapovnena)
        self.gridLayout_avto.setObjectName("gridLayout_avto")
        self.label_irc = QtWidgets.QCheckBox(self.frame_avtozapovnena)
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        font.setBold(False)
        font.setWeight(50)
        self.label_irc.setFont(font)
        self.label_irc.setObjectName("label_irc")
        self.label_irc.setText( " Автоматизована система ІРЦ,\n використати попередній пароль?")
        self.gridLayout_avto.addWidget(self.label_irc)

        self.edit_URL = QtWidgets.QLineEdit(self.frame_avtozapovnena)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_URL.sizePolicy().hasHeightForWidth())
        self.edit_URL.setSizePolicy(sizePolicy)
        self.edit_URL.setMinimumSize(
                QtCore.QSize(int(250 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.edit_URL.setMaximumSize(
                QtCore.QSize(int(300 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.edit_URL.setFont(font)
        self.edit_URL.setStyleSheet("QLineEdit{\n"
                                    "    \n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                    "    border: 1px solid;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: rgb(41, 213, 202);\n"
                                    f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                    "\n"
                                    "    \n"
                                    "}")
        self.edit_URL.setObjectName("edit_URL")
        self.edit_URL.setPlaceholderText('URL:')
        self.gridLayout_avto.addWidget(self.edit_URL)

        self.login = QtWidgets.QLineEdit(self.frame_avtozapovnena)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(
                QtCore.QSize(int(250 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.login.setMaximumSize(
                QtCore.QSize(int(300 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.login.setFont(font)
        self.login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login.setStyleSheet("QLineEdit{\n"
                                 "    \n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                 "    border: 1px solid;\n"
                                 "}\n"
                                 "QLineEdit:hover {\n"
                                 "    border: 1px solid;\n"
                                 "    border-color: rgb(41, 213, 202);\n"
                                 f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                 "\n"
                                 "    \n"
                                 "}")
        self.login.setObjectName("login")
        self.login.setPlaceholderText('Логін:')
        self.gridLayout_avto.addWidget(self.login)

        self.password = QtWidgets.QLineEdit(self.frame_avtozapovnena)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(
                QtCore.QSize(int(250 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        self.password.setMaximumSize(
                QtCore.QSize(int(300 * suma3 / Ui_MainWindow.number), int(16777215 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit{\n"
                                    "    \n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                    "    border: 1px solid;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: rgb(41, 213, 202);\n"
                                    f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                    "\n"
                                    "    \n"
                                    "}")
        self.password.setObjectName("password")
        self.password.setPlaceholderText('Пароль:')
        self.gridLayout_avto.addWidget(self.password)

        self.label_metoduk = QtWidgets.QLabel(self.frame_avtozapovnena)
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        font.setBold(False)
        font.setWeight(50)
        self.label_metoduk.setFont(font)
        self.label_metoduk.setStyleSheet("QLabel{\n"
                                         "    border:0px;\n"
                                         "}")
        self.label_metoduk.setObjectName("label_metoduk")
        self.label_metoduk.setText('Методика обстеження:')
        self.gridLayout_avto.addWidget(self.label_metoduk)

        self.comboBox_site = QtWidgets.QComboBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_site.sizePolicy().hasHeightForWidth())
        self.comboBox_site.setSizePolicy(sizePolicy)
        self.comboBox_site.setMinimumSize( QtCore.QSize(int(270 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.comboBox_site.setFont(font)
        self.comboBox_site.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                f"    border: 1px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"

                "}"
                "\n"
                "QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "  border: 0px ;\n"

                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
                "")
        self.comboBox_site.setObjectName("comboBox_site")
        self.gridLayout_avto.addWidget(self.comboBox_site)
        spacerItem10 = QtWidgets.QSpacerItem(int(20 * suma3 / Ui_MainWindow.number),
                                             int(50 * suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_avto.addItem(spacerItem10)

        self.btn_kompetencia_2 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_kompetencia_2.setMinimumSize( QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_kompetencia_2.setFont(font)
        self.btn_kompetencia_2.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.btn_kompetencia_2.setObjectName("btn_kompetencia_2")
        self.btn_kompetencia_2.setText('Додати в компетенцію')
        self.gridLayout_avto.addWidget(self.btn_kompetencia_2)

        self.btn_potrebu_2 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_potrebu_2.setMinimumSize(QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_potrebu_2.setFont(font)
        self.btn_potrebu_2.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                         "    border: 1px solid;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    border: 1px solid;\n"
                                         "    border-color: rgb(41, 213, 202);\n"
                                         f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                         "\n"
                                         "    \n"
                                         "}")
        self.btn_potrebu_2.setObjectName("btn_potrebu_2")
        self.btn_potrebu_2.setText('Додати в потреби')
        self.gridLayout_avto.addWidget(self.btn_potrebu_2)

        self.btn_recomendacii_2 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_recomendacii_2.setMinimumSize(QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_recomendacii_2.setFont(font)
        self.btn_recomendacii_2.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "    border: 1px solid;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "\n"
                                              "    \n"
                                              "}")
        self.btn_recomendacii_2.setObjectName("btn_recomendacii_2")
        self.btn_recomendacii_2.setText('Додати в рекомендації')
        self.gridLayout_avto.addWidget(self.btn_recomendacii_2)

        spacerItem_avto = QtWidgets.QSpacerItem(int(20 * suma3 / Ui_MainWindow.number),
                                                int(10 * suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_avto.addItem(spacerItem_avto)

        self.btn_kompetencia_3 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_kompetencia_3.setMinimumSize(QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_kompetencia_3.setFont(font)
        self.btn_kompetencia_3.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "    border: 1px solid;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    border: 1px solid;\n"
                                             "    border-color: rgb(41, 213, 202);\n"
                                             f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                             "\n"
                                             "    \n"
                                             "}")
        self.btn_kompetencia_3.setObjectName("btn_kompetencia_2")
        self.btn_kompetencia_3.setText('Видалити компетенцію')
        self.gridLayout_avto.addWidget(self.btn_kompetencia_3)

        self.btn_potrebu_3 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_potrebu_3.setMinimumSize(QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_potrebu_3.setFont(font)
        self.btn_potrebu_3.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                         "    border: 1px solid;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    border: 1px solid;\n"
                                         "    border-color: rgb(41, 213, 202);\n"
                                         f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                         "\n"
                                         "    \n"
                                         "}")
        self.btn_potrebu_3.setObjectName("btn_potrebu_2")
        self.btn_potrebu_3.setText('Видалити потреби')
        self.gridLayout_avto.addWidget(self.btn_potrebu_3)

        self.btn_recomendacii_3 = QtWidgets.QPushButton(self.frame_avtozapovnena)
        self.btn_recomendacii_3.setMinimumSize(QtCore.QSize(int(130 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14 / Ui_MainWindow.number))
        self.btn_recomendacii_3.setFont(font)
        self.btn_recomendacii_3.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "    border: 1px solid;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgb(41, 213, 202);\n"
                                              f"    border-radius: {4 * suma3 / Ui_MainWindow.number}%;\n"
                                              "\n"
                                              "    \n"
                                              "}")
        self.btn_recomendacii_3.setObjectName("btn_recomendacii_2")
        self.btn_recomendacii_3.setText('Видалити рекомендації')
        self.gridLayout_avto.addWidget(self.btn_recomendacii_3)

        self.gridLayout_2.addWidget(self.frame_avtozapovnena, int(0), int(1), int(1), int(1))

        # створити опитування

        self.frame_create_oputyvana = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_create_oputyvana.sizePolicy().hasHeightForWidth())
        self.frame_create_oputyvana.setSizePolicy(sizePolicy)
        self.frame_create_oputyvana.setMinimumSize(QtCore.QSize(int(300* suma3 / Ui_MainWindow.number), int(540* suma3 / Ui_MainWindow.number)))
        self.frame_create_oputyvana.setMaximumSize(QtCore.QSize(int(300* suma3 / Ui_MainWindow.number), int(16777215* suma3 / Ui_MainWindow.number)))
        self.frame_create_oputyvana.setStyleSheet("QFrame{\n"
                                                  f"    border-radius: {2* suma3 / Ui_MainWindow.number}%;\n"
                                                  "    border: 2px solid;\n"
                                                  "    border-color: rgb(41, 213, 202);\n"
                                                  "}")
        self.frame_create_oputyvana.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_create_oputyvana.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_create_oputyvana.setObjectName("frame_create_oputyvana")
        self.layoutWidget = QtWidgets.QWidget(self.frame_create_oputyvana)
        self.layoutWidget.setGeometry(QtCore.QRect(int(12* suma3 / Ui_MainWindow.number), int(8* suma3 / Ui_MainWindow.number), int(275* suma3 / Ui_MainWindow.number), int(523* suma3 / Ui_MainWindow.number)))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nazva_oputyvana = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nazva_oputyvana.sizePolicy().hasHeightForWidth())
        self.nazva_oputyvana.setSizePolicy(sizePolicy)
        self.nazva_oputyvana.setMinimumSize(QtCore.QSize(int(260* suma3 / Ui_MainWindow.number), int(40* suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        self.nazva_oputyvana.setFont(font)
        self.nazva_oputyvana.setStyleSheet("QLineEdit{\n"
                                           "    \n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                           "    border: 1px solid;\n"
                                           "}\n"
                                           "QLineEdit:hover {\n"
                                           "    border: 1px solid;\n"
                                           "    border-color: rgb(41, 213, 202);\n"
                                           "    border-radius: 2%;\n"
                                           "\n"
                                           "    \n"
                                           "}")
        self.nazva_oputyvana.setPlaceholderText('Назва опитування')
        self.nazva_oputyvana.setObjectName("nazva_oputyvana")
        self.verticalLayout.addWidget(self.nazva_oputyvana)
        self.add_putana = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_putana.sizePolicy().hasHeightForWidth())
        self.add_putana.setSizePolicy(sizePolicy)
        self.add_putana.setMinimumSize(QtCore.QSize(int(260* suma3 / Ui_MainWindow.number), int(40* suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        self.add_putana.setFont(font)
        self.add_putana.setStyleSheet("QLineEdit{\n"
                                      "    \n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                      "    border: 1px solid;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 1px solid;\n"
                                      "    border-color: rgb(41, 213, 202);\n"
                                      f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                      "\n"
                                      "    \n"
                                      "}")
        self.add_putana.setPlaceholderText('Питання')
        self.add_putana.setObjectName("add_putana")
        self.verticalLayout.addWidget(self.add_putana)
        spacerItem = QtWidgets.QSpacerItem(int(20* suma3 / Ui_MainWindow.number), int(13* suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.School_oputyvana = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(int(50 / Ui_MainWindow.number))
        self.School_oputyvana.setFont(font)
        self.School_oputyvana.setObjectName("School_oputyvana")
        self.School_oputyvana.setText('Шкільний вік')
        self.verticalLayout.addWidget(self.School_oputyvana)
        self.Doschilnul_oputyvana = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Doschilnul_oputyvana.setFont(font)
        self.Doschilnul_oputyvana.setObjectName("Doschilnul_oputyvana")
        self.Doschilnul_oputyvana.setText('Дошкільний вік')
        self.verticalLayout.addWidget(self.Doschilnul_oputyvana)
        spacerItem1 = QtWidgets.QSpacerItem(int(20* suma3 / Ui_MainWindow.number), int(13* suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.File_save_oputyvana = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.File_save_oputyvana.setFont(font)
        self.File_save_oputyvana.setObjectName("File_save_oputyvana")
        self.File_save_oputyvana.setText('Зберегти файлом')
        self.verticalLayout.addWidget(self.File_save_oputyvana)
        spacerItem2 = QtWidgets.QSpacerItem(int(20* suma3 / Ui_MainWindow.number), int(13* suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.add_oputyvana = QtWidgets.QPushButton(self.layoutWidget)
        self.add_oputyvana.setMinimumSize(QtCore.QSize(int(0* suma3 / Ui_MainWindow.number), int(40* suma3 / Ui_MainWindow.number)))
        self.add_oputyvana.setMaximumSize(QtCore.QSize(int(260* suma3 / Ui_MainWindow.number), int(16777215* suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        self.add_oputyvana.setFont(font)
        self.add_oputyvana.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                         "    border: 1px solid;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    border: 1px solid;\n"
                                         "    border-color: rgb(41, 213, 202);\n"
                                         f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                         "\n"
                                         "    \n"
                                         "}")
        self.add_oputyvana.setObjectName("add_oputyvana")
        self.add_oputyvana.setText('Додати')
        self.verticalLayout.addWidget(self.add_oputyvana)
        self.delete_oputyvana = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_oputyvana.setMinimumSize(QtCore.QSize(int(0* suma3 / Ui_MainWindow.number), int(40* suma3 / Ui_MainWindow.number)))
        self.delete_oputyvana.setMaximumSize(QtCore.QSize(int(260* suma3 / Ui_MainWindow.number), int(16777215* suma3 / Ui_MainWindow.number)))
        font = QtGui.QFont()
        font.setPointSize(int(14/ Ui_MainWindow.number))
        self.delete_oputyvana.setFont(font)
        self.delete_oputyvana.setStyleSheet("QPushButton{\n"
                                            "    \n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                            "    border: 1px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 1px solid;\n"
                                            "    border-color: rgb(41, 213, 202);\n"
                                            f"    border-radius: {4* suma3 / Ui_MainWindow.number}%;\n"
                                            "\n"
                                            "    \n"
                                            "}")
        self.delete_oputyvana.setObjectName("delete_oputyvana")
        self.delete_oputyvana.setText('Видалити')
        self.verticalLayout.addWidget(self.delete_oputyvana)
        spacerItem3 = QtWidgets.QSpacerItem(int(20* suma3 / Ui_MainWindow.number), int(250* suma3 / Ui_MainWindow.number), QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.frame_create_oputyvana, 0, 1, 1, 1)
        self.frame_create_oputyvana.hide()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.chenge_number = 0
        self.create_number = 0
        self.potreba_number = 0
        self.delete_number = 0
        self.rekomendacii_number = 0
        self.save_material = None
        self.rozmir = 0
        self.qestion = [ ]
        self.potreba_recomendacii = [ ]
        self.grup = [ ]
        self.count = 0
        self.all_metoduk = [ ]
        self.text_combo = None
        self.metoduk_con = [ ]
        self.potrebu_con = [ ]
        self.rekomendacii_con = [ ]
        self.grups_con = [ ]
        self.list_grupAll = [ ]
        self.id_grup_qestion = [ ]
        self.id_list_grup_for_table = [ ]
        self.chenge_list = [ ]
        self.index_delete = [ ]
        self.table = None
        self.site=0
        self.oputyvana=0
        self.delete_avto=None
        self.delete_or_add=None
        self.delete_grups_eror=None
        self.list_oputyvaba=[]
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create an Estimate"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Змінити"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Група"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Del"))
        self.School.setText(_translate("MainWindow", "Шкільний вік"))
        self.Doschilnul.setText(_translate("MainWindow", "Дошкільний вік"))
        self.add_to_metoduk.setText(_translate("MainWindow", "Додати"))
        self.delete_qestion.setText(_translate("MainWindow", "Видалити"))
        self.minus.clicked.connect(lambda: self.rozmir_window('-'))
        self.plus.clicked.connect(lambda: self.rozmir_window('+'))
        self.add_metoduk.clicked.connect(self.create_metoduk)
        self.potreba.clicked.connect(lambda: self.create_potreba())
        # self.Show_potreb.clicked.connect(lambda: self.show_grups('p'))
        # self.Show_recom.clicked.connect(lambda: self.show_grups('r'))
        self.rekomendacii.clicked.connect(lambda: self.create_rekomendacii())
        self.chenge.clicked.connect(self.chenge_metoduk)
        self.delete_metoduk.clicked.connect(self.delete_metodub_is_db)
        self.save.clicked.connect(self.save_all)
        self.add_to_metoduk.clicked.connect(self.add_to_table_qestion_and_grup)
        self.delete_qestion.clicked.connect(self.delete_qestion_to_metoduk)
        self.add_to_potrebu.clicked.connect(lambda:self.add_potrebu_and_recomendacii('p'))
        self.delete_potrebu.clicked.connect(self.potreba_recomendacii_delete)
        self.add_to_recom.clicked.connect(lambda:self.add_potrebu_and_recomendacii('r'))
        self.delete_recom.clicked.connect(self.potreba_recomendacii_delete)
        self.chenge_to_metoduk.clicked.connect(lambda: self.show_chenge('k'))
        self.show_potrebu.clicked.connect(lambda: self.show_chenge('p'))
        self.show_recomendacii.clicked.connect(lambda: self.show_chenge('r'))
        self.show_grups_metoduk.clicked.connect(lambda: self.show_chenge('g'))
        self.show_anketa.clicked.connect(lambda: self.show_chenge('a'))
        self.del_che.clicked.connect(self.delete_chenge)
        self.add_che.clicked.connect(self.add_chenge_to_row)
        self.delete_metoduk_for_db.clicked.connect(lambda:self.delete_all_metoduk('del_metoduk_db'))
        self.new_nazva_metoduk.clicked.connect(self.delete_nazva)
        self.update_btn_avto.clicked.connect(lambda:self.site_metoduk())
        self.btn_kompetencia_2.clicked.connect(lambda: self.selenium_metoduk('k'))
        self.btn_potrebu_2.clicked.connect(lambda: self.selenium_metoduk('p'))
        self.btn_recomendacii_2.clicked.connect(lambda: self.selenium_metoduk('r'))
        self.btn_kompetencia_3.clicked.connect(lambda: self.selenium_metoduk('k_d'))
        self.btn_potrebu_3.clicked.connect(lambda: self.selenium_metoduk('p_d'))
        self.btn_recomendacii_3.clicked.connect(lambda: self.selenium_metoduk('r_d'))
        self.create_qestions.clicked.connect(self.oputyvana_create_update)
        self.add_oputyvana.clicked.connect(self.add_oputyvalnuk)
        self.delete_oputyvana.clicked.connect(self.delete_putana_oputyvana)
        self.new_nazva_anketa.clicked.connect(lambda: self.delete_nazva('del_anketa'))
        self.delete_anketa_for_db.clicked.connect(lambda: self.delete_all_metoduk('del_anketa_db'))
        self.error.clicked.connect(self.hide_error)
        self.comboBox_potrebu_create.activated.connect(lambda: self.curent_add_grup_potrebu('p'))
        self.comboBox_recom_create.activated.connect(lambda: self.curent_add_grup_potrebu('r'))

    def curent_add_grup_potrebu(self, x):
        try:
            if x == 'p':
                self.show_grups('p')
            elif x == 'r':
                self.show_grups('r')
        except Exception as ex:
            print('curent_id potrebu', ex)

    def hide_error(self):
        self.error.hide()

    def mesage_output(self, x):
        try:
            msgBox = QMessageBox()
            msgBox.setWindowFlag(Qt.FramelessWindowHint)
            msgBox.setIcon(QMessageBox.Information)


            if x == 'save_anketa':
                msgBox.setText("ERROR save_anketa"+'\n'+'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'delete_putana_oputyvana':
                msgBox.setText("ERROR delete_putana_oputyvana" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='add_oputyvalnuk':
                msgBox.setText("ERROR add_oputyvalnuk" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='selenium_metoduk':
                msgBox.setText("ERROR selenium_metoduk" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='conect_delete':
                msgBox.setText("ERROR conect_delete" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='delete_nazva':
                msgBox.setText("ERROR delete_nazva" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='update_qestions_potreb_recomendacii':
                msgBox.setText("ERROR update_qestions_potreb_recomendacii" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='update_anketa':
                msgBox.setText("ERROR update_anketa" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x=='update_grups':
                msgBox.setText("ERROR update_grups" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'add_chenge_to_row':
                msgBox.setText("ERROR add_chenge_to_row" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'delete_chenge':
                msgBox.setText("ERROR delete_chenge" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'delete':
                msgBox.setText("ERROR delete" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'checge_connect':
                msgBox.setText("ERROR checge_connect" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'chenge_table_all':
                msgBox.setText("ERROR chenge_table_all" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'show_grups_table':
                msgBox.setText("ERROR show_grups_table" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'show_anketa_table':
                msgBox.setText("ERROR show_anketa_table" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'show_chenge':
                msgBox.setText("ERROR show_chenge" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'potreba_recomendacii_delete':
                msgBox.setText("ERROR potreba_recomendacii_delete" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'add_potrebu_and_recomendacii':
                msgBox.setText("ERROR add_potrebu_and_recomendacii" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'delete_qestion_to_metoduk':
                msgBox.setText("ERROR delete_row_k_p_r" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'add_to_table_qestion_and_grup':
                msgBox.setText("ERROR delete_child" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'save_potrebu_recomendscii':
                msgBox.setText("ERROR save_potrebu_recomendscii" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'save_kompetencia':
                msgBox.setText("ERROR save_kompetencia" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'show_grups':
                msgBox.setText("ERROR all_dani_children" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'create_rekomendacii':
                msgBox.setText("ERROR create_rekomendacii" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'create_potreba':
                msgBox.setText("ERROR create_potreba" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'create_metoduk':
                msgBox.setText("ERROR create_metoduk" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'con_nazva_metoduk':
                msgBox.setText("ERROR con_nazva_metoduk" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")
            elif x == 'save_all':
                msgBox.setText("ERROR save_all" + '\n' + 'Перезаватажте програму')
                msgBox.setWindowTitle("ERROR")



            font = QtGui.QFont()
            font.setPointSize(14)
            msgBox.setFont(font)
            msgBox.setStyleSheet('QMessageBox{'
                                 'background-color: white;'
                                 f'border-radius: {7 * suma3}%;'
                                 'border: 2px solid;'
                                 '}'
                                 "QPushButton{min-width: 100px;}"
                                 )
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok and x == 'save_anketa':
                pass
            elif   returnValue == QMessageBox.Ok and x == 'delete_putana_oputyvana':
                pass
            elif returnValue == QMessageBox.Ok and x=='add_oputyvalnuk':
                pass
            elif returnValue == QMessageBox.Ok and x == 'selenium_metoduk':
                pass
            elif returnValue == QMessageBox.Ok and x == 'conect_delete':
                pass
            elif returnValue == QMessageBox.Ok and x == 'delete_nazva':
                pass
            elif returnValue == QMessageBox.Ok and x == 'update_qestions_potreb_recomendacii':
                pass
            elif returnValue == QMessageBox.Ok and x == 'update_anketa':
                pass
            elif returnValue == QMessageBox.Ok and x == 'update_grups':
                pass
            elif returnValue == QMessageBox.Ok and x == 'add_chenge_to_row':
                pass
            elif returnValue == QMessageBox.Ok and x == 'delete_chenge':
                pass
            elif returnValue == QMessageBox.Ok and x == 'delete':
                pass
            elif returnValue == QMessageBox.Ok and x == 'checge_connect':
                pass
            elif returnValue == QMessageBox.Ok and x == 'chenge_table_all':
                pass
            elif returnValue == QMessageBox.Ok and x == 'show_grups_table':
                pass
            elif returnValue == QMessageBox.Ok and x == 'show_anketa_table':
                pass
            elif returnValue == QMessageBox.Ok and x == 'show_chenge':
                pass
            elif returnValue == QMessageBox.Ok and x == 'potreba_recomendacii_delete':
                pass
            elif returnValue == QMessageBox.Ok and x == 'add_potrebu_and_recomendacii':
                pass
            elif returnValue == QMessageBox.Ok and x == 'delete_qestion_to_metoduk':
                pass
            elif returnValue == QMessageBox.Ok and x == 'add_to_table_qestion_and_grup':
                pass
            elif returnValue == QMessageBox.Ok and x == 'save_potrebu_recomendscii':
                pass
            elif returnValue == QMessageBox.Ok and x == 'save_kompetencia':
                pass
            elif returnValue == QMessageBox.Ok and x == 'show_grups':
                pass
            elif returnValue == QMessageBox.Ok and x == 'create_rekomendacii':
                pass
            elif returnValue == QMessageBox.Ok and x == 'create_potreba':
                pass
            elif returnValue == QMessageBox.Ok and x == 'create_metoduk':
                pass
            elif returnValue == QMessageBox.Ok and x == 'con_nazva_metoduk':
                pass
            elif returnValue == QMessageBox.Ok and x == 'save_all':
                pass

        except Exception as ex:
            print('mesage_output', ex)

    def save_anketa(self):
        self.previrka = 'ok'
        self.save.setIcon(QIcon('savergb.png'))
        self.save.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
        connect = sl.connect('IRCdb.db')
        if self.Doschilnul_oputyvana.isChecked():
            zaklad = self.Doschilnul_oputyvana.text().replace(' ', '_')
        elif self.School_oputyvana.isChecked():
            zaklad = self.School_oputyvana.text().replace(' ', '_')
        else:
            zaklad = ''
        nazva_metoduku = self.nazva_oputyvana.text().replace(' ', '_').replace(",", "_").replace("(", "").replace(")","").replace("'", "`")
        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {nazva_metoduku + "_" + zaklad}_Anketa'
                               f'(id INTEGER PRIMARY KEY, putana varchar(700));')
            with connect as con:
                cursor = con.cursor()
                let_grup = len(self.list_oputyvaba)
                for i in range(let_grup):
                    cursor.execute(f"""INSERT INTO {nazva_metoduku + "_" + zaklad}_Anketa  (putana) VALUES ('{self.list_oputyvaba[i]}') """)

        except Exception as ex:
            self.previrka = self.mesage_exept('kompetencia')
            self.error.show()
            self.mesage_output('save_anketa')
            print('save_anketa:', ex)
        if self.previrka == 'ERROR':
            self.save.setIcon(QIcon('save.png'))
            self.save.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
            pass
        else:
            if self.File_save_oputyvana.isChecked():
                filename = QFileDialog.getSaveFileName()
                self.path = filename[0]
                nazva_maoduku = self.nazva_metodulu.text()
                with open(f'{self.path + nazva_maoduku + zaklad}.txt', 'w', encoding='utf-8') as f:
                    if self.Doschilnul_oputyvana.isChecked():
                        f.write(self.Doschilnul_oputyvana.text() + '\n')
                    elif self.School_oputyvana.isChecked():
                        f.write(self.School_oputyvana.text() + '\n')
                    for i in range(len(self.list_oputyvaba)):
                        f.write(self.list_oputyvaba[i]+'\n')
            self.nazva_metodulu.clear()
            self.list_oputyvaba.clear()
            self.len = len(self.qestion)
            for i in range(self.len + 1):
                self.tableWidget.setRowCount(i)
            self.save.setIcon(QIcon('save.png'))
            self.save.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))

    def delete_putana_oputyvana(self):
        index = []
        try:
            for i in range(len(self.list_oputyvaba)):
                if self.tableWidget.cellWidget(i, 1).checkState():
                    index.append(self.tableWidget.item(i, 0).text())
            for i in index:
                c = i
                if c in self.list_oputyvaba:
                    index_del = self.list_oputyvaba.index(c)
                    self.list_oputyvaba.pop(index_del)

            for i in range(len(self.list_oputyvaba) + 1):
                self.tableWidget.setRowCount(i)

            for i in range(len(self.list_oputyvaba)):
                check = QtWidgets.QCheckBox()
                check.setStyleSheet("""
                                           QCheckBox:hover{
                                               background-color: rgb(41, 213, 202);
                                           }
                                           QCheckBox::indicator {
                                               width: 80px;
                                               height: 30px;
                                           }
                                       """)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(self.list_oputyvaba[i]))
                self.tableWidget.setCellWidget(i, 1, check)
            index.clear()

        except Exception as ex:
            self.error.show()
            self.mesage_output('delete_putana_oputyvana')
            print('delete_putana_oputyvana:', ex)

    def add_oputyvalnuk(self):
        try:
            if self.add_putana.text() == '':
                pass
            else:
                self.list_oputyvaba.append(self.add_putana.text().replace("'", "`"))

                self.add_putana.setText('')
                self.len = len(self.list_oputyvaba)
                for i in range(self.len + 1):
                    self.tableWidget.setRowCount(i)

                for i in range(self.len):
                    check = QtWidgets.QCheckBox()
                    check.setStyleSheet("""
                               QCheckBox:hover{
                                   background-color: rgb(41, 213, 202);
                               }
                               QCheckBox::indicator {
                                   width: 80px;
                                   height: 30px;
                               }
                           """)
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(self.list_oputyvaba[i]))
                    self.tableWidget.setCellWidget(i, 1, check)
        except Exception as ex:
            self.error.show()
            self.mesage_output('add_oputyvalnuk')
            print('add_oputyvalnuk', ex)

    def oputyvana_create_update(self):
        self.table_restart()
        row_result = self.tableWidget.rowCount()
        for i in range(row_result):
            self.tableWidget.removeRow(i)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Питання")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("clear")
        for i in range(row_result):
            self.tableWidget.removeRow(i)
        self.tableWidget.setColumnCount(2)
        if self.oputyvana==0:
            self.hide_widget()
            self.frame_create_oputyvana.show()
            self.oputyvana=1
            self.create_qestions.setIcon(QIcon('argb.png'))
            self.create_qestions.setIconSize(
                QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
        else:
            self.frame_create_oputyvana.hide()
            self.oputyvana=0
            self.create_qestions.setIcon(QIcon('a.png'))
            self.create_qestions.setIconSize(
                QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))

    def mesage_exept(self,x):
            msgBox = QMessageBox()
            msgBox.setWindowFlag(Qt.FramelessWindowHint)
            msgBox.setIcon(QMessageBox.Information)
            if x =='kompetencia':
                msgBox.setText('Помилка, перевірте розділові знаки та цифри в назві методики')
            msgBox.setStyleSheet('QMessageBox{'
                                 'background-color: white;'
                                 f'border-radius: {7 * suma3}%;'
                                 'border: 2px solid;'
                                 '}'
                                 )
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            return 'ERROR'

    def site_metoduk(self):
            self.comboBox_site.clear()
            if self.site == 0:
                    self.hide_widget()
                    self.site = 1
                    self.frame_avtozapovnena.show()
                    self.con_nazva_metoduk('site')
                    self.update_btn_avto.setIcon(QIcon('internet_rgb.png'))
                    self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
            else:
                    self.site = 0
                    self.frame_avtozapovnena.hide()
                    self.update_btn_avto.setIcon(QIcon('internet.png'))
                    self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))

    def selenium_metoduk(self,x):
        try:
            kompetencia_list = [ ]
            potrebu_list = [ ]
            recomendacii_list = [ ]
            login_user = self.login.text()
            password_user = self.password.text()
            url_user = self.edit_URL.text()
            metoduk = self.comboBox_site.currentText()
            self.btn_variant=None
            connect = sl.connect('IRCdb.db')

            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'DELETE FROM irc_selenium_kompetencia;')

            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'DELETE FROM irc_selenium_potrebu;')

            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'DELETE FROM irc_selenium_recomendacii;')

            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f"SELECT qestion FROM  {metoduk.replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'qestions'} ;")
                    for i in cursor:
                            KO_str = i
                            kompetencia = KO_str [ 0 ]
                            kompetencia_list.append(kompetencia)
            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f"SELECT potrebu FROM  {metoduk.replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'} ;")
                    for i in cursor:
                            KO_str = i
                            potrebu = KO_str [ 0 ]
                            potrebu_list.append(potrebu)
            with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f"SELECT recomendacii FROM  {metoduk.replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'} ;")
                    for i in cursor:
                            KO_str = i
                            recomendacii = KO_str [ 0 ]
                            recomendacii_list.append(recomendacii)

            if self.label_irc.isChecked():
                    with connect as con:
                            cursor = con.cursor()
                            cursor.execute(f' UPDATE irc_portal SET url_user="{url_user}" WHERE id=1;')
            else:
                    with connect as con:
                            cursor = con.cursor()
                            cursor.execute(f'DELETE FROM irc_portal;')

                    with connect as con:
                            cursor = con.cursor()
                            cursor.execute(
                                    f"""INSERT INTO irc_portal  (login_user, password_user, url_user) VALUES ('{login_user}', '{password_user}', '{url_user}') """)

            with connect as con:
                    cursor = con.cursor()
                    for i in range(len(kompetencia_list)):
                            cursor.execute(
                                    f"""INSERT INTO irc_selenium_kompetencia  (kompetencia_user) VALUES ('{kompetencia_list [ i ]}') """)

            with connect as con:
                    cursor = con.cursor()
                    for i in range(len(potrebu_list)):
                            cursor.execute(
                                    f"""INSERT INTO irc_selenium_potrebu  (potrebu_user) VALUES ('{potrebu_list [ i ]}') """)

            with connect as con:
                    cursor = con.cursor()
                    for i in range(len(recomendacii_list)):
                            cursor.execute(
                                    f"""INSERT INTO irc_selenium_recomendacii  (recomendacii_user) VALUES ('{recomendacii_list [ i ]}') """)

            if x == 'k':
                    self.delete_avto = 'k'
                    self.delete_or_add='add'
                    self.mesage()
            elif x == 'p':
                    self.delete_avto = 'p'
                    self.delete_or_add='add'
                    self.mesage()
            elif x == 'r':
                    self.delete_avto = 'r'
                    self.delete_or_add='add'
                    self.mesage()
            elif x == 'k_d':
                    self.delete_avto='k_d'
                    self.delete_or_add='delete'
                    self.mesage()
            elif x == 'p_d':
                    self.delete_avto='p_d'
                    self.delete_or_add='delete'
                    self.mesage()
            elif x == 'r_d':
                    self.delete_avto='r_d'
                    self.delete_or_add='delete'
                    self.mesage()

        except Exception as ex:
            self.error.show()
            self.mesage_output('selenium_metoduk')
            print('selenium_metoduk', ex)

    def conect_delete(self):
        try:
            self.comboBox_delete.clear()
            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                cursor.execute('SELECT name from sqlite_master where type= "table"')
                for i in cursor:
                    table = str(i).replace('(', '').replace(')', '').replace("'", '').replace(',', '')
                    if 'qestions' in table:
                        self.comboBox_delete.addItem(
                            table.replace('_', ' ').replace('qestions', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))
                    elif 'Anketa' in table:
                        self.comboBox_delete.addItem(
                            table.replace('_', ' ').replace('Anketa', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))
        except Exception as ex:
            self.error.show()
            self.mesage_output('conect_delete')
            print('conect_delete', ex)

    def delete_nazva(self, x):
        try:
            if x=='del_anketa':
                chenge_anketa = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'Anketa'
                delete_line_edit = self.chenge_line_metoduk.text().replace(" ", "_")
                age = None
                if self.School_chenge.isChecked():
                    age = self.School_chenge.text().replace(" ", "_")
                elif self.Doschilnul_chenge.isChecked():
                    age = self.Doschilnul_chenge.text().replace(" ", "_")
                connect = sl.connect('IRCdb.db')
                with connect as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT name from sqlite_master where type= "table"')
                    for i in cursor:
                        table = i[0]
                        if chenge_anketa in table:
                            with connect as con:
                                db = con.cursor()
                                db.execute(f'ALTER TABLE  {chenge_anketa} RENAME TO {delete_line_edit + "_" + age}Anketa;')
            else:
                chenge_qestions = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'qestions'
                chenge_potrebu = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'
                chenge_recomendacii = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'
                chenge_grups = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'grups'
                delete_line_edit = self.chenge_line_metoduk.text().replace(" ","_")
                age=None
                if self.School_chenge.isChecked():
                    age=self.School_chenge.text().replace(" ","_")
                elif self.Doschilnul_chenge.isChecked():
                    age=self.Doschilnul_chenge.text().replace(" ","_")

                connect = sl.connect('IRCdb.db')
                with connect as con:
                    cursor = con.cursor()
                    cursor.execute('SELECT name from sqlite_master where type= "table"')
                    for i in cursor:
                        table = str(i).replace('(', '').replace(')', '').replace("'", '').replace(',', '')
                        if chenge_grups in table:
                            print(chenge_grups)
                            with connect as con:
                                db = con.cursor()
                                db.execute(f'ALTER TABLE  {chenge_grups} RENAME TO {delete_line_edit + "_" + age}_grups;')
                        elif chenge_qestions in table:
                            print(chenge_qestions)
                            with connect as con:
                                db = con.cursor()
                                db.execute(f'ALTER TABLE  {chenge_qestions} RENAME TO {delete_line_edit + "_" + age}_qestions;')
                        elif chenge_potrebu in table:
                            with connect as con:
                                db = con.cursor()
                                db.execute(f'ALTER TABLE  {chenge_potrebu} RENAME TO {delete_line_edit + "_" + age}_potrebu;')
                            print(chenge_potrebu)
                        elif chenge_recomendacii in table:
                            print(chenge_recomendacii)
                            with connect as con:
                                db = con.cursor()
                                db.execute(f'ALTER TABLE  {chenge_recomendacii} RENAME TO {delete_line_edit + "_" + age}_recomendacii;')


                self.chenge_line_metoduk.clear()
            self.conect_delete()
        except Exception as ex:
            self.conect_delete()
            self.error.show()
            self.mesage_output('delete_nazva')
            print('delete_nazva',ex)

    def delete_all_metoduk(self, x):
        if x=='del_anketa_db':
            self.btn_variant = 'anketa_delit'
            self.delete_or_add=None
            self.delete_avto=None
            self.mesage()
        elif x=='del_metoduk_db':
            self.btn_variant = 't'
            self.delete_or_add=None
            self.delete_avto=None
            self.mesage()

    def update_qestions_potreb_recomendacii(self):
        try:
            text=None

            if self.btn_variant == 'k':
                text = self.comboBox.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'qestions'
            elif self.btn_variant == 'p':
                text = self.comboBox_potrebu.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'
            elif self.btn_variant == 'r':
                text = self.comboBox_recomendacii.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'


            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'DELETE FROM  {text};')
            c= self.tableWidget.rowCount()
            list_is_db=[]
            grups=[]
            with connect as con:
                cursor = con.cursor()
                for i in range(c):
                    if self.btn_variant == 'k':
                        cursor.execute(f"""SELECT id FROM {text.replace('qestions','grups')} WHERE grup='{self.tableWidget.cellWidget(i, 1).currentText().replace('----------',' ')}' """)
                    elif self.btn_variant == 'p':
                        cursor.execute(f"""SELECT id FROM {text.replace('potrebu','grups')} WHERE grup='{self.tableWidget.cellWidget(i, 1).currentText().replace('----------',' ')}' """)
                    elif self.btn_variant == 'r':
                        cursor.execute(f"""SELECT id FROM {text.replace('recomendacii','grups')} WHERE grup='{self.tableWidget.cellWidget(i, 1).currentText().replace('----------',' ')}' """)
                    id = cursor.fetchone()
                    id_grup = id[0]
                    list_is_db.append(self.tableWidget.item(i, 0).text().replace("'","`"))
                    grups.append(id_grup)
            with connect as con:
                cursor = con.cursor()
                for i in range(c):
                    if self.btn_variant == 'k':
                        cursor.execute(f"""INSERT INTO  {text} (qestion, grup_id) VALUES ('{list_is_db[i]}', {grups[i]}) """)
                    elif self.btn_variant == 'p':
                        cursor.execute(f"""INSERT INTO  {text} (potrebu, grup_id) VALUES ('{list_is_db[i]}', {grups[i]}) """)
                    elif self.btn_variant == 'r':
                        cursor.execute(f"""INSERT INTO  {text} (recomendacii, grup_id) VALUES ('{list_is_db[i]}', {grups[i]}) """)
            list_is_db.clear()
            grups.clear()
            self.mesage_ok()

        except Exception as ex:
            self.error.show()
            self.mesage_output('update_qestions_potreb_recomendacii')
            print('update_qestions_potreb_recomendacii:',ex)

    def update_anketa(self):
        try:
            text = None
            text = self.comboBox_anketa.currentText().replace('шкл.', 'Шкільний вік').replace('дош.', 'Дошкільний вік').replace(' ', '_') + 'Anketa'
            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'DELETE FROM  {text};')
            c = self.tableWidget.rowCount()
            list_is_db = []

            for i in range(c):
                list_is_db.append(self.tableWidget.item(i, 0).text().replace("'", "`"))
            with connect as con:
                cursor = con.cursor()
                for i in range(c):
                        cursor.execute(f"""INSERT INTO  {text} (putana) VALUES ('{list_is_db[i]}') """)
            list_is_db.clear()
            self.mesage_ok()
        except Exception as ex:
            self.error.show()
            self.mesage_output('update_anketa')
            print('update_anketa',ex)

    def update_grups(self):
        try:
            list_grups = [ ]
            text_grups = self.comboBox_grups.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ','_') + 'grups'
            print(text_grups)
            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                for i in range(len(self.index_delete)):
                    cursor.execute('pragma foreign_keys=on')
                    cursor.execute(f'DELETE FROM  {text_grups} WHERE id = {self.index_delete[i]};')
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT grup FROM  {text_grups};')
                for i in cursor:
                    string = str(i)
                    grup = string.replace(string [ 0 ], '').replace(string [ 1 ], '').replace(string [ -1 ], '').replace(string [ -2 ], '')
                    list_grups.append(grup)
            with connect as con:
                cursor = con.cursor()
                for i in range(len(list_grups)):
                    text_table_row = self.tableWidget.item(i, 0).text().replace("'", "`")
                    # text_table_row = self.tableWidget.item(i, 0).text().replace("'","`").replace("----------", " ")
                    if text_table_row=='----------':
                        text_table_row=' '
                    cursor.execute(f'UPDATE {text_grups} SET grup="{text_table_row}" WHERE grup="{list_grups[i]}";')
            c = self.tableWidget.rowCount()
            db_list = len(list_grups)
            cucl_insert = c-db_list
            c=db_list
            for i in range(cucl_insert):
                text_table_row_insert = self.tableWidget.item(c, 0).text().replace("'", "`")
                if text_table_row_insert == '----------':
                    text_table_row_insert = ' '
                # text_table_row_insert = self.tableWidget.item(c, 0).text().replace("'","`").replace("----------", " ")
                with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'INSERT INTO {text_grups} (grup) VALUES ("{text_table_row_insert}") ;')
                c+=1
            list_grups.clear()
            self.mesage_ok()

        except Exception as ex:
            self.error.show()
            self.mesage_output('update_grups')
            print('update_grups:', ex)

    def add_chenge_to_row(self):
        try:
            c= self.tableWidget.rowCount()
            self.tableWidget.setRowCount(c+1)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(' '))

            select = QtWidgets.QComboBox()
            font = QtGui.QFont()
            font.setPointSize(12)
            select.setStyleSheet(
                "QComboBox{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {3 * suma3}%;\n"
                f"    border: 2px solid;\n"
                "}\n"
                "QComboBox:hover{"
                "border-color: rgb(41, 213, 202)"
                "}"
                "\n"
                "QComboBox, QAbstractItemView{\n"
                "  selection-color: black;\n"
                "  selection-background-color: #05F3CC ;\n"
                "}\n"
                "QComboBox::drop-down{\n"
                "  border: 0 ;\n"
                "}\n"
    
                "")
            select.setFont(font)
            for i in range(len(self.list_grupAll)):
                select.addItem(self.list_grupAll [ i ])
            self.tableWidget.setCellWidget(c, 1, select)
            check = QtWidgets.QCheckBox()
            check.setStyleSheet("""
                                    QCheckBox:hover{
                                        background-color: rgb(41, 213, 202);
                                    }
                                    QCheckBox::indicator {
                                        width: 80px;
                                        height: 30px;
                                    }
                                """)
            if self.btn_variant=='g':
                self.tableWidget.setCellWidget(c, 1, check)
            elif self.btn_variant=='a':
                self.tableWidget.setCellWidget(c, 1, check)
            else:
                self.tableWidget.setCellWidget(c, 2, check)
            self.btn_delete = QtWidgets.QPushButton()
            font.setPointSize(12)
            self.btn_delete.setStyleSheet(
                "QPushButton{\n"
                "    background-color: rgb(255, 255, 255);\n"
                f"    border-radius: {3 * suma3}%;\n"
                f"    border: 2px solid;\n"
                "}\n"
                "QPushButton:hover{"
                "border-color: red;"
                "}"
                "\n"
                "}\n"
    
                "")
            self.btn_delete.setFont(font)
            self.btn_delete.setText('X')
            if self.btn_variant=='g':
                self.tableWidget.setCellWidget(c, 2, self.btn_delete)
            elif self.btn_variant=='a':
                self.tableWidget.setCellWidget(c, 2, self.btn_delete)
            else:
                self.tableWidget.setCellWidget(c, 3, self.btn_delete)

            self.btn_delete.clicked.connect(self.mesage)
        except Exception as ex:
            self.error.show()
            self.mesage_output('add_chenge_to_row')
            print('add_chenge_to_row', ex)

    def delete_chenge(self):
        try:
            text_grups = self.comboBox_grups.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'grups'
            c= self.tableWidget.rowCount()
            for i in range(c):
                if self.btn_variant=='g':
                    if self.tableWidget.cellWidget(i, 1).checkState():
                        text = self.tableWidget.item(i, 0).text()
                        connect = sl.connect('IRCdb.db')
                        with connect as con:
                            cursor = con.cursor()
                            cursor.execute(f'SELECT id FROM  {text_grups} WHERE grup="{text}";')
                            exsist = cursor.fetchone()
                            if exsist != None:
                                self.chenge_list.append(self.tableWidget.item(i, 0).text())
                        self.tableWidget.setItem(i, 0, QTableWidgetItem(''))
                        check = QtWidgets.QCheckBox()
                        check.setChecked(False)
                        check.setStyleSheet("""
                                                                                                                      QCheckBox:hover{
                                                                                                                          background-color: rgb(41, 213, 202);
                                                                                                                      }
                                                                                                                      QCheckBox::indicator {
                                                                                                                          width: 80px;
                                                                                                                          height: 30px;
                                                                                                                      }
                                                                                                                  """)
                        self.tableWidget.setCellWidget(i, 1, check)
                if self.btn_variant=='a':
                    if self.tableWidget.cellWidget(i, 1).checkState():
                        self.tableWidget.setItem(i, 0, QTableWidgetItem(''))
                        check = QtWidgets.QCheckBox()
                        check.setChecked(False)
                        check.setStyleSheet("""
                                                                                                                      QCheckBox:hover{
                                                                                                                          background-color: rgb(41, 213, 202);
                                                                                                                      }
                                                                                                                      QCheckBox::indicator {
                                                                                                                          width: 80px;
                                                                                                                          height: 30px;
                                                                                                                      }
                                                                                                                  """)
                        self.tableWidget.setCellWidget(i, 1, check)
                else:
                    if self.tableWidget.cellWidget(i, 2).checkState():
                        self.chenge_list.append(self.tableWidget.item(i, 0).text())
                        self.tableWidget.setItem(i, 0, QTableWidgetItem(''))
                        check = QtWidgets.QCheckBox()
                        check.setChecked(False)
                        check.setStyleSheet("""
                                                                                               QCheckBox:hover{
                                                                                                   background-color: rgb(41, 213, 202);
                                                                                               }
                                                                                               QCheckBox::indicator {
                                                                                                   width: 80px;
                                                                                                   height: 30px;
                                                                                               }
                                                                                           """)
                        self.tableWidget.setCellWidget(i, 2, check)

        except Exception as ex:
            self.error.show()
            self.mesage_output('delete_chenge')
            print('delete_chenge:',ex)

    def delete(self, x):
        try:
            if self.btn_variant=='g':
                text_grups = self.comboBox_grups.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'grups'
                for i in self.tableWidget.selectedIndexes():
                    index = i.row()
                    connect = sl.connect('IRCdb.db')
                    with connect as con:
                        cursor = con.cursor()
                        if self.tableWidget.item(index, 0).text()==" ":
                                self.delete_grups_eror='ERROR'
                                self.mesage_ok()
                                pass
                        else:
                                text = self.tableWidget.item(index, 0).text().replace('----------', ' ')
                                cursor.execute(f'SELECT id FROM  {text_grups} WHERE grup="{text}";')
                                for i in cursor:
                                    id = str(i)
                                    id_grup = id.replace(id [ 0 ], '').replace(id [ -1 ], '').replace(id [ -2 ], '')
                                    self.index_delete.append(id_grup)
                                self.tableWidget.removeRow(index)
            elif self.btn_variant=='t':
                delete_qestions = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'qestions'
                delete_potrebu = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'
                delete_recomendacii = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'
                delete_grups = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'grups'
                connect = sl.connect('IRCdb.db')
                with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'DROP TABLE IF EXISTS {delete_qestions};')
                    cursor.execute(f'DROP TABLE IF EXISTS {delete_potrebu};')
                    cursor.execute(f'DROP TABLE IF EXISTS {delete_recomendacii};')
                    cursor.execute(f'DROP TABLE IF EXISTS {delete_grups};')
                self.delete_nazva('nazva')
            elif self.btn_variant == 'anketa_delit':
                delete_anketa = self.comboBox_delete.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'Anketa'
                connect = sl.connect('IRCdb.db')
                with connect as con:
                    cursor = con.cursor()
                    cursor.execute(f'DROP TABLE IF EXISTS {delete_anketa};')
                self.delete_nazva('nazva')
            else:
                for i in self.tableWidget.selectedIndexes():
                    index = i.row()
                    self.tableWidget.removeRow(index)
        except Exception as ex:
            self.error.show()
            self.mesage_output('delete')
            print('delete', ex)

    def mesage_ok(self):
        msgBox = QMessageBox()
        msgBox.setWindowFlag(Qt.FramelessWindowHint)
        msgBox.setIcon(QMessageBox.Information)
        if  self.delete_grups_eror=='ERROR':
                msgBox.setText('Помилка')
                self.delete_grups_eror = None
        else:
                msgBox.setText('Збережено')
        msgBox.setStyleSheet('QMessageBox{'
                                'background-color: white;'
                                f'border-radius: {7 * suma3}%;'
                                'border: 2px solid;'
                             '}'
                             )
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()

    def mesage(self):
        msgBox = QMessageBox()
        msgBox.setWindowFlag(Qt.FramelessWindowHint)
        msgBox.setIcon(QMessageBox.Information)

        for i in self.tableWidget.selectedIndexes():
            index = i.row()
            msgBox.setText("Видалити? "+self.tableWidget.item(index,0).text())
        if self.delete_or_add=='add':
                msgBox.setText('Ви бажаєте додати методику? ' + self.comboBox_site.currentText())
        elif self.delete_or_add=='delete':
                msgBox.setText('Ви бажаєте видалити методику? ' + self.comboBox_site.currentText())
        elif self.btn_variant=='t':
            msgBox.setText('Видалити методику? '+self.comboBox_delete.currentText())
        elif self.btn_variant == 'anketa_delit':
            msgBox.setText('Видалити анкету? ' + self.comboBox_delete.currentText())
        print(self.delete_or_add)
        msgBox.setWindowTitle("Видалення")
        msgBox.setStyleSheet('QMessageBox{'
                                'background-color: white;'
                                f'border-radius: {7 * suma3}%;'
                                'border: 2px solid;'
                             '}'
                             )
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok and self.delete_avto=='k':
            self.add_kompetencia_auto()
        elif returnValue == QMessageBox.Ok and self.delete_avto == 'p':
            self.add_potrebu_auto()
        elif returnValue == QMessageBox.Ok and self.delete_avto == 'r':
            self.add_recocomendacii_auto()
        elif returnValue == QMessageBox.Ok and self.delete_avto=='k_d':
            self.delete_kompetencia_auto()
        elif returnValue == QMessageBox.Ok and self.delete_avto=='p_d':
            self.delete_potrebu_auto()
        elif returnValue == QMessageBox.Ok and self.delete_avto=='r_d':
            self.delete_recomendacii_auto()
        elif returnValue == QMessageBox.Ok:
            self.delete('del')

    def add_kompetencia_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        kompetencia_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",'')
            login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT kompetencia_user FROM  irc_selenium_kompetencia ;')
                for i in cursor:
                    KO_str = i
                    kompetencia = KO_str [ 0 ]
                    kompetencia_list.append(str(kompetencia).replace("`", "'"))
            # авторизація
            # url_2="https://ircenter.gov.ua/irc/index/ko-forms-detail/form_id/40900"
            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)

            # дані
            for i in kompetencia_list:
                time.sleep(1)
                input_qestion = browser.find_element(By.ID, "name")
                input_qestion.clear()
                input_qestion.send_keys(i)

                chetbox = browser.find_element(By.XPATH,
                                               "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[3]/select/option[3]")
                chetbox.click()

                time.sleep(1)

                btn_save = browser.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[4]/button")
                btn_save.click()




        except Exception as ex:
            print(ex)

    def add_potrebu_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        potrebu_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",
                                                                                                                  '')
                login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT potrebu_user FROM  irc_selenium_potrebu ;')
                for i in cursor:
                    KO_str = i
                    potrebu = KO_str [ 0 ]
                    potrebu_list.append(str(potrebu).replace("`", "'"))
            # авторизація

            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)

            # дані
            for i in potrebu_list:
                time.sleep(1)
                input_qestion = browser.find_element(By.ID, "name")
                input_qestion.clear()
                input_qestion.send_keys(i)

                chetbox = browser.find_element(By.XPATH,
                                               "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[3]/select/option[3]")
                chetbox.click()
                time.sleep(1)

                btn_save = browser.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[4]/button")
                btn_save.click()





        except Exception as ex:
            print(ex)

    def add_recocomendacii_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        recomendacii_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",
                                                                                                                  '')
                login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT recomendacii_user FROM  irc_selenium_recomendacii ;')
                for i in cursor:
                    KO_str = i
                    recomendacii = KO_str [ 0 ]
                    recomendacii_list.append(str(recomendacii).replace("`", "'"))

            # авторизація
            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)

            # дані
            for i in recomendacii_list:
                time.sleep(1)
                input_qestion = browser.find_element(By.ID, "name")
                input_qestion.clear()
                input_qestion.send_keys(i)

                chetbox = browser.find_element(By.XPATH,
                                               "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[3]/select/option[3]")
                chetbox.click()
                time.sleep(1)

                btn_save = browser.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div/div/div/div[3]/form/table/tbody/tr[2]/td[4]/button")
                btn_save.click()



        except Exception as ex:
            print(ex)

    def delete_kompetencia_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        kompetencia_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",
                                                                                                                  '')
            login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT kompetencia_user FROM  irc_selenium_kompetencia ;')
                for i in cursor:
                    KO_str = i
                    kompetencia = KO_str [ 0 ]
                    kompetencia_list.append(
                        str(kompetencia).replace("`", "'").replace(" ", "").replace("    ", "").replace("  ",
                                                                                                        "").replace(".",
                                                                                                                    "").replace(
                            "'", "").replace(",", ""))
            # авторизація
            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)
            text_chetbox = browser.find_elements(By.TAG_NAME, "tr")
            number = [ ]
            for i in range(len(text_chetbox)):
                text = text_chetbox [ i ].text.replace(" ", "").replace("    ", "").replace("  ", "").replace(".",
                                                                                                              "").replace(
                    "`", "").replace("'", "").replace(",", "")
                if text in kompetencia_list:
                    number.append(i)
                    kompetencia_list.remove(text)
            time.sleep(1)

            img = browser.find_elements(By.TAG_NAME, "a")
            src = [ ]
            for i in range(len(img)):
                src.append(img [ i ].get_attribute("href"))
            for i in number:
                browser.get(src [ i + 24 ])
                browser.get(url_2)
            # дані




        except Exception as ex:
            print(ex)

    def delete_potrebu_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        potrebu_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",
                                                                                                                  '')
                login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT potrebu_user FROM  irc_selenium_potrebu ;')
                for i in cursor:
                    KO_str = i
                    potrebu = KO_str [ 0 ]
                    potrebu_list.append(
                        str(potrebu).replace("`", "'").replace(" ", "").replace("    ", "").replace("  ", "").replace(
                            ".", "").replace("'", "").replace(",", ""))
            # авторизація
            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)
            text_chetbox = browser.find_elements(By.TAG_NAME, "tr")
            number = [ ]
            for i in range(len(text_chetbox)):
                text = text_chetbox [ i ].text.replace(" ", "").replace("    ", "").replace("  ", "").replace(".",
                                                                                                              "").replace(
                    "`", "").replace("'", "").replace(",", "")
                if text in potrebu_list:
                    number.append(i)
                    potrebu_list.remove(text)
            time.sleep(1)

            img = browser.find_elements(By.TAG_NAME, "a")
            src = [ ]
            for i in range(len(img)):
                src.append(img [ i ].get_attribute("href"))
            for i in number:
                browser.get(src [ i + 24 ])
                browser.get(url_2)
            # дані



        except Exception as ex:
            print(ex)

    def delete_recomendacii_auto(self):
        browser = webdriver.Firefox()
        url_2 = None
        login = None
        password = None
        option = webdriver.FirefoxOptions()
        connect = sl.connect('IRCdb.db')
        recomendacii_list = [ ]

        try:
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f"""SELECT login_user, password_user, url_user FROM  irc_portal;""")
                user = str(cursor.fetchone())
                user_dani = user.replace(user [ 0 ], '').replace(user [ 1 ], '').replace(user [ -1 ], '').replace(",",
                                                                                                                  '')
                login, password, url_2 = user_dani.split()

            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT recomendacii_user FROM  irc_selenium_recomendacii ;')
                for i in cursor:
                    KO_str = i
                    recomendacii = KO_str [ 0 ]
                    recomendacii_list.append(
                        str(recomendacii).replace("`", "'").replace(" ", "").replace("    ", "").replace("  ",
                                                                                                         "").replace(
                            ".", "").replace("'", "").replace(",", ""))

            # авторизація
            browser.get(url_2)
            time.sleep(2)

            login_input = browser.find_element(By.ID, "username")
            login_input.clear()
            login_input.send_keys(login)

            password_input = browser.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)

            btn_vhid = browser.find_element(By.ID, "login")
            btn_vhid.click()

            # авторизація
            time.sleep(2)
            text_chetbox = browser.find_elements(By.TAG_NAME, "tr")
            number = [ ]
            for i in range(len(text_chetbox)):
                text = text_chetbox [ i ].text.replace(" ", "").replace("    ", "").replace("  ", "").replace(".",
                                                                                                              "").replace(
                    "`", "").replace("'", "").replace(",", "")
                if text in recomendacii_list:
                    number.append(i)
                    recomendacii_list.remove(text)
            time.sleep(1)

            img = browser.find_elements(By.TAG_NAME, "a")
            src = [ ]
            for i in range(len(img)):
                src.append(img [ i ].get_attribute("href"))
            for i in number:
                browser.get(src [ i + 24 ])
                browser.get(url_2)
            # дані


        except Exception as ex:
            print(ex)

    def checge_connect(self):
        try:
            connect = sl.connect('IRCdb.db')
            self.metoduk_con.clear()
            self.potrebu_con.clear()
            self.rekomendacii_con.clear()
            self.grups_con.clear()

            self.comboBox.clear()
            self.comboBox_potrebu.clear()
            self.comboBox_recomendacii.clear()
            self.comboBox_grups.clear()
            with connect as con:
                cursor = con.cursor()
                cursor.execute('SELECT name from sqlite_master where type= "table"')
                for i in cursor:
                    table = str(i).replace('(', '').replace(')', '').replace("'", '').replace(',', '')
                    if 'qestions' in table:
                        if 'answers' not in table:
                            if 'irc' not in table:
                                self.metoduk_con.append(table)
                                self.comboBox.addItem(table.replace('_', ' ').replace('qestions', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))
                    elif 'potrebu' in table:
                        if 'answers' not in table:
                            if 'irc' not in table:
                                self.potrebu_con.append(table)
                                self.comboBox_potrebu.addItem(table.replace('_', ' ').replace('potrebu', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))
                    elif 'recomendacii' in table:
                        if 'answers' not in table:
                            if 'irc' not in table:
                                self.rekomendacii_con.append(table)
                                self.comboBox_recomendacii.addItem(table.replace('_', ' ').replace('recomendacii', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))
                    elif 'grups' in table:
                        if 'answers' not in table:
                            if 'irc' not in table:
                                self.grups_con.append(table)
                                self.comboBox_grups.addItem(table.replace('_', ' ').replace('grups', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))

                        # self.comboBox.addItem('Виберіть групу:')

        except Exception as ex:
            self.error.show()
            self.mesage_output('checge_connect')
            print('checge_connect:',ex)

    def chenge_table_all(self):
            try:

                    self.list_grupAll.clear()
                    self.id_grup_qestion.clear()
                    self.id_list_grup_for_table.clear()
                    connect = sl.connect('IRCdb.db')
                    # cursor.execute('pragma foreign_keys=on')
                    text_qestion = self.comboBox.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'qestions'
                    text_potrebu = self.comboBox_potrebu.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'
                    text_recomendacii = self.comboBox_recomendacii.currentText().replace('шкл.','Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'

                    with connect as con:
                            cursor = con.cursor()
                            if self.btn_variant == 'k':
                                    cursor.execute(f'SELECT COUNT(1) FROM  {text_qestion};')
                            elif self.btn_variant == 'p':
                                    cursor.execute(f'SELECT COUNT(1) FROM  {text_potrebu};')
                            elif self.btn_variant == 'r':
                                    cursor.execute(f'SELECT COUNT(1) FROM  {text_recomendacii};')

                            count = cursor.fetchone()
                            count_rows = count[0]
                            for i in range(int(count_rows) + 1):
                                    self.tableWidget.setRowCount(i)
                            if self.btn_variant == 'k':
                                    cursor.execute(f'SELECT qestion from {text_qestion};')
                            elif self.btn_variant == 'p':
                                    cursor.execute(f'SELECT potrebu from {text_potrebu};')
                            elif self.btn_variant == 'r':
                                    cursor.execute(f'SELECT recomendacii from {text_recomendacii};')

                            c = 0
                            for i in cursor:
                                    string = i
                                    qestion = string[ 0 ]
                                    self.tableWidget.setItem(c, 0, QTableWidgetItem(qestion))
                                    c += 1
                            if self.btn_variant == 'k':
                                    cursor.execute(f'SELECT grup from {text_qestion.replace("qestions", "grups")};')
                            elif self.btn_variant == 'p':
                                    cursor.execute(f'SELECT grup from {text_potrebu.replace("potrebu", "grups")};')
                            elif self.btn_variant == 'r':
                                    cursor.execute(
                                            f'SELECT grup from {text_recomendacii.replace("recomendacii", "grups")};')
                            try:
                                    for i in cursor:
                                            grup_str = i
                                            grups_str_all = grup_str [ 0 ]
                                            if grups_str_all == ' ':
                                                    grups_str_all = '----------'
                                            self.list_grupAll.append(grups_str_all)
                            except Exception as ex:
                                    print(ex)
                            if self.btn_variant == 'k':
                                    cursor.execute(f'SELECT grup_id from {text_qestion};')
                            elif self.btn_variant == 'p':
                                    cursor.execute(f'SELECT grup_id from {text_potrebu};')
                            elif self.btn_variant == 'r':
                                    cursor.execute(f'SELECT grup_id from {text_recomendacii};')

                            for i in cursor:
                                    string = i
                                    grup_id = string[0]
                                    self.id_grup_qestion.append(grup_id)

                            for i in range(len(self.id_grup_qestion)):
                                    if self.btn_variant == 'k':
                                            cursor.execute(
                                                    f'SELECT grup from {text_qestion.replace("qestions", "grups")} WHERE id={self.id_grup_qestion [ i ]};')
                                    elif self.btn_variant == 'p':
                                            cursor.execute(
                                                    f'SELECT grup from {text_potrebu.replace("potrebu", "grups")} WHERE id={self.id_grup_qestion [ i ]};')
                                    elif self.btn_variant == 'r':
                                            cursor.execute(
                                                    f'SELECT grup from {text_recomendacii.replace("recomendacii", "grups")} WHERE id={self.id_grup_qestion [ i ]};')

                                    str_grup = cursor.fetchone()
                                    str_id_grup = str_grup[0]
                                    if str_id_grup == ' ':
                                            str_id_grup = '----------'
                                    self.id_list_grup_for_table.append(str_id_grup)

                            g = 0
                            for i in range(int(count_rows)):
                                    select = QtWidgets.QComboBox()
                                    font = QtGui.QFont()
                                    font.setPointSize(12)
                                    select.setStyleSheet(
                                            "QComboBox{\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            f"    border-radius: {3 * suma3}%;\n"
                                            f"    border: 1px solid;\n"
                                            "}\n"
                                            "QComboBox:hover{"
                                            "border-color: rgb(41, 213, 202)"
                                            "}"
                                            "\n"
                                            "QComboBox, QAbstractItemView{\n"
                                            "  selection-color: black;\n"
                                            "  selection-background-color: #05F3CC ;\n"
                                            "}\n"
                                            "QComboBox::drop-down{\n"
                                            "  border: 0 ;\n"
                                            "}\n"

                                            "")
                                    select.setFont(font)
                                    select.addItem(self.id_list_grup_for_table [ i ])
                                    for i in range(len(self.list_grupAll)):
                                            select.addItem(self.list_grupAll [ i ])
                                    self.tableWidget.setCellWidget(g, 1, select)
                                    check = QtWidgets.QCheckBox()
                                    check.setStyleSheet("""
                                                                           QCheckBox:hover{
                                                                               background-color: rgb(41, 213, 202);
                                                                           }
                                                                           QCheckBox::indicator {
                                                                               width: 80px;
                                                                               height: 30px;
                                                                           }
                                                                       """)
                                    self.tableWidget.setCellWidget(g, 2, check)
                                    self.btn_delete = QtWidgets.QPushButton()
                                    font.setPointSize(12)
                                    self.btn_delete.setStyleSheet(
                                            "QPushButton{\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            f"    border-radius: {3 * suma3}%;\n"
                                            f"    border: 2px solid;\n"
                                            "}\n"
                                            "QPushButton:hover{"
                                            "border-color: red;"
                                            "}"
                                            "\n"
                                            "}\n"

                                            "")
                                    self.btn_delete.setFont(font)
                                    self.btn_delete.setText('X')
                                    self.tableWidget.setCellWidget(g, 3, self.btn_delete)
                                    g += 1
                                    self.btn_delete.clicked.connect(self.mesage)
            except Exception as ex:
                    print('chenge_table_all:', ex)
                    self.error.show()
                    self.mesage_output('chenge_table_all')
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem('Немає створених методик!'))

    def show_grups_table(self):
        try:
            text_grups = self.comboBox_grups.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ','_') + 'grups'
            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT COUNT(1) FROM  {text_grups};')
                count = str(cursor.fetchone())
                count_rows = count.replace(count [ 0 ], '').replace(count [ -1 ], '').replace(count [ -2 ], '')
                for i in range(int(count_rows) + 1):
                    self.tableWidget.setRowCount(i)
                cursor.execute(f'SELECT grup from {text_grups};')
                c = 0
                for i in cursor:
                    string = str(i)
                    grups_one = string.replace(string [ 0 ], '').replace(string [ 1 ], '').replace(string [ -1 ], '').replace(string [ -2 ], '')
                    if grups_one==' ':
                        grups_one='----------'
                    self.tableWidget.setItem(c, 0, QTableWidgetItem(grups_one))
                    c += 1
                g = 0
                for i in range(int(count_rows)):
                    check = QtWidgets.QCheckBox()
                    check.setStyleSheet("""
                                                                                      QCheckBox:hover{
                                                                                          background-color: rgb(41, 213, 202);
                                                                                      }
                                                                                      QCheckBox::indicator {
                                                                                          width: 80px;
                                                                                          height: 30px;
                                                                                      }
                                                                                  """)
                    self.tableWidget.setCellWidget(g, 1, check)
                    self.btn_delete = QtWidgets.QPushButton()
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.btn_delete.setStyleSheet(
                        "QPushButton{\n"
                        "    background-color: rgb(255, 255, 255);\n"
                        f"    border-radius: {3 * suma3}%;\n"
                        f"    border: 2px solid;\n"
                        "}\n"
                        "QPushButton:hover{"
                        "border-color: red;"
                        "}"
                        "\n"
                        "}\n"
    
                        "")
                    self.btn_delete.setFont(font)
                    self.btn_delete.setText('X')
                    self.tableWidget.setCellWidget(g, 2, self.btn_delete)
                    self.btn_delete.clicked.connect(self.mesage)
                    g += 1
        except Exception as ex:
            self.error.show()
            self.mesage_output('show_grups_table')
            print('show_grups_table', ex)

    def show_anketa_table(self):
        try:
            self.oputyvana=2
            text_anketa = self.comboBox_anketa.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ','_') + 'Anketa'
            connect = sl.connect('IRCdb.db')
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT COUNT(1) FROM  {text_anketa};')
                count = cursor.fetchone()
                count_rows = count[0]
                for i in range(int(count_rows) + 1):
                    self.tableWidget.setRowCount(i)
                cursor.execute(f'SELECT putana from {text_anketa};')
                c = 0
                for i in cursor:
                    string = i
                    anketa_one = string[0]
                    if anketa_one==' ':
                        anketa_one='----------'
                    self.tableWidget.setItem(c, 0, QTableWidgetItem(anketa_one))
                    c += 1
                g = 0
                for i in range(int(count_rows)):
                    check = QtWidgets.QCheckBox()
                    check.setStyleSheet("""
                                                                                      QCheckBox:hover{
                                                                                          background-color: rgb(41, 213, 202);
                                                                                      }
                                                                                      QCheckBox::indicator {
                                                                                          width: 80px;
                                                                                          height: 30px;
                                                                                      }
                                                                                  """)
                    self.tableWidget.setCellWidget(g, 1, check)
                    self.btn_delete = QtWidgets.QPushButton()
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.btn_delete.setStyleSheet(
                        "QPushButton{\n"
                        "    background-color: rgb(255, 255, 255);\n"
                        f"    border-radius: {3 * suma3}%;\n"
                        f"    border: 2px solid;\n"
                        "}\n"
                        "QPushButton:hover{"
                        "border-color: red;"
                        "}"
                        "\n"
                        "}\n"
    
                        "")
                    self.btn_delete.setFont(font)
                    self.btn_delete.setText('X')
                    self.tableWidget.setCellWidget(g, 2, self.btn_delete)
                    self.btn_delete.clicked.connect(self.mesage)
                    g += 1
        except Exception as ex:
            self.error.show()
            self.mesage_output('show_anketa_table')
            print('show_anketa_table', ex)

    def show_chenge(self, x):
        try:
            self.table_restart()
            row_result = self.tableWidget.rowCount()
            for i in range(row_result):
                self.tableWidget.removeRow(i)
            if x == 'k':
                self.btn_variant='k'
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText('Компенція')
                self.chenge_table_all()

            elif x =='p':
                self.btn_variant='p'
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText('Потреби')
                text_potrebu = self.comboBox.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'potrebu'
                self.chenge_table_all()

            elif x == 'r':
                self.btn_variant='r'
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText('Рекомендації')
                text_recomendacii = self.comboBox.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'recomendacii'
                self.chenge_table_all()

            elif x == 'g':
                self.btn_variant = 'g'
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText('Групи')
                text_grups = self.comboBox.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ', '_') + 'grups'
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText('clear')
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText('del')
                self.tableWidget.setColumnCount(3)
                self.show_grups_table()
            elif x == 'a':
                self.btn_variant='a'
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText('Питання')
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText('clear')
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText('del')
                self.tableWidget.setColumnCount(3)
                self.show_anketa_table()
        except Exception as ex:
            self.error.show()
            self.mesage_output('show_chenge')
            print('show_chenge',ex)

    def potreba_recomendacii_delete(self):
        index = [ ]
        try:
            for i in range(len(self.potreba_recomendacii)):
                if self.tableWidget.cellWidget(i, 2).checkState():
                    index.append(self.tableWidget.item(i, 0).text())
            len_in = len(index)
            for i in range(len_in):
                c = index [ i ]
                if c in self.potreba_recomendacii :
                    index_del = self.potreba_recomendacii.index(c)
                    self.potreba_recomendacii.pop(index_del)
                    self.grup.pop(index_del)

            for i in range(len(self.potreba_recomendacii) + 1):
                self.tableWidget.setRowCount(i)

            for i in range(len(self.potreba_recomendacii)):
                check = QtWidgets.QCheckBox()
                check.setStyleSheet("""
                                           QCheckBox:hover{
                                               background-color: rgb(41, 213, 202);
                                           }
                                           QCheckBox::indicator {
                                               width: 80px;
                                               height: 30px;
                                           }
                                       """)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(self.potreba_recomendacii [ i ]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(self.grup [ i ]))
                self.tableWidget.setCellWidget(i, 2, check)
            index.clear()
        except Exception as ex:
            self.error.show()
            self.mesage_output('potreba_recomendacii_delete')
            print('potreba_recomendacii_delete',ex)

    def add_potrebu_and_recomendacii(self,x):
        self.len_potreb = len(self.potreba_recomendacii)
        try:
            if self.add_potrebu.text()=='':
                    pass
            elif self.add_recom.text()=='':
                    pass
            if x=='p':
                self.potreba_recomendacii.append(self.add_potrebu.text().replace("'", "`"))
                self.grup.append(self.comboBox_grup_potrebu.currentText())
            elif x=='r':
                self.potreba_recomendacii.append(self.add_recom.text().replace("'", "`"))
                self.grup.append(self.comboBox_grups_recomendacii.currentText())
            for i in range(self.len_potreb + 2):
                self.tableWidget.setRowCount(i)
            for i in range(self.len_potreb+1):
                check = QtWidgets.QCheckBox()
                check.setStyleSheet("""
                               QCheckBox:hover{
                                   background-color: rgb(41, 213, 202);
                               }
                               QCheckBox::indicator {
                                   width: 80px;
                                   height: 30px;
                               }
                           """)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(self.potreba_recomendacii [ i ]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(self.grup [ i ]))
                self.tableWidget.setCellWidget(i, 2, check)
            if x=='p':
                self.add_potrebu.setText('')
            elif x=='r':
                self.add_recom.setText('')
        except Exception as ex:
            self.error.show()
            self.mesage_output('add_potrebu_and_recomendacii')
            print('add_potrebu_and_recomendacii',ex)

    def delete_qestion_to_metoduk(self):
        index=[ ]
        index_grup=[]
        try:
            for i in range(len(self.qestion)):
                if self.tableWidget.cellWidget(i, 2).checkState():
                    index.append(self.tableWidget.item(i,0).text())
                    index_grup.append(self.tableWidget.item(i,1).text())
            len_in = len(index)
            for i in range(len_in):
                c = index [ i ]
                if c  in self.qestion :
                    index_del = self.qestion.index(c)
                    self.qestion.pop(index_del)
                    self.grup.pop(index_del)
            for i in range(len(self.qestion)+1):
                self.tableWidget.setRowCount(i)

            for i in range(len(self.qestion)):
                check = QtWidgets.QCheckBox()
                check.setStyleSheet("""
                                    QCheckBox:hover{
                                        background-color: rgb(41, 213, 202);
                                    }
                                    QCheckBox::indicator {
                                        width: 80px;
                                        height: 30px;
                                    }
                                """)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(self.qestion [ i ]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(self.grup [ i ]))
                self.tableWidget.setCellWidget(i, 2, check)
            index.clear()
            index_grup.clear()

        except Exception as ex:
            self.error.show()
            self.mesage_output('delete_qestion_to_metoduk')
            print('delete_qestion_to_metoduk:',ex)

    def add_to_table_qestion_and_grup(self):
        try:
            if self.add_qestion.text() == '':
                    pass
            else:
                    self.qestion.append(self.add_qestion.text().replace("'", "`"))
                    if self.add_grup.text() != '':
                            self.grup.append(self.add_grup.text().replace("'", "`"))

                    else:
                            self.grup.append(' ')
                    self.add_qestion.setText('')
                    self.len = len(self.qestion)
                    for i in range(self.len + 1):
                            self.tableWidget.setRowCount(i)

                    for i in range(self.len):
                            check = QtWidgets.QCheckBox()
                            check.setStyleSheet("""
                               QCheckBox:hover{
                                   background-color: rgb(41, 213, 202);
                               }
                               QCheckBox::indicator {
                                   width: 80px;
                                   height: 30px;
                               }
                           """)
                            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.qestion [ i ]))
                            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.grup [ i ]))
                            self.tableWidget.setCellWidget(i, 2, check)
        except Exception as ex:
            self.error.show()
            self.mesage_output('add_to_table_qestion_and_grup')
            print('add_to_table_qestion_and_grup', ex)

    def save_all(self):
        try:
            if self.create_number == 1:
                    self.save_kompetencia()
            elif self.potreba_number==1:
                    self.save_potrebu_recomendscii()
            elif self.rekomendacii_number==1:
                    self.save_potrebu_recomendscii()
            elif self.chenge_number == 1:
                    if self.btn_variant == 'g':
                        self.update_grups()
                        self.btn_variant=None
                    elif self.btn_variant=='a':
                        self.update_anketa()
                        self.btn_variant=None
                    else:
                            self.update_qestions_potreb_recomendacii()
            elif self.oputyvana==1:
                self.save_anketa()
        except Exception as ex:
            self.error.show()
            self.mesage_output('save_all')
            print('save_all', ex)

    def save_potrebu_recomendscii(self):
        try:
            self.save.setIcon(QIcon('savergb.png'))
            self.save.setIconSize(QSize(int(40 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
            connect = sl.connect('IRCdb.db')
            try:
                    if self.save_material == 'p':
                            self.nazva_potreb_recomendacii = self.comboBox_potrebu_create.currentText().replace('дош.','Дошкільний вік').replace('шкл.', 'Шкільний вік').replace(' ', '_') + 'potrebu'
                            self.references_potrebu = self.comboBox_potrebu_create.currentText().replace('дош.','Дошкільний вік').replace('шкл.', 'Шкільний вік').replace(' ', '_')
                    elif self.save_material == 'r':
                            self.nazva_potreb_recomendacii = self.comboBox_recom_create.currentText().replace('дош.','Дошкільний вік').replace('шкл.', 'Шкільний вік').replace(' ', '_') + 'recomendacii'
                            self.references_potrebu = self.comboBox_recom_create.currentText().replace('дош.','Дошкільний вік').replace('шкл.', 'Шкільний вік').replace(' ', '_')


                    print(self.references_potrebu)
                    with connect as con:
                            cursor = con.cursor()
                            if self.save_material == 'p':
                                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.nazva_potreb_recomendacii}'
                                                    f'(id INTEGER PRIMARY KEY, potrebu varchar(400), grup_id int REFERENCES {self.references_potrebu}grups(id) ON DELETE CASCADE);')
                            elif self.save_material == 'r':
                                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.nazva_potreb_recomendacii}'
                                                    f'(id INTEGER PRIMARY KEY, recomendacii varchar(400), grup_id int REFERENCES {self.references_potrebu}grups(id) ON DELETE CASCADE);')
            except Exception as ex:
                print('save_potrebu_recomendscii:', ex)
            with connect as con:
                            cursor = con.cursor()
                            let_list = len(self.potreba_recomendacii)
                            for i in range(let_list):
                                    potrebu = str(self.potreba_recomendacii [ i ])
                                    cursor.execute(f"""SELECT id FROM {self.references_potrebu}grups WHERE grup="{str(self.grup [ i ]).replace('----------', ' ')}" """)
                                    id = cursor.fetchone()
                                    id_grup = id[0]
                                    print(id_grup)
                                    if self.save_material == 'p':
                                            cursor.execute(f"""INSERT INTO  {self.nazva_potreb_recomendacii} (potrebu, grup_id) VALUES ('{potrebu}', {id_grup}) """)
                                    elif self.save_material == 'r':
                                            cursor.execute(f"""INSERT INTO  {self.nazva_potreb_recomendacii} (recomendacii, grup_id) VALUES ('{potrebu}', {id_grup}) """)
                            print('Записано')


            if self.File_save_potrebu.isChecked() or self.File_save_recom.isChecked():
                    filename = QFileDialog.getSaveFileName()
                    self.path = filename [ 0 ]
                    with open(f'{self.path + self.nazva_potreb_recomendacii}.txt', 'w', encoding='utf-8') as f:
                            for i in range(len(self.potreba_recomendacii)):
                                    f.write(self.potreba_recomendacii [ i ] + ' : ' + self.grup [ i ] + '\n')

            self.potreba_recomendacii.clear()
            self.grup.clear()
            self.len = len(self.potreba_recomendacii)
            for i in range(self.len + 1):
                    self.tableWidget.setRowCount(i)

            self.save.setIcon(QIcon('save.png'))
            self.save.setIconSize(QSize(int(40 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
        except Exception as ex:
            self.error.show()
            self.mesage_output('save_potrebu_recomendscii')
            print('save_potrebu_recomendscii', ex)

    def save_kompetencia(self):
            self.previrka='ok'
            self.save.setIcon(QIcon('savergb.png'))
            self.save.setIconSize(QSize(int(40 * suma3/Ui_MainWindow.number), int(40 * suma3/Ui_MainWindow.number)))
            connect = sl.connect('IRCdb.db')
            if self.Doschilnul.isChecked():
                    zaklad = self.Doschilnul.text().replace(' ', '_')
            elif self.School.isChecked():
                    zaklad = self.School.text().replace(' ', '_')
            else:
                    zaklad = ''
            nazva_metoduku = self.nazva_metodulu.text().replace(' ', '_').replace(",","_").replace("(","").replace(")","").replace("'","`")
            try:
                    with connect as con:
                            cursor = con.cursor()
                            cursor.execute(f'CREATE TABLE IF NOT EXISTS {nazva_metoduku + "_" + zaklad}_grups'
                                           f'(id INTEGER PRIMARY KEY, grup varchar(400));')
                    with connect as con:
                            cursor = con.cursor()
                            grups = [ ]
                            for i in self.grup:
                                    if i not in grups:
                                            grups.append(i)
                            let_grup = len(grups)
                            for i in range(let_grup):
                                    grup = str(grups [ i ])
                                    cursor.execute(
                                            f"""INSERT INTO {nazva_metoduku + "_" + zaklad}_grups  (grup) VALUES ('{grup}') """)
                            print('Записано')
                    with connect as con:
                            cursor = con.cursor()
                            cursor.execute(f'CREATE TABLE IF NOT EXISTS {nazva_metoduku + "_" + zaklad}_qestions '
                                           f'(id INTEGER PRIMARY KEY, qestion varchar(400), grup_id int REFERENCES {nazva_metoduku + "_" + zaklad}_grups(id) ON DELETE CASCADE);')
                    with connect as con:
                            cursor = con.cursor()
                            let_qestion = len(self.qestion)
                            for i in range(let_qestion):
                                    qestion = str(self.qestion [ i ])
                                    cursor.execute(
                                            f"""SELECT id FROM {nazva_metoduku + '_' + zaklad}_grups WHERE grup='{str(self.grup [ i ])}' """)
                                    id = cursor.fetchone()
                                    id_grup = int(
                                            str(id).replace('(', '').replace('"', '').replace(',', '').replace("'","").replace(")", ""))
                                    cursor.execute(f"""INSERT INTO  {nazva_metoduku + '_' + zaklad}_qestions (qestion, grup_id) VALUES ('{qestion}', {id_grup}) """)
                            print('Записано')

            except Exception as ex:
                    self.error.show()
                    self.mesage_output('save_kompetencia')
                    self.previrka=self.mesage_exept('kompetencia')
                    print('save_kompetencia:', ex)
            if self.previrka=='ERROR':
                    self.save.setIcon(QIcon('save.png'))
                    self.save.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))
                    pass
            else:
                    if self.File_save.isChecked():
                            filename = QFileDialog.getSaveFileName()
                            self.path = filename [ 0 ]
                            nazva_maoduku = self.nazva_metodulu.text()
                            with open(f'{self.path + nazva_maoduku + zaklad}.txt', 'w', encoding='utf-8') as f:
                                    if self.Doschilnul.isChecked():
                                            f.write(self.Doschilnul.text() + '\n')
                                    elif self.School.isChecked():
                                            f.write(self.School.text() + '\n')
                                    for i in range(len(self.qestion)):
                                            f.write(self.qestion [ i ] + ' : ' + self.grup [ i ] + '\n')
                    self.nazva_metodulu.clear()
                    self.qestion.clear()
                    self.grup.clear()
                    self.len = len(self.qestion)
                    for i in range(self.len + 1):
                            self.tableWidget.setRowCount(i)
                    self.save.setIcon(QIcon('save.png'))
                    self.save.setIconSize(QSize(int(40 * suma3 / Ui_MainWindow.number), int(40 * suma3 / Ui_MainWindow.number)))

    def delete_metodub_is_db(self):
            if self.delete_number == 0:
                self.hide_widget()
                self.frame_delete.show()
                self.delete_metoduk.setGeometry(QtCore.QRect(int(4 * suma3 /Ui_MainWindow.number), int(320 * suma3 /Ui_MainWindow.number),int(55 * suma3 /Ui_MainWindow.number), int(55 * suma3 /Ui_MainWindow.number)))
                self.delete_metoduk.setIcon(QIcon('delrgb.png'))
                self.delete_number += 1
                self.conect_delete()

            else:
                self.frame_delete.hide()
                self.delete_number = 0
                self.delete_metoduk.setGeometry(QtCore.QRect(int(4 * suma3 /Ui_MainWindow.number), int(320 * suma3 /Ui_MainWindow.number),int(55 * suma3 /Ui_MainWindow.number), int(55 * suma3 /Ui_MainWindow.number)))
                self.delete_metoduk.setIcon(QIcon('del.png'))

    def chenge_metoduk(self):

            if self.chenge_number == 0:
                    self.hide_widget()
                    self.chenge.setIcon(QIcon('chenge_rgb.png'))
                    self.chenge.setIconSize(QSize(int(35 * suma3 /Ui_MainWindow.number), int(35 * suma3 /Ui_MainWindow.number)))
                    self.chenge_number += 1
                    self.freme_chenge.show()
                    self.plus.hide()
                    self.minus.hide()
                    self.add_che.show()
                    self.del_che.show()
                    self.checge_connect()
                    self.con_nazva_metoduk('anketa')
            else:
                    self.chenge.setIcon(QIcon('chenge.png'))
                    self.chenge.setIconSize(QSize(int(35 * suma3 /Ui_MainWindow.number), int(35 * suma3 /Ui_MainWindow.number)))
                    self.chenge_number = 0
                    self.freme_chenge.hide()
                    self.add_che.hide()
                    self.del_che.hide()
                    self.plus.show()
                    self.minus.show()

    def show_grups(self,x):
        try:
            grup_list=[]
            grup_list.clear()
            self.comboBox_grup_potrebu.clear()
            self.comboBox_grups_recomendacii.clear()

            connect = sl.connect('IRCdb.db')
            if x=='p':
                self.text_combo = self.comboBox_potrebu_create.currentText().replace('шкл.', 'Шкільний вік').replace('дош.','Дошкільний вік').replace(' ','_')+'grups'
            elif x =='r':
                self.text_combo = self.comboBox_recom_create.currentText().replace('шкл.', 'Шкільний вік').replace('дош.', 'Дошкільний вік').replace(' ', '_') + 'grups'
            else:
                    pass
            with connect as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT grup from {self.text_combo};')
                for i in cursor:
                    string =i
                    grup = i[0]
                    if grup not in grup_list:
                        grup_list.append(grup)
                    if ' ' in  grup_list:
                        grup_list.remove(' ')
                        if '----------'  not in grup_list:
                            grup_list.append('----------')
                if x=='p':
                        self.comboBox_grup_potrebu.addItem('Виберіть групу:')
                elif x=='r':
                        self.comboBox_grups_recomendacii.addItem('Виберіть групу:')
                else:
                        pass

                for i in grup_list:
                    if x == 'p':
                        self.comboBox_grup_potrebu.addItem(i)
                    elif x == 'r':
                        self.comboBox_grups_recomendacii.addItem(i)
                    else:
                        pass


        except Exception as ex:
            self.error.show()
            self.mesage_output('show_grups')
            print('show_grups',ex)

    def create_rekomendacii(self):
            try:
                    self.table_restart()
                    row_result = self.tableWidget.rowCount()
                    for i in range(row_result):
                            self.tableWidget.removeRow(i)
                    self.tableWidget.setColumnCount(3)
                    if self.rekomendacii_number == 0:
                            self.hide_widget()
                            self.frame_create_recom.show()
                            self.rekomendacii_number += 1
                            self.save_material = 'r'
                            self.rekomendacii.setIcon(QIcon('рrgb.png'))
                            self.potreba.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number),
                                                           int(50 * suma3 / Ui_MainWindow.number)))
                            self.add_recom.setPlaceholderText('Рекомендації:')
                            item = self.tableWidget.horizontalHeaderItem(0)
                            item.setText("Рекомендації")
                            self.con_nazva_metoduk('r')
                            self.show_grups('r')

                    else:
                            self.frame_create_recom.hide()
                            self.save_material = None
                            self.rekomendacii.setIcon(QIcon('р.png'))
                            self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number),
                                                                int(50 * suma3 / Ui_MainWindow.number)))
                            self.rekomendacii_number = 0

            except Exception as ex:
                self.error.show()
                self.mesage_output('create_rekomendacii')
                print('create_rekomendacii',ex)

    def create_potreba(self):
            try:
                    self.table_restart()
                    row_result = self.tableWidget.rowCount()
                    for i in range(row_result):
                            self.tableWidget.removeRow(i)
                    self.tableWidget.setColumnCount(3)
                    self.potreba_recomendacii.clear()
                    if self.potreba_number == 0:
                            self.hide_widget()
                            self.con_nazva_metoduk('p')
                            self.frame_create_potr.show()
                            self.potreba_number += 1
                            self.save_material = 'p'
                            self.potreba.setIcon(QIcon('пrgb.png'))
                            self.potreba.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
                            self.add_potrebu.setPlaceholderText('Потреба:')
                            item = self.tableWidget.horizontalHeaderItem(0)
                            item.setText("Потреби")
                            self.show_grups('p')
                    else:
                            self.frame_create_potr.hide()
                            self.save_material = None
                            self.potreba.setIcon(QIcon('п.png'))
                            self.potreba.setIconSize(QSize(int(50 *suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
                            self.potreba_number = 0

            except Exception as ex:
                self.error.show()
                self.mesage_output('create_potreba')
                print('create_potreba',ex)

    def create_metoduk(self):
        self.table_restart()
        row_result=self.tableWidget.rowCount()
        for i in range(row_result):
            self.tableWidget.removeRow(i)
        self.tableWidget.setColumnCount(3)
        self.potreba_recomendacii.clear()

        try:

            if self.create_number==0:
                self.hide_widget()
                self.add_metoduk.setIcon(QIcon('кrgb.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3/Ui_MainWindow.number), int(50 * suma3/Ui_MainWindow.number)))
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText("Питання")
                self.frame_create_kom.show()
                self.create_number+=1

            else:
                self.frame_create_kom.hide()
                self.create_number=0
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 *suma3/Ui_MainWindow.number), int(50 *suma3/Ui_MainWindow.number)))



        except Exception as ex:
            self.error.show()
            self.mesage_output('create_metoduk')
            print('create_metoduk:',ex)

    def rozmir_window(self,n):

        if n == '-':
                if Ui_MainWindow.number == 0:
                        Ui_MainWindow.number = 1.02
                elif Ui_MainWindow.number >= 0:
                        Ui_MainWindow.number += 0.02
        if n == '+':
                if Ui_MainWindow.number == 0:
                        Ui_MainWindow.number = 1.00

                elif Ui_MainWindow.number >= 0:
                        Ui_MainWindow.number -= 0.02

        self.setupUi(MainWindow)
        self.table_restart()

    def table_restart(self):

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(int(14/Ui_MainWindow.number))
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        table = self.tableWidget
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Змінити")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText('Група')
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText('clear')
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText('del')

    def con_nazva_metoduk(self, n):
        try:
            connect = sl.connect('IRCdb.db')
            self.all_metoduk.clear()
            self.comboBox_anketa.clear()
            if n=='p':
                self.comboBox_potrebu_create.clear()
            elif n=='r':
                 self.comboBox_recom_create.clear()
            else:
                pass
            with connect as con:
                cursor = con.cursor()
                cursor.execute('SELECT name from sqlite_master where type= "table"')
                for i in cursor:
                    table = str(i).replace('(', '').replace(')', '').replace("'", '').replace(',', '')
                    if 'qestions' in table:
                        self.all_metoduk.append(table)
                        if n == 'p':
                            self.comboBox_potrebu_create.addItem(table.replace('_', ' ').replace('qestions', '').replace('Шкільний вік','шкл.').replace('Дошкільний вік','дош.'))
                            self.comboBox_grup_potrebu.addItem('Виберіть групу:')
                        elif n == 'r':
                            self.comboBox_recom_create.addItem(table.replace('_', ' ').replace('qestions', '').replace('Шкільний вік','шкл.').replace('Дошкільний вік', 'дош.'))
                            self.comboBox_grups_recomendacii.addItem('Виберіть групу:')
                        elif n =='site':
                                self.comboBox_site.addItem(table.replace('_', ' ').replace('qestions', '').replace('Шкільний вік','шкл.').replace('Дошкільний вік', 'дош.'))
                        else:
                            pass
                    if 'Anketa' in table:
                        if n=='anketa':
                            self.comboBox_anketa.addItem(table.replace('_', ' ').replace('Anketa', '').replace('Шкільний вік', 'шкл.').replace('Дошкільний вік', 'дош.'))




        except Exception as ex:
            self.error.show()
            self.mesage_output('con_nazva_metoduk')
            print('con_nazva_metoduk',ex)

    def hide_widget(self):
        if self.create_number==0:
           self.freme_chenge.hide()
           self.frame_delete.hide()
           self.frame_create_potr.hide()
           self.frame_create_recom.hide()
           self.frame_delete.hide()
           self.frame_avtozapovnena.hide()
           self.frame_create_oputyvana.hide()
           self.create_qestions.setIcon(QIcon('a.png'))
           self.create_qestions.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
           self.rekomendacii.setIcon(QIcon('р.png'))
           self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
           self.update_btn_avto.setIcon(QIcon('internet.png'))
           self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
           self.chenge.setIcon(QIcon('chenge.png'))
           self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
           self.potreba.setIcon(QIcon('п.png'))
           self.potreba.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
           self.delete_metoduk.setIcon(QIcon('del.png'))
           self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
           self.potreba_number=0
           self.rekomendacii_number=0
           self.delete_number=0
           self.chenge_number=0
           self.site=0
           self.oputyvana=0
           self.add_che.hide()
           self.del_che.hide()
           self.minus.show()
           self.plus.show()
        elif self.potreba_number==0:
                self.freme_chenge.hide()
                self.frame_delete.hide()
                self.frame_create_kom.hide()
                self.frame_create_recom.hide()
                self.frame_delete.hide()
                self.frame_avtozapovnena.hide()
                self.rekomendacii.setIcon(QIcon('р.png'))
                self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIcon(QIcon('chenge.png'))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.delete_metoduk.setIcon(QIcon('del.png'))
                self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.update_btn_avto.setIcon(QIcon('internet.png'))
                self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.create_number = 0
                self.rekomendacii_number = 0
                self.delete_number = 0
                self.chenge_number = 0
                self.site=0
                self.add_che.hide()
                self.del_che.hide()
                self.minus.show()
                self.plus.show()
                self.frame_create_oputyvana.hide()
                self.create_qestions.setIcon(QIcon('a.png'))
                self.create_qestions.setIconSize(
                    QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.oputyvana = 0

        elif self.rekomendacii_number==0:
                self.freme_chenge.hide()
                self.frame_delete.hide()
                self.frame_create_kom.hide()
                self.frame_create_potr.hide()
                self.frame_delete.hide()
                self.frame_avtozapovnena.hide()
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIcon(QIcon('chenge.png'))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.delete_metoduk.setIcon(QIcon('del.png'))
                self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.potreba.setIcon(QIcon('п.png'))
                self.update_btn_avto.setIcon(QIcon('internet.png'))
                self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.create_number = 0
                self.potreba_number = 0
                self.delete_number = 0
                self.chenge_number = 0
                self.site=0
                self.add_che.hide()
                self.del_che.hide()
                self.minus.show()
                self.plus.show()
                self.frame_create_oputyvana.hide()
                self.create_qestions.setIcon(QIcon('a.png'))
                self.create_qestions.setIconSize(
                    QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.oputyvana = 0

        elif self.chenge_number==0:
                self.rekomendacii_chenge.hide()
                self.frame_delete.hide()
                self.frame_create_kom.hide()
                self.frame_create_potr.hide()
                self.frame_delete.hide()
                self.frame_avtozapovnena.hide()
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.rekomendacii.setIcon(QIcon('р.png'))
                self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.delete_metoduk.setIcon(QIcon('del.png'))
                self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.potreba.setIcon(QIcon('п.png'))
                self.update_btn_avto.setIcon(QIcon('internet.png'))
                self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.create_number = 0
                self.potreba_number = 0
                self.delete_number = 0
                self.site=0
                self.rekomendacii_number = 0
                self.frame_create_oputyvana.hide()
                self.create_qestions.setIcon(QIcon('a.png'))
                self.create_qestions.setIconSize(
                    QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.oputyvana = 0

        elif self.delete_number==0:
                self.rekomendacii_chenge.hide()
                self.frame_delete.hide()
                self.frame_create_kom.hide()
                self.frame_create_potr.hide()
                self.freme_chenge.hide()
                self.frame_avtozapovnena.hide()
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.rekomendacii.setIcon(QIcon('р.png'))
                self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIcon(QIcon('chenge.png'))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.potreba.setIcon(QIcon('п.png'))
                self.update_btn_avto.setIcon(QIcon('internet.png'))
                self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.create_number = 0
                self.potreba_number = 0
                self.chenge_number = 0
                self.rekomendacii_number = 0
                self.site=0
                self.add_che.hide()
                self.del_che.hide()
                self.minus.show()
                self.plus.show()
                self.frame_create_oputyvana.hide()
                self.create_qestions.setIcon(QIcon('a.png'))
                self.create_qestions.setIconSize(
                    QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.oputyvana = 0

        elif self.site==0:
                self.rekomendacii_chenge.hide()
                self.frame_delete.hide()
                self.frame_create_kom.hide()
                self.frame_create_potr.hide()
                self.freme_chenge.hide()
                self.frame_delete.hide()
                self.add_metoduk.setIcon(QIcon('к.png'))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.rekomendacii.setIcon(QIcon('р.png'))
                self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.chenge.setIcon(QIcon('chenge.png'))
                self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
                self.potreba.setIcon(QIcon('п.png'))
                self.delete_metoduk.setIcon(QIcon('del.png'))
                self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.delete_number = 0
                self.create_number = 0
                self.potreba_number = 0
                self.chenge_number = 0
                self.rekomendacii_number = 0
                self.add_che.hide()
                self.del_che.hide()
                self.minus.show()
                self.plus.show()
                self.frame_create_oputyvana.hide()
                self.create_qestions.setIcon(QIcon('a.png'))
                self.create_qestions.setIconSize(
                    QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
                self.oputyvana = 0

        elif self.oputyvana==0:
            self.rekomendacii_chenge.hide()
            self.frame_delete.hide()
            self.frame_create_kom.hide()
            self.frame_create_potr.hide()
            self.frame_delete.hide()
            self.frame_avtozapovnena.hide()
            self.add_metoduk.setIcon(QIcon('к.png'))
            self.add_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
            self.rekomendacii.setIcon(QIcon('р.png'))
            self.rekomendacii.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
            self.delete_metoduk.setIcon(QIcon('del.png'))
            self.delete_metoduk.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
            self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
            self.potreba.setIcon(QIcon('п.png'))
            self.update_btn_avto.setIcon(QIcon('internet.png'))
            self.update_btn_avto.setIconSize(QSize(int(50 * suma3 / Ui_MainWindow.number), int(50 * suma3 / Ui_MainWindow.number)))
            self.create_number = 0
            self.potreba_number = 0
            self.delete_number = 0
            self.site = 0
            self.rekomendacii_number =0
            self.freme_chenge.hide()
            self.chenge.setIcon(QIcon('chenge.png'))
            self.chenge.setIconSize(QSize(int(35 * suma3 / Ui_MainWindow.number), int(35 * suma3 / Ui_MainWindow.number)))
            self.chenge_number = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('LOGO.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
