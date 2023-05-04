# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: metodos para usuarios                                           #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 18/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################

import hashlib
from PySide6.QtWidgets import QMessageBox
from Interfaz import Limpieza_interfaz
from DB import querys_db

def mostrar_status(self):
    try:
        nom = self.ui.comboBox_2.currentText()
        if nom == 'Elige un usuario':
            self.ui.checkBox_7.setChecked(False)
            self.ui.checkBox_8.setChecked(False)
        else:
            usuario = querys_db.status_usuario(nom)
            if usuario.status == 'alta':
                self.ui.checkBox_7.setChecked(False)
                self.ui.checkBox_8.setChecked(True)
            else:
                self.ui.checkBox_8.setChecked(False)
                self.ui.checkBox_7.setChecked(True)
    except ValueError:
        pass

def aceptar_usuario(self):
    if self.ui.checkBox.isChecked():
        nombre = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_7.text()
        password = hashlib.sha256(password.encode())
        password = password.hexdigest()
        if self.ui.checkBox_5.isChecked():
            permisos = 1
        else:
            permisos = 0
        if nombre == '':
            QMessageBox.critical(self, 'ALERTA', 'Falta nombre')
        elif password == '':
            QMessageBox.critical(self,'ALERTA','Faltan contraseña')
        else:
            querys_db.ingreso_nuevo(nombre, password, permisos)
            cancelar_usuario(self)

    if self.ui.checkBox_3.isChecked():
        nombre = self.ui.comboBox_2.currentText()
        if nombre == 'Elige un usuario':
            QMessageBox.critical(self,'ALERTA','No elegiste usuario')
        else:
            if self.ui.checkBox_7.isChecked() == False and self.ui.checkBox_8.isChecked() == False:
                QMessageBox.critical(self, 'ALERTA', 'No seleccionaste permisos')
            else:
                if self.ui.checkBox_7.isChecked():
                    status = 'baja'
                elif self.ui.checkBox_8.isChecked():
                    status = 'alta'
                querys_db.baja_usuarios(nombre, status)
                cancelar_usuario(self)


    elif self.ui.checkBox_2.isChecked():
        nombre = self.ui.comboBox.currentText()
        password = self.ui.lineEdit_8.text()
        password = hashlib.sha256(password.encode())
        password = password.hexdigest()
        if self.ui.comboBox.currentText() == 'Elige un usuario':
            QMessageBox.critical(self,'ALERTA','No elegiste usuario')
        else:
            if self.ui.lineEdit_8.text() == '':
                QMessageBox.critical(self, 'ALERTA', 'Ingresa contraseña')
            else:
                if self.ui.checkBox_6.isChecked():
                    permisos = 1
                else:
                    permisos = 0
                querys_db.modificar_usuario(nombre, password, permisos)
                cancelar_usuario(self)


def check_baja(self):
    if self.ui.checkBox_7.isChecked():
        self.ui.checkBox_8.setDisabled(True)
    else:
        self.ui.checkBox_8.setDisabled(False)

def check_alta(self):
    if self.ui.checkBox_8.isChecked():
        self.ui.checkBox_7.setDisabled(True)
    else:
        self.ui.checkBox_7.setDisabled(False)



def alta_usuario(self):
    Limpieza_interfaz.limpiar_usuario_ingreso(self)
    if self.ui.checkBox.isChecked():
        self.ui.checkBox_3.setDisabled(True)
        self.ui.checkBox_2.setDisabled(True)
        self.ui.frame.show()
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_4.setDisabled(False)
    else:
        self.ui.frame.hide()
        self.ui.checkBox_3.setDisabled(False)
        self.ui.checkBox_2.setDisabled(False)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)

def baja_usuario(self):
    Limpieza_interfaz.limpiar_usuario_baja(self)
    if self.ui.checkBox_3.isChecked():
        resultado = querys_db.busqueda_usuarios_baja_alta()
        if len(resultado) == 0 :
            QMessageBox.critical(self,'ALERTA','No existen usuarios activos')
            self.ui.checkBox_3.setChecked(False)
        else:
            self.ui.comboBox_2.addItem('Elige un usuario')
            for i in range(len(resultado)):
                self.ui.comboBox_2.addItem(resultado[i].nombre)
            self.ui.checkBox.setDisabled(True)
            self.ui.checkBox_2.setDisabled(True)
            self.ui.frame_2.show()
            self.ui.pushButton_3.setDisabled(False)
            self.ui.pushButton_4.setDisabled(False)
    else:
        self.ui.frame_2.hide()
        self.ui.checkBox.setDisabled(False)
        self.ui.checkBox_2.setDisabled(False)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)

def modificar_usuario(self):
    Limpieza_interfaz.limpiar_usurio_modificar(self)
    if self.ui.checkBox_2.isChecked():
        resultado = querys_db.busqueda_usuarios_activos()
        if len(resultado) == 0 :
            QMessageBox.critical(self,'ALERTA','No existen usuarios activos')
        else:
            self.ui.comboBox.addItem('Elige un usuario')
            for i in range(len(resultado)):
                self.ui.comboBox.addItem(resultado[i].nombre)
            self.ui.checkBox.setDisabled(True)
            self.ui.checkBox_3.setDisabled(True)
            self.ui.frame_5.show()
            self.ui.pushButton_3.setDisabled(False)
            self.ui.pushButton_4.setDisabled(False)
    else:
        self.ui.frame_5.hide()
        self.ui.checkBox.setDisabled(False)
        self.ui.checkBox_3.setDisabled(False)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)

def cancelar_usuario(self):
    Limpieza_interfaz.limpiar_usurio_modificar(self)
    Limpieza_interfaz.limpiar_usuario_baja(self)
    Limpieza_interfaz.limpiar_usuario_ingreso(self)
    self.ui.checkBox.setDisabled(False)
    self.ui.checkBox_2.setDisabled(False)
    self.ui.checkBox_3.setDisabled(False)
    self.ui.pushButton_3.setDisabled(True)
    self.ui.pushButton_4.setDisabled(True)
    self.ui.frame_2.hide()
    self.ui.frame_5.hide()
    self.ui.frame.hide()
    self.ui.checkBox.setChecked(False)
    self.ui.checkBox_2.setChecked(False)
    self.ui.checkBox_3.setChecked(False)

