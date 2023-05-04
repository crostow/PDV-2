# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: interfaz principal                                              #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 15/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtCore import QSize

from PySide6.QtGui import QFont, QIcon
import Setup
from datetime import date
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QWidget, \
    QLabel, QLineEdit, QSpacerItem, QPushButton, QGridLayout, QTabWidget, \
    QSizePolicy, QHBoxLayout, QTableWidget, QMessageBox

from PySide6.QtCore import Qt
from Interfaz import Interfaz_principal
from Metodos import Metodos_usuarios, Metodos_almacen, Metodos_venta,\
    Metodos_reportes, barras


class Principal(QMainWindow):
    def __init__(self, parent=None,  *datos):
    # def __init__(self, parent=None):
        super(Principal, self).__init__(parent)


        self.ui = Interfaz_principal.Ui_MainWindow()
        self.ui.setupUi(self)

        self.vendedor = str(datos[0][0])
        b1 = barras.barra_bienvenida(self.vendedor)
        b2 = barras.barra_menu(self)

        self.addToolBar(b1)
        self.addToolBarBreak(Qt.TopToolBarArea)
        self.addToolBar(b2)

        if datos[0][1] == 0:
            btn_1 = self.findChild(QPushButton, 'btn_almacen')
            btn_2 = self.findChild(QPushButton, 'btn_usuarios')
            btn_3 = self.findChild(QPushButton, 'btn_reportes')
            btn_1.setDisabled(True)
            btn_2.setDisabled(True)
            btn_3.setDisabled(True)




        labe_nombre = QLabel()
        labe_nombre.setText('Fecha: ' +str(date.today()))
        # labe_nombre.setText('Atendido por:   '+str(datos [0][0])+ '    Fecha:  '+str(date.today()))
        self.ui.statusbar.addPermanentWidget(labe_nombre,0)



        # self.showMaximized()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.frame.hide()
        self.ui.frame_5.hide()
        self.ui.frame_2.hide()
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)

        self.tab_creada = 0
        self.venta_iniciada = 0
        self.ventas_permitidas = 0

        # self.shortcut_open = QShortcut(QKeySequence('Ctrl+P'), self)
        # self.shortcut_open.activated.connect(self.cobrar)

        # conectamos los metodos con los elementos graficos
        self.ui.checkBox.stateChanged.connect(self.mostrar_alta)
        self.ui.checkBox_3.stateChanged.connect(self.mostrar_baja)
        self.ui.checkBox_2.stateChanged.connect(self.mostrar_modificar)
        self.ui.pushButton_4.clicked.connect(self.cancelar_usuario)
        self.ui.pushButton_3.clicked.connect(self.aceptar_usuario)
        self.ui.checkBox_7.stateChanged.connect(self.habilitar_baja)
        self.ui.checkBox_8.stateChanged.connect(self.habilitar_alta)
        self.ui.comboBox_2.currentIndexChanged.connect(self.verificar_status)
        self.ui.tabWidget.currentChanged.connect(self.cambio_pestaña_almacen)
        self.ui.pushButton.clicked.connect(self.cancelar_ingreso_compra)
        self.ui.lineEdit.returnPressed.connect(self.producto_marca)
        self.ui.lineEdit_3.returnPressed.connect(self.marca_cantidad)
        self.ui.lineEdit_4.returnPressed.connect(self.cantidad_precio)
        self.ui.lineEdit_2.returnPressed.connect(self.precio_aceptar)
        self.ui.pushButton_2.clicked.connect(self.ingreso_compra_nueva)
        self.ui.lineEdit.textChanged.connect(self.filtro_nombre_producto)
        self.ui.lineEdit_5.textChanged.connect(self.filtro_nombre_producto_alta_baja)
        self.ui.tableWidget.cellDoubleClicked.connect(self.llenado_info_compra_nueva)
        self.ui.tableWidget_3.cellDoubleClicked.connect(self.mandar_info_modificacion)
        self.ui.lineEdit_13.textChanged.connect(self.filtro_nombre_producto_modificacion)
        self.ui.pushButton_5.clicked.connect(self.cancelar_modificaciones)
        self.ui.pushButton_6.clicked.connect(self.aplicar_cambio_modificacion_producto)
        self.ui.pushButton_7.clicked.connect(self.busqueda_ventas_hoy)
        self.ui.pushButton_8.clicked.connect(self.busqueda_ventas_fecha_especifica)
        self.ui.pushButton_9.clicked.connect(self.exportar_pdf_corte)
        self.ui.pushButton_10.clicked.connect(self.exportar_inventario_pdf)
        self.ui.pushButton_11.clicked.connect(self.mensaje_de_ayuda)

    def mensaje_de_ayuda(self):
        Metodos_almacen.mostrar_ayuda(self)

    def exportar_inventario_pdf(self):
        Metodos_almacen.export_to_pdf(self)

    def exportar_pdf_corte(self):
        Metodos_reportes.exportar_pdf(self)

    def busqueda_ventas_fecha_especifica(self):
        Metodos_reportes.busqueda_ventas_fecha_especifica(self)

    def busqueda_ventas_hoy(self):
        Metodos_reportes.busqueda_ventas_hoy(self)


    def interfaz_reportes(self):
        Metodos_reportes.cambio_pest_reportes(self)

    def aplicar_cambio_modificacion_producto(self):
        Metodos_almacen.aplicar_modificacion_productos(self)

    def cancelar_modificaciones(self):
        Metodos_almacen.cancelar_modificaciones_producto(self)

    def filtro_nombre_producto_modificacion(self):
        Metodos_almacen.filtro_productos_pest_3(self)

    def mandar_info_modificacion(self):
        Metodos_almacen.mandar_info_modificar_producto(self)

    def llenado_info_compra_nueva(self):
        fila = self.ui.tableWidget.currentRow()
        nombre = self.ui.tableWidget.item(fila, 0).text()
        marca = self.ui.tableWidget.item(fila, 3).text()
        codigo = self.ui.tableWidget.item(fila, 4).text()
        self.ui.lineEdit.setText(nombre)
        self.ui.lineEdit_3.setText(marca)
        self.ui.lineEdit_14.setText(codigo)


    def filtro_nombre_producto_alta_baja(self):
        Metodos_almacen.filtro_nombre_producto_alta_baja(self)

    def filtro_nombre_producto(self):
        Metodos_almacen.filtro_nombre_producto(self)

    def ingreso_compra_nueva(self):
        Metodos_almacen.ingreso_compra_nueva(self)

    def precio_aceptar(self):
        self.ui.pushButton_2.setDefault(True)
        self.ui.pushButton_2.setFocus()

    def cantidad_precio(self):
        self.ui.lineEdit_2.setFocus()

    def marca_cantidad(self):
        self.ui.lineEdit_4.setFocus()

    def producto_marca(self):
        self.ui.lineEdit_3.setFocus()

    def cancelar_ingreso_compra(self):
        Metodos_almacen.cancelar_ingreso_compra(self)

    def cambio_pestaña_almacen(self):
        Metodos_almacen.cambio_pestaña_almacen(self)

    def verificar_status(self):
        Metodos_usuarios.mostrar_status(self)

    def habilitar_baja(self):
        Metodos_usuarios.check_baja(self)

    def habilitar_alta(self):
        Metodos_usuarios.check_alta(self)

    def aceptar_usuario(self):
        Metodos_usuarios.aceptar_usuario(self)

    def cancelar_usuario(self):
        Metodos_usuarios.cancelar_usuario(self)

    def mostrar_modificar(self):
        Metodos_usuarios.modificar_usuario(self)

    def mostrar_baja(self):
        Metodos_usuarios.baja_usuario(self)

    def mostrar_alta(self):
        Metodos_usuarios.alta_usuario(self)

    def interfaz_almacen(self):
        Metodos_almacen.mostrar_pantalla(self)

    def interfaz_usuarios(self):
        Metodos_almacen.interfaz_usuarios(self)

    def venta_nueva(self):
        if self.ventas_permitidas <= 8 :
            if self.ui.stackedWidget.currentIndex() == 1:
                total_tabs = self.tabs.count()
                self.tabs.setCurrentIndex(total_tabs - 1)
                numero_venta = self.tabs.tabText(self.tabs.currentIndex())
                n_p = self.agregar_tab(int(numero_venta[-1]) + 1)
                self.tabs.addTab(n_p,'venta #'+str(int(numero_venta[-1]) + 1))
                self.tabs.setCurrentIndex(self.tabs.count() - 1)
                Metodos_venta.productos_existencia_alta(self, self.contador_ventas)
                self.ventas_permitidas += 1
            else:
                if self.venta_iniciada == 1:
                    self.ui.stackedWidget.setCurrentIndex(1)
                else:
                    if self.tab_creada == 1:
                        self.ui.stackedWidget.setCurrentIndex(1)
                        ventas = 0
                        n_p = self.agregar_tab(ventas)
                        self.tabs.addTab(n_p, 'venta #' + str(self.tabs.count()))
                        self.tabs.setCurrentIndex(self.tabs.count() - 1)
                        num_pest = self.tabs.tabText(self.tabs.currentIndex())
                        self.contador_ventas = int(num_pest[-1])
                        Metodos_venta.productos_existencia_alta(self, self.contador_ventas)
                        self.ventas_permitidas += 1
                    else:
                        ventas = 0
                        self.ui.stackedWidget.setCurrentIndex(1)
                        pestaña = self.interfaz_venta(ventas)
                        self.ui.gridLayout_18.addWidget(pestaña)
                        Metodos_venta.productos_existencia_alta(self, ventas)
                        self.venta_iniciada = 1
                        self.ventas_permitidas +=1
        else:
            QMessageBox.critical(self, 'Alerta', 'llegaste al limite de ventas permitidas')
            self.ui.stackedWidget.setCurrentIndex(1)

        pro = self.findChild(QLineEdit, 'line_{}'.format(int(self.tabs.currentIndex())))
        pro.setFocus()

    def cancelar_venta(self):
        numero_venta = self.tabs.tabText(self.tabs.currentIndex())
        numero = int(numero_venta[-1])
        Metodos_venta.cancelar_venta(self, numero)

        if self.tabs.count() >= 1:
            pass
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.venta_iniciada = 0
            self.tab_creada =1

    def realizar_venta(self):
        numero_venta = self.tabs.tabText(self.tabs.currentIndex())
        Metodos_venta.realizar_venta(self, int(numero_venta[-1]), self.vendedor)

        if self.tabs.count() >= 1:
            pass
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.venta_iniciada = 0
            self.tab_creada = 1

    def interfaz_venta(self, numero):
        self.tabs = QTabWidget()
        self.tabs.setObjectName('tab_{}'.format(numero))
        self.tabs.currentChanged.connect(self.cambio_id_pest)
        tab = QWidget()
        elementos = self.elementos_tab(numero)
        tab.setLayout(elementos)
        self.tabs.addTab(tab, 'venta #'+str(numero))
        return self.tabs

    def agregar_tab(self, numero):
        tab = QWidget()
        elementos = self.elementos_tab(numero)
        tab.setLayout(elementos)
        return tab

    def elementos_tab(self, numero):
        #creamos los elementos que contendra
        label_producto = QLabel('Producto')
        label_producto.setFont(QFont('Source Code Variable', 12))
        label_producto.setObjectName('line_1_{}'.format(numero))

        producto = QLineEdit()
        producto.setFont(QFont('Source Code Variable', 12))
        producto.setObjectName('line_{}'.format(numero))
        producto.setMinimumSize(QSize(541, 25))
        producto.setMaximumSize(QSize(541, 25))
        producto.textChanged.connect(self.tomar_valor_lineedit)
        spacerItem = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout_1 = QHBoxLayout()
        layout_1.addWidget(label_producto)
        layout_1.addWidget(producto)
        layout_1.addItem(spacerItem)


        tabla_1 = QTableWidget()
        tabla_1.verticalHeader().hide()
        tabla_1.setFont(QFont('Source Code Variable', 12))
        tabla_1.setObjectName('tabla_1_{}'.format(numero))
        tabla_1.doubleClicked.connect(self.envio_tabla_venta)

        tabla_2 = QTableWidget()
        tabla_2.setFont(QFont('Source Code Variable', 12))
        tabla_2.verticalHeader().hide()
        tabla_2.setObjectName('tabla_2_{}'.format(numero))
        tabla_2.doubleClicked.connect(self.devolver_pro)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(tabla_1)
        layout_2.addWidget(tabla_2)

        layout_3 = QGridLayout()

        label_total = QLabel('Total')
        label_total.setFont(QFont('Source Code Variable', 12))
        label_total.setObjectName('label_2_{}'.format(numero))
        label_total.setMinimumSize(QSize(110, 25))
        label_total.setMaximumSize(QSize(110, 25))

        total = QLabel('')
        total.setFont(QFont('Source Code Variable', 12))
        total.setObjectName('label_3_{}'.format(numero))
        total.setMinimumSize(QSize(110, 25))
        total.setMaximumSize(QSize(110, 25))

        boton_cancelar = QPushButton('   F9-Cancelar   '  )
        boton_cancelar.setFont(QFont('Source Code Variable', 12))
        boton_cancelar.setObjectName('boton_1_{}'.format(numero))
        boton_cancelar.clicked.connect(self.cancelar_venta)

        boton_aceptar = QPushButton('F8-Aceptar')
        boton_aceptar.setFont(QFont('Source Code Variable', 12))
        boton_aceptar.setObjectName('boton_2_{}'.format(numero))
        boton_aceptar.clicked.connect(self.realizar_venta)

        horizontalSpacer_2 = QSpacerItem(577, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalSpacer_3 = QSpacerItem(577, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout_3.addItem(horizontalSpacer_2,0,0,1,2)
        layout_3.addItem(horizontalSpacer_3,1,0,1,1)

        layout_3.addWidget(label_total,0,2,1,2)
        layout_3.addWidget(total,0,4,1,1)
        layout_3.addWidget(boton_cancelar,1,1,1,2)
        layout_3.addWidget(boton_aceptar,1,3,1,2)

        tab_grid = QGridLayout()
        tab_grid.addLayout(layout_1,0,0,1,1)
        tab_grid.addLayout(layout_2,1,0,1,1)
        tab_grid.addLayout(layout_3,2,0,1,1)
        return tab_grid

    def tomar_valor_lineedit(self):
        Metodos_venta.filtros_productos_existentes(self, self.contador_ventas)

    def envio_tabla_venta(self):
        Metodos_venta.envio_producto_venta(self, self.contador_ventas)

    def cambio_id_pest(self):
        if self.tabs.count() >= 1:
            numero_venta =  self.tabs.tabText(self.tabs.currentIndex())
            self.contador_ventas = int(numero_venta[-1])
            Metodos_venta.filtros_productos_existentes(self, self.contador_ventas)

    def devolver_pro(self):
        Metodos_venta.regreso_productos(self, self.contador_ventas)

    def salir_aplicacion(self):
        try:
            if self.tabs.count() <= 0:
                self.close()
                ventana_i = Setup.Inicio_aplicacion(self)
                ventana_i.show()
            else:
                QMessageBox.critical(self, 'Alerta','Tienes ventas pendientes')
        except AttributeError:
            self.close()
            ventana_i = Setup.Inicio_aplicacion(self)
            ventana_i.show()


    def contextMenuEvent(self, event):
        if self.ui.tableWidget_2.selectionModel().selection().indexes():
            for i in self.ui.tableWidget_2.selectionModel().selection().indexes():
                fila, columna = i.row(), i.column()
            menu = QMenu()
            menu_alta = menu.addAction("Alta")
            menu_baja = menu.addAction("Baja")
            menu_salir = menu.addAction("Salir")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == menu_alta:
                pro = self.ui.tableWidget_2.item(fila,0).text()
                marca = self.ui.tableWidget_2.item(fila,3).text()
                Metodos_almacen.cambio_status_producto_almacen_menu_alta(self, pro, marca)
                Metodos_almacen.busqueda_total_productos_alta_baja(self)
                self.ui.tableWidget_2.clearSelection()
            if action == menu_baja:
                pro = self.ui.tableWidget_2.item(fila,0).text()
                marca = self.ui.tableWidget_2.item(fila,3).text()
                Metodos_almacen.cambio_status_producto_almacen_baja(self, pro, marca)
                Metodos_almacen.busqueda_total_productos_alta_baja(self)
                self.ui.tableWidget_2.clearSelection()
            if action == menu_salir:
                self.ui.tableWidget_2.clearSelection()

        try:
            tabla_productos = self.findChild(QTableWidget, 'tabla_1_{}'.format(self.contador_ventas))
            tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(self.contador_ventas))

            if tabla_productos.selectionModel().selection().indexes():
                for i in tabla_productos.selectionModel().selection().indexes():
                    fila, columna = i.row(), i.column()
                menu = QMenu()
                menu_cantidad = menu.addAction("Cantidad")
                menu_salir = menu.addAction("Salir")
                action = menu.exec_(self.mapToGlobal(event.pos()))
                if action == menu_cantidad:
                    Metodos_venta.envio_producto_venta_clik_derecho(self, self.contador_ventas, fila)
                elif action == menu_salir:
                    tabla_productos.clearSelection()

            if tabla_venta.selectionModel().selection().indexes():
                for i in tabla_venta.selectionModel().selection().indexes():
                    fila, columna = i.row(), i.column()
                menu = QMenu()
                menu_devolver = menu.addAction("Devolver")
                menu_salir = menu.addAction("Salir")
                action = menu.exec_(self.mapToGlobal(event.pos()))
                if action == menu_devolver:
                    Metodos_venta.regreso_productos_click_derecho(self, fila, self.contador_ventas)
                elif action == menu_salir:
                   tabla_venta.clearSelection()
        except AttributeError:
            pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_F4:
            self.salir_aplicacion()
        elif QKeyEvent.key() == Qt.Key_F5:
            self.venta_nueva()
        elif QKeyEvent.key() == Qt.Key_F8:
            try:
                if self.tabs.count() <= 0:
                    pass
                else:
                    self.realizar_venta()
            except AttributeError:
                pass
        elif QKeyEvent.key() == Qt.Key_F9:
            try:
                if self.tabs.count() <= 0:
                    pass
                else:
                    self.cancelar_venta()
            except AttributeError:
                pass

        elif QKeyEvent.key() == Qt.Key_Right:
            if QApplication.keyboardModifiers() == Qt.AltModifier:
                total_tabs = self.tabs.count()
                if total_tabs <=1:
                    pass
                else:
                    num_pest = self.tabs.tabText(self.tabs.currentIndex())
                    num_pest = int(num_pest[-1])
                    if num_pest >= (total_tabs - 1):
                        pass
                    else:
                        self.tabs.setCurrentIndex(num_pest + 1)
        elif QKeyEvent.key() == Qt.Key_Left:
            if QApplication.keyboardModifiers() == Qt.AltModifier:
                if self.tabs.currentIndex() <= 0:
                    pass
                else:
                    num_pest = self.tabs.tabText(self.tabs.currentIndex())
                    num_pest = int(num_pest[-1])

                    self.tabs.setCurrentIndex(num_pest - 1)

