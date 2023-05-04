# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: barras de menu personalizadas                                   #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 15/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QSizePolicy, QLabel, QToolBar, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import iconos_rc


def barra_bienvenida(vendedor):
    barra_bienvenida = QToolBar()
    barra_bienvenida.setMovable(False)
    # barra_bienvenida.setStyleSheet('background-color: rgb(30, 30, 30); color: white;')
    # barra_bienvenida.setStyleSheet('background: rgb(30, 30, 30); border: 0 8px')

    spacer = QWidget()
    spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    logo = QLabel()
    logo.setFixedSize(80, 80)
    img = (':icon/punto-de-venta.png')
    # logo.setPixmap(img)
    logo.setScaledContents(1)

    nom = QLabel('''    PUNTO DE
       VENTA''')
    nom.setFont(QFont('Arial black', 20))
    nom.setStyleSheet('color: rgb(57,167,194)')

    atiende = QLabel()
    atiende.setText('USUARIO:')
    atiende.setFont(QFont('Arial black', 15))
    atiende.setAlignment(Qt.AlignCenter)

    usuario = QLabel()
    usuario.setText(' '+str(vendedor))
    usuario.setFont(QFont('Arial bold', 15))
    usuario.setStyleSheet('color: rgb(57,167,194)')

    barra_bienvenida.addWidget(logo)
    barra_bienvenida.addWidget(nom)
    barra_bienvenida.addWidget(spacer)
    barra_bienvenida.addWidget(atiende)
    barra_bienvenida.addWidget(usuario)

    return barra_bienvenida

def barra_menu(self):
    barra_menu = QToolBar()
    barra_menu.setMovable(False)
    # barra_menu.setStyleSheet('borde: 1px')

    btn_venta = QPushButton()
    btn_venta.setObjectName('btn_venta')
    btn_venta.setText('F5-Venta')
    icon = QIcon()
    icon.addFile(':/icon/rebaja.png', QSize(), QIcon.Normal, QIcon.Off)
    btn_venta.setIcon(icon)
    btn_venta.setFixedSize(100,30)
    btn_venta.clicked.connect(self.venta_nueva)

    btn_almacen = QPushButton()
    btn_almacen.setText('Almacen')
    btn_almacen.setObjectName('btn_almacen')
    icon = QIcon()
    icon.addFile(':icon/notebook-1.png', QSize(), QIcon.Normal, QIcon.Off)
    btn_almacen.setIcon(icon)
    btn_almacen.setFixedSize(100,30)
    btn_almacen.clicked.connect(self.interfaz_almacen)


    btn_usuarios = QPushButton()
    btn_usuarios.setText('Usuarios')
    btn_usuarios.setObjectName('btn_usuarios')
    icon = QIcon()
    icon.addFile(':icon/users.png', QSize(), QIcon.Normal, QIcon.Off)
    btn_usuarios.setIcon(icon)
    btn_usuarios.setFixedSize(100, 30)
    btn_usuarios.clicked.connect(self.interfaz_usuarios)


    btn_reportes = QPushButton()
    btn_reportes.setText('Reportes')
    btn_reportes.setObjectName('btn_reportes')

    icon = QIcon()
    icon.addFile(':icon/016-file.png', QSize(), QIcon.Normal, QIcon.Off)
    btn_reportes.setIcon(icon)
    btn_reportes.setFixedSize(100, 30)
    btn_reportes.clicked.connect(self.interfaz_reportes)


    btn_salir = QPushButton()
    btn_salir.setText('Salir')
    icon = QIcon()
    icon.addFile(':icon/exit-1.png', QSize(), QIcon.Normal, QIcon.Off)
    btn_salir.setIcon(icon)
    btn_salir.setFixedSize(100, 30)
    btn_salir.clicked.connect(self.salir_aplicacion)


    barra_menu.addWidget(btn_venta)
    barra_menu.addWidget(btn_almacen)

    barra_menu.addWidget(btn_usuarios)
    barra_menu.addWidget(btn_reportes)
    barra_menu.addWidget(btn_salir)


    return barra_menu