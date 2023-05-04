# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: Inicio de la aplicacion                                         #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 02/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
import sys
import hashlib
import Principal
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Interfaz import Interfaz_ingreso, Limpieza_interfaz
from DB import querys_db

class Inicio_aplicacion (QMainWindow):
    def __init__(self, parent = None):
        super(Inicio_aplicacion, self).__init__(parent)

        self.ui = Interfaz_ingreso.Ui_MainWindow()
        self.ui.setupUi(self)



        self.setWindowTitle('PDV')
        Limpieza_interfaz.limpieza_interfaz_ingreso(self)
        self.ui.lineEdit.setFocus()

        self.ui.pushButton_2.clicked.connect(self.verificar_usuario)
        self.ui.pushButton.clicked.connect(self.cerrar_aplicacon)
        self.ui.lineEdit.returnPressed.connect(self.cambio_label)
        self.ui.lineEdit_2.returnPressed.connect(self.cambio_boton)

    def cambio_boton(self):
        self.ui.pushButton_2.setDefault(True)
        self.ui.pushButton_2.setFocus()

    def cambio_label(self):
        self.ui.lineEdit_2.setFocus()

    def cerrar_aplicacon(self):
        self.close()

    def verificar_usuario(self):
        datos =[]
        nombre = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        password_enc = hashlib.sha256(password.encode())
        if nombre == '' or password == '':
            QMessageBox.critical(self, 'Alerta', 'Datos incompletos')
            Limpieza_interfaz.limpieza_interfaz_ingreso(self)
            self.ui.pushButton_2.setDefault(False)
        else:
            datos = querys_db.busqueda_usuarios(nombre)
            if datos == []:
                QMessageBox.critical(self, 'Alerta', 'No existe usuario')
                Limpieza_interfaz.limpieza_interfaz_ingreso(self)
                self.ui.pushButton_2.setDefault(False)
            elif datos[0].password != password_enc.hexdigest():
                QMessageBox.critical(self, 'Alerta', 'Contraseña incorrecta')
                Limpieza_interfaz.limpieza_interfaz_ingreso(self)
                self.ui.pushButton_2.setDefault(False)
            else:
                self.close()
                datos = [datos[0].nombre, datos[0].permisos]
                ventana_p = Principal.Principal(self, datos)
                ventana_p.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Inicio_aplicacion()
    ventana.show()
    sys.exit(app.exec_())