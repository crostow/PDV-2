# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: metodos de la interfaz de venta                                 #
# Autor: Mauricio Roman Ruiz Bárcenas                                        #
# Fecha: 20/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
from PySide6.QtCore import QSize, QObject
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget, \
    QMessageBox, QInputDialog, QLabel, QLineEdit, QTabWidget, QPushButton
from DB import querys_db


def productos_existencia_alta(self, numero):
    tabla_busqueda = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    resultado = querys_db.productos_existentes()
    if resultado == 0:
        tabla_busqueda.setRowCount(0)
    else:
        envio_informacion_tabla_ventas(self, resultado, numero)


def filtros_productos_existentes(self, numero):
    producto = self.findChild(QLineEdit, 'line_{}'.format(numero))
    tabla_busqueda = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    try:
        resultado = querys_db.filtro_busqueda_venta(producto.text())
        if len(resultado) == 0:
            tabla_busqueda.setRowCount(0)
        elif len(resultado) == 1:
            envio_informacion_tabla_ventas(self, resultado, numero)

            envio_producto_venta_un_solo_resultado(self, resultado, numero)
        else:
            envio_informacion_tabla_ventas(self, resultado, numero)
    except AttributeError:
        pass

def envio_producto_venta_un_solo_resultado(self, resultado, numero):
    envio_informacion_tabla_ventas(self, resultado, numero)
    linea_producto_venta = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    producto = self.findChild(QLineEdit, 'line_{}'.format(numero))
    pro = linea_producto_venta.item(0, 0).text()
    precio = linea_producto_venta.item(0, 1).text()
    cant = int(linea_producto_venta.item(0, 2).text())
    marca = linea_producto_venta.item(0, 3).text()
    if cant <= 0:
        QMessageBox.critical(self, 'ALERTA', 'No hay productos en existencia')
    else:
        querys_db.restar_producto_venta(pro, marca)
        producto.setText('')
        filtros_productos_existentes(self, numero)
        linea_producto_venta.clearSelection()
        envio_producto_tabla_2(self, pro, marca, precio, numero)

def envio_informacion_tabla_ventas(self, resultado, numero):
    tabla_busqueda = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    tabla_busqueda.clear()
    tabla_busqueda.setColumnCount(4)
    encabezado_columans_tabla_busqueda = ('Producto', 'Precio', 'Cantidad', 'Marca')
    tabla_busqueda.setHorizontalHeaderLabels(encabezado_columans_tabla_busqueda)
    tabla_busqueda.setRowCount(len(resultado))
    for i in range(len(resultado)):
        item = QTableWidgetItem()
        item.setText(str(resultado[i].producto))
        tabla_busqueda.setItem(i, 0, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].precio_venta))
        tabla_busqueda.setItem(i, 1, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].cantidad_existente))
        tabla_busqueda.setItem(i, 2, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].marca))
        tabla_busqueda.setItem(i, 3, item)
    color_producto_venta(self, numero)


def color_producto_venta(self, numero):
    tabla_busqueda = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    filas = tabla_busqueda.rowCount()
    for i in range(filas):
        cant = int(tabla_busqueda.item(i, 2).text())
        if cant <= 5:
            for j in range(4):
                tabla_busqueda.item(i, j).setBackground(QColor(219, 88, 96))
        elif cant >= 5 and cant <= 20:
            for j in range(4):
                tabla_busqueda.item(i, j).setBackground(QColor(237, 212, 0))
        elif cant >= 20:
            for j in range(4):
                tabla_busqueda.item(i, j).setBackground(QColor(133,183,88))
    tabla_busqueda.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    tabla_busqueda.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    tabla_busqueda.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    tabla_busqueda.setEditTriggers(QTableWidget.NoEditTriggers)

def envio_producto_venta(self, numero):
    linea_producto_venta = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    fila = linea_producto_venta.currentRow()
    pro = linea_producto_venta.item(fila, 0).text()
    precio = linea_producto_venta.item(fila, 1).text()
    cant = int(linea_producto_venta.item(fila, 2).text())
    marca = linea_producto_venta.item(fila, 3).text()
    if cant <= 0:
        QMessageBox.critical(self, 'ALERTA', 'No hay productos en existencia')
    else:
        querys_db.restar_producto_venta(pro, marca)
        filtros_productos_existentes(self, numero)
        linea_producto_venta.clearSelection()
        envio_producto_tabla_2(self, pro, marca, precio, numero)

def envio_producto_tabla_2(self, pro, marca, precio, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    bandera_venta = 0
    fila_suma = None
    filas = tabla_venta.rowCount()
    if filas <= 0:
        envio_informacion_tabla_2(self, pro, marca, precio, numero)
    elif filas > 0:
        for i in range(filas):
            if tabla_venta.item(i, 0).text() == pro and tabla_venta.item(i, 2).text() == marca:
                bandera_venta = 1
                # valor de la fila a sumar prodructos
                fila_suma = i
        if bandera_venta == 1:
            cant = int(tabla_venta.item(fila_suma, 3).text())
            item = QTableWidgetItem()
            item.setText(str(cant + 1))
            tabla_venta.setItem(fila_suma, 3, item)
            calcular_producto_total(self, numero)
        else:
            envio_informacion_tabla_2(self, pro, marca, precio, numero)

def envio_informacion_tabla_2(self, pro, marca, precio, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    tabla_venta.insertRow(tabla_venta.rowCount())
    tabla_venta.setColumnCount(5)
    encabezado_tabla_venta = ('Producto', 'Precio', 'Marca', 'Cantidad', 'Total')
    tabla_venta.setHorizontalHeaderLabels(encabezado_tabla_venta)
    item = QTableWidgetItem()
    item.setText(str(pro))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 0, item)
    item = QTableWidgetItem()
    item.setText(str(precio))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 1, item)
    item = QTableWidgetItem()
    item.setText(str(marca))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 2, item)
    item = QTableWidgetItem()
    item.setText(str('1'))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 3, item)
    calcular_producto_total(self, numero)
    tabla_venta.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    tabla_venta.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    tabla_venta.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    tabla_venta.setEditTriggers(QTableWidget.NoEditTriggers)


def calcular_producto_total(self, numero):
    total = 0
    t1 = 0
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    filas = tabla_venta.rowCount()
    label_suma = self.findChild(QLabel, 'label_3_{}'.format(numero))
    for i in range(filas):
        precio = float(tabla_venta.item(i, 1).text())
        cantidad = float(tabla_venta.item(i, 3).text())
        total = precio * cantidad
        item =QTableWidgetItem()
        item.setText(str(round(total,2)))
        tabla_venta.setItem(i, 4, item)

    for j in range(filas):
        t2 = 0
        t2 = float(tabla_venta.item(j, 4).text())
        t1 += t2
    label_suma.setText(str(t1))

def envio_producto_venta_clik_derecho(self,numero,  fila):
    tabla_pro = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))

    pro = tabla_pro.item(fila, 0).text()
    marca = tabla_pro.item(fila, 3).text()
    precio = float(tabla_pro.item(fila, 1).text())
    existencia = int(tabla_pro.item(fila, 2).text())
    cantidad, ok = QInputDialog.getInt(self, 'Producto', 'Cantidad')
    if ok and cantidad <= existencia:
        querys_db.restar_producto_venta_click_derecho(pro, marca, cantidad)
        filtros_productos_existentes(self, numero)
        tabla_pro.clearSelection()
        envio_producto_tabla_2_click_derecho(self, pro, marca, precio, cantidad, numero)
    elif ok and cantidad > existencia:
        QMessageBox.critical(self, 'ALERTA', 'No hay suficiente producto para surtir')


def envio_producto_tabla_2_click_derecho(self, pro, marca, precio, cantidad, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))

    bandera_venta = 0
    fila_suma = None

    filas = tabla_venta.rowCount()
    if filas <= 0:
        envio_informacion_tabla_2_click_derecho(self, pro, marca, precio, cantidad, numero)
    elif filas > 0:
        for i in range(filas):
            if tabla_venta.item(i, 0).text() == pro and tabla_venta.item(i, 2).text() == marca:
                bandera_venta = 1
                # valor de la fila a sumar prodructos
                fila_suma = i

        if bandera_venta == 1:
            cant = int(tabla_venta.item(fila_suma, 3).text())
            item = QTableWidgetItem()
            item.setText(str(cant + cantidad))
            tabla_venta.setItem(fila_suma, 3, item)
            calcular_producto_total(self, numero)
        else:
            envio_informacion_tabla_2_click_derecho(self, pro, marca, precio, cantidad, numero)


def envio_informacion_tabla_2_click_derecho(self, pro, marca, precio, cantidad, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))

    tabla_venta.insertRow(tabla_venta.rowCount())
    tabla_venta.setColumnCount(5)
    item = QTableWidgetItem()
    item.setText(str(pro))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 0, item)
    item = QTableWidgetItem()
    item.setText(str(precio))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 1, item)
    item = QTableWidgetItem()
    item.setText(str(marca))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 2, item)
    item = QTableWidgetItem()
    item.setText(str(cantidad))
    tabla_venta.setItem(tabla_venta.rowCount() - 1, 3, item)
    calcular_producto_total(self, numero)
    tabla_venta.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    tabla_venta.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    tabla_venta.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    tabla_venta.setEditTriggers(QTableWidget.NoEditTriggers)



def regreso_productos_click_derecho(self, fila, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))

    pro = tabla_venta.item(fila, 0).text()
    marca = tabla_venta.item(fila, 2).text()
    cant = int(tabla_venta.item(fila, 3).text())
    cantidad, ok = QInputDialog.getInt(self, 'Producto', 'Cantidad a devolver')
    if cantidad < cant:
        querys_db.devolver_producto_venta_click_derecho(pro, marca, cantidad)
        item = QTableWidgetItem()
        item.setText(str(cant - cantidad))
        tabla_venta.setItem(fila, 3, item)
        filtros_productos_existentes(self, numero)
    elif cantidad == cant:
        querys_db.devolver_producto_venta_click_derecho(pro, marca, cantidad)
        filtros_productos_existentes(self, numero)
        tabla_venta.removeRow(fila)
    else:
        QMessageBox.critical(self,'ALERTA','solo puedes devolver '+str(cant))
    calcular_producto_total(self, numero)


def regreso_productos(self, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    fila = tabla_venta.currentRow()
    pro = tabla_venta.item(fila, 0).text()
    marca = tabla_venta.item(fila, 2).text()
    cant = int(tabla_venta.item(fila, 3).text())
    if cant >1:
        querys_db.devolver_producto_venta(pro, marca)
        item = QTableWidgetItem()
        item.setText(str(cant - 1))
        tabla_venta.setItem(fila, 3, item)
    elif cant == 1:
        querys_db.devolver_producto_venta(pro, marca)
        tabla_venta.removeRow(fila)

    calcular_producto_total(self, numero)
    filtros_productos_existentes(self, numero)
    tabla_venta.clearSelection()

def cancelar_venta(self, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    if tabla_venta.rowCount() <= 0:
        eliminacion_widgets(self, numero)
        self.tabs.removeTab(self.tabs.currentIndex())
        self.ventas_permitidas -= 1

    else:
        filas = tabla_venta.rowCount()
        for i in range(filas):
            fila = []
            for j in range(5):
                valor = tabla_venta.item(i, j).text()
                fila.append(valor)
            querys_db.devolver_productos_cancelados_venta(fila)
        filtros_productos_existentes(self, numero)
        tabla_venta.setRowCount(0)
        label_suma = self.findChild(QLabel, 'label_3_{}'.format(numero))
        label_suma.setText('')


def eliminacion_widgets(self, numero):
    label_producto = self.findChild(QLabel, 'line_1_{}'.format(numero))
    producto = self.findChild(QLineEdit, 'line_{}'.format(numero))


    tabla_busqueda = self.findChild(QTableWidget, 'tabla_1_{}'.format(numero))
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))



    boton_cancelar = self.findChild(QPushButton, 'boton_1_{}'.format(numero))
    boton_aceptar = self.findChild(QPushButton, 'boton_2_{}'.format(numero))


    label_total = self.findChild(QLabel, 'label_2_{}'.format(numero))
    label_suma = self.findChild(QLabel, 'label_3_{}'.format(numero))

    label_producto.deleteLater()
    producto.deleteLater()
    tabla_busqueda.deleteLater()
    tabla_venta.deleteLater()
    boton_aceptar.deleteLater()
    boton_cancelar.deleteLater()
    label_total.deleteLater()
    label_suma.deleteLater()





def realizar_venta(self, numero, vendedor):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    if tabla_venta.rowCount() <= 0:
        pass
    else:
        ticket = querys_db.ultimo_folio()
        if ticket == None:
            ticket = 1
        else:
            ticket +=1
        querys_db.registrar_ticket(ticket, vendedor)
        registrar_productos_ticket(self, ticket, numero)


def registrar_productos_ticket(self, ticket, numero):
    tabla_venta = self.findChild(QTableWidget, 'tabla_2_{}'.format(numero))
    filas = tabla_venta.rowCount()
    for i in range(filas):
        fila = []
        for j in range(5):
            valor = tabla_venta.item(i, j).text()
            fila.append(valor)
        querys_db.ingreso_producto_ticket(fila, ticket)
    eliminacion_widgets(self, numero)
    self.tabs.removeTab(self.tabs.currentIndex())


