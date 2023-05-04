# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
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
        MainWindow.resize(1102, 727)
        MainWindow.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_17 = QGridLayout(self.centralwidget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")

        self.gridLayout_2.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_21 = QGridLayout(self.page_3)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font = QFont()
        font.setFamily(u"Source Code Variable")
        font.setPointSize(12)
        font.setItalic(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_13 = QGridLayout(self.tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(120, 30))
        self.lineEdit_4.setMaximumSize(QSize(120, 30))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_23, 1, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 29))
        self.pushButton_2.setMaximumSize(QSize(100, 29))
        self.pushButton_2.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 8, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.tab)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(70, 29))
        self.lineEdit_16.setMaximumSize(QSize(70, 29))
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_16, 1, 5, 1, 1)

        self.lineEdit_14 = QLineEdit(self.tab)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(206, 29))
        self.lineEdit_14.setMaximumSize(QSize(206, 29))
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_14, 1, 7, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 0, 9, 1, 1)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_18, 1, 6, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(70, 29))
        self.lineEdit_2.setMaximumSize(QSize(70, 29))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 3, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 1, 9, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(500, 28))
        self.lineEdit.setMaximumSize(QSize(500, 28))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 5)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(717, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 0, 1, 7)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 29))
        self.pushButton.setMaximumSize(QSize(100, 29))
        self.pushButton.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton, 2, 7, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(206, 29))
        self.lineEdit_3.setMaximumSize(QSize(206, 29))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 7, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_11 = QPushButton(self.tab)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(50, 50))
        self.pushButton_11.setMaximumSize(QSize(50, 50))
        self.pushButton_11.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/049-light bulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(717, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.tab)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_10, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/icon/013-fast-delivery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.tableWidget_2, 1, 0, 1, 2)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/icon/023-swap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_16 = QGridLayout(self.tab_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.lineEdit_13 = QLineEdit(self.tab_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.lineEdit_13)


        self.gridLayout_15.addLayout(self.horizontalLayout_7, 0, 0, 1, 2)

        self.tableWidget_3 = QTableWidget(self.tab_3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.gridLayout_15.addWidget(self.tableWidget_3, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.tab_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_9.setFont(font1)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_9, 0, 1, 1, 4)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout.addWidget(self.label_15, 0, 5, 1, 1)

        self.lineEdit_11 = QLineEdit(self.tab_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font1)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_11, 0, 6, 1, 1)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.tab_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font1)
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.tab_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font1)
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_12, 1, 3, 1, 1)

        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout.addWidget(self.label_19, 1, 4, 1, 1)

        self.lineEdit_15 = QLineEdit(self.tab_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setFont(font1)
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_15, 1, 5, 1, 2)


        self.gridLayout_15.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pushButton_5 = QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(130, 33))
        self.pushButton_5.setMaximumSize(QSize(130, 33))
        self.pushButton_5.setFont(font)

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(134, 33))
        self.pushButton_6.setMaximumSize(QSize(134, 33))
        self.pushButton_6.setFont(font)

        self.horizontalLayout_8.addWidget(self.pushButton_6)


        self.gridLayout_15.addLayout(self.horizontalLayout_8, 3, 0, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/icon/036-edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")

        self.gridLayout_21.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_11 = QGridLayout(self.page_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer = QSpacerItem(790, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(417, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 2, 1, 2)

        self.checkBox = QCheckBox(self.page_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.gridLayout_10.addWidget(self.checkBox, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.page_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)

        self.gridLayout_10.addWidget(self.checkBox_3, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.page_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.gridLayout_10.addWidget(self.checkBox_2, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(277, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.frame = QFrame(self.page_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(991, 55))
        self.frame.setMaximumSize(QSize(991, 55))
        self.frame.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lineEdit_6)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_7)

        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)

        self.horizontalLayout_2.addWidget(self.checkBox_5)

        self.horizontalSpacer_6 = QSpacerItem(105, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_8.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(991, 55))
        self.frame_5.setMaximumSize(QSize(991, 55))
        self.frame_5.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 10, 957, 35))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(69, 25))
        self.label_10.setMaximumSize(QSize(69, 25))
        self.label_10.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(232, 33))
        self.comboBox.setMaximumSize(QSize(232, 33))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(93, 25))
        self.label_11.setMaximumSize(QSize(93, 25))
        self.label_11.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(220, 33))
        self.lineEdit_8.setMaximumSize(QSize(220, 33))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.lineEdit_8)

        self.checkBox_6 = QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setMinimumSize(QSize(94, 31))
        self.checkBox_6.setMaximumSize(QSize(94, 31))
        self.checkBox_6.setFont(font)

        self.horizontalLayout_3.addWidget(self.checkBox_6)

        self.horizontalSpacer_7 = QSpacerItem(217, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.gridLayout_8.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(991, 55))
        self.frame_2.setMaximumSize(QSize(991, 55))
        self.frame_2.setStyleSheet(u"background-color: rgb(249, 248, 248);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 781, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(90, 25))
        self.label_12.setMaximumSize(QSize(90, 25))
        self.label_12.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.comboBox_2 = QComboBox(self.layoutWidget1)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(250, 33))
        self.comboBox_2.setMaximumSize(QSize(250, 33))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.checkBox_7 = QCheckBox(self.layoutWidget1)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(84, 23))
        self.checkBox_7.setMaximumSize(QSize(84, 23))
        self.checkBox_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.layoutWidget1)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setMinimumSize(QSize(84, 23))
        self.checkBox_8.setMaximumSize(QSize(84, 23))
        self.checkBox_8.setFont(font)

        self.horizontalLayout_4.addWidget(self.checkBox_8)

        self.horizontalSpacer_8 = QSpacerItem(247, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.gridLayout_8.addWidget(self.frame_2, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(547, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.page_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(130, 33))
        self.pushButton_4.setMaximumSize(QSize(130, 33))
        self.pushButton_4.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.page_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(130, 33))
        self.pushButton_3.setMaximumSize(QSize(130, 33))
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout_8.addLayout(self.horizontalLayout, 4, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_19 = QGridLayout(self.page_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_7 = QPushButton(self.page_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)

        self.gridLayout_12.addWidget(self.pushButton_7, 0, 0, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(47, 27, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.page_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)

        self.gridLayout_12.addWidget(self.pushButton_8, 0, 4, 1, 3)

        self.horizontalSpacer_13 = QSpacerItem(57, 27, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_13, 0, 7, 1, 2)

        self.dateEdit = QDateEdit(self.page_5)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.dateEdit, 0, 9, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_14, 0, 10, 1, 1)

        self.label = QLabel(self.page_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label, 1, 0, 1, 1)

        self.label_20 = QLabel(self.page_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(70, 30))
        self.label_20.setMaximumSize(QSize(70, 30))
        self.label_20.setFont(font)

        self.gridLayout_12.addWidget(self.label_20, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(87, 30, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_9, 1, 2, 1, 2)

        self.label_21 = QLabel(self.page_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_21, 1, 4, 1, 1)

        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 30))
        self.label_22.setMaximumSize(QSize(100, 30))
        self.label_22.setFont(font)

        self.gridLayout_12.addWidget(self.label_22, 1, 5, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(87, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_15, 1, 6, 1, 2)

        self.pushButton_9 = QPushButton(self.page_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)

        self.gridLayout_12.addWidget(self.pushButton_9, 1, 8, 1, 2)

        self.horizontalSpacer_11 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 1, 10, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.tableWidget_4 = QTableWidget(self.page_5)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.gridLayout_14.addWidget(self.tableWidget_4, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout_17.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_16)
        QWidget.setTabOrder(self.lineEdit_16, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.tableWidget_3)
        QWidget.setTabOrder(self.tableWidget_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.checkBox_6)
        QWidget.setTabOrder(self.checkBox_6, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.checkBox_7)
        QWidget.setTabOrder(self.checkBox_7, self.checkBox_8)
        QWidget.setTabOrder(self.checkBox_8, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.checkBox_5)
        QWidget.setTabOrder(self.checkBox_5, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_15)
        QWidget.setTabOrder(self.lineEdit_15, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.tableWidget_4)
        QWidget.setTabOrder(self.tableWidget_4, self.tableWidget_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"P/Compra ", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_4.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"P/Venta  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Aceptar ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_16.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_14.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"C/Barras", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Exportar a pdf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Compras", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Altas - Bajas", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"  Aceptar  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Modificar productos", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Selecciona una opci\u00f3n", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Ingreso", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Alta/Baja", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Admin.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.comboBox.setCurrentText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Admin.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Baja", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"  Ventas realizadas hoy  ", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"  Ventas realizadas por fecha  ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"# ventas: ", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"total efectivo", None))
        self.label_22.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Exportar a pdf", None))
    # retranslateUi

