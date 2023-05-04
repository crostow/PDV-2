# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: Limpieza de los elementos graficos                              #
# Autor: Mauricio Roman Ruiz Bárcenas                                        #
# Fecha: 15/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################

from datetime import date
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QRect
from PySide6.QtGui import QRegion


def limpieza_pest_4(self):
    self.ui.label_20.setText('')
    self.ui.label_22.setText('')
    self.ui.tableWidget_4.clear()
    self.ui.tableWidget_4.setRowCount(0)
    self.ui.tableWidget_4.setColumnCount(4)
    self.ui.tableWidget_4.clear()
    encabezado_columans_tabla_reportes = ('Ticket', 'Producto', 'Cantidad', 'Monto')
    self.ui.tableWidget_4.setHorizontalHeaderLabels(encabezado_columans_tabla_reportes)



def limpieza_interfaz_pestaña_3_almacen(self):
    self.ui.lineEdit_13.setText('')
    self.ui.lineEdit_9.setText('')
    self.ui.lineEdit_10.setText('')
    self.ui.lineEdit_11.setText('')
    self.ui.lineEdit_12.setText('')
    self.ui.lineEdit_15.setText('')
    self.ui.tableWidget_3.setRowCount(0)
    self.ui.lineEdit_13.setFocus()
    bloqueo_elementos_modificaciom(self)

def bloqueo_elementos_modificaciom(self):
    self.ui.lineEdit_9.setDisabled(True)
    self.ui.lineEdit_10.setDisabled(True)
    self.ui.lineEdit_11.setDisabled(True)
    self.ui.lineEdit_12.setDisabled(True)
    self.ui.lineEdit_15.setDisabled(True)
    self.ui.pushButton_5.setDisabled(True)
    self.ui.pushButton_6.setDisabled(True)

def desbloqueo_elementos_modificaciom(self):
    self.ui.lineEdit_9.setDisabled(False)
    self.ui.lineEdit_10.setDisabled(False)
    self.ui.lineEdit_11.setDisabled(False)
    self.ui.lineEdit_12.setDisabled(False)
    self.ui.lineEdit_15.setDisabled(False)
    self.ui.pushButton_5.setDisabled(False)
    self.ui.pushButton_6.setDisabled(False)

def limpieza_pestaña_2_almacen(self):
    self.ui.lineEdit_5.setText('')
    self.ui.tableWidget_2.clear()
    self.ui.tableWidget_2.setRowCount(0)

def limpieza_compras_almacen(self):
    self.ui.pushButton_11.setMask(QRegion(QRect(2, 2, 45, 45), QRegion.Ellipse))
    # self.ui.pushButton_11.setStyleSheet('background-color: transparent;')
    # self.ui.pushButton_11.setToolTip('Ayuda')
    self.ui.pushButton_11.setStyleSheet("QPushButton {background-color: transparent; border: 2px solid black; "
                                        "border-radius: 29.4px} QPushButton:pressed " "{background-color: yellow;}")

    self.ui.lineEdit.setText('')
    self.ui.lineEdit_2.setText('')
    self.ui.lineEdit_3.setText('')
    self.ui.lineEdit_4.setText('')
    self.ui.lineEdit_14.setText('')
    self.ui.lineEdit_16.setText('')
    self.ui.tableWidget.setRowCount(0)
    self.ui.tableWidget.clear()


def limpieza_interfaz_ingreso(self):
    self.ui.lineEdit.setText('')
    self.ui.lineEdit_2.setText('')
    self.ui.lineEdit.setFocus()

def limpiar_usuario_ingreso(self):
    self.ui.lineEdit_6.setText('')
    self.ui.lineEdit_7.setText('')
    self.ui.checkBox_5.setChecked(False)

def limpiar_usurio_modificar(self):
    self.ui.comboBox.clear()
    self.ui.lineEdit_8.setText('')
    self.ui.checkBox_6.setChecked(False)

def limpiar_usuario_baja(self):
    self.ui.comboBox_2.clear()
    self.ui.checkBox_7.setChecked(False)
    self.ui.checkBox_8.setChecked(False)




