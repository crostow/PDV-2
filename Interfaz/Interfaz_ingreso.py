# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ingreso.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

import iconos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(277, 300)
        MainWindow.setMinimumSize(QSize(277, 300))
        MainWindow.setMaximumSize(QSize(277, 300))
        icon = QIcon()
        icon.addFile(u":/icon/023-sale.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(77, 121, 124);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(241, 151))
        self.label_3.setMaximumSize(QSize(241, 151))
        self.label_3.setPixmap(QPixmap(u":/icon/punto-de-venta.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(240, 28))
        self.lineEdit.setMaximumSize(QSize(240, 28))
        font = QFont()
        font.setFamily(u"Source Code Variable")
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(240, 28))
        self.lineEdit_2.setMaximumSize(QSize(240, 28))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(110, 31))
        self.pushButton.setMaximumSize(QSize(110, 31))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 240, 216);")
        self.pushButton.setAutoDefault(True)

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(110, 31))
        self.pushButton_2.setMaximumSize(QSize(110, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 240, 216);")
        self.pushButton_2.setAutoDefault(True)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_3.setText("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
    # retranslateUi

