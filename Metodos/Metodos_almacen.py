# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: metodos de la interfaz de almacen                               #
# Autor: Mauricio Roman Ruiz Bárcenas                                        #
# Fecha: 20/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtGui import QColor
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QTableWidget, QFileDialog
from fpdf import FPDF
from datetime import date, time

from DB import querys_db
from Interfaz import Limpieza_interfaz

def mostrar_ayuda(self):
    text = ('''    Todos los campos deben se completados 
    para ingresar la informacion

    Nombre = nombre con el que se guadara del producto
    Marca = marca del producto
    Cantidad = cantidad de producto comprado
    P/Compra = precio con la que fue comprado el producto
    P/Venta = precio que se dara a la venta publico
    C/Barras = codigo de baras del producto

    ''')

    QMessageBox.critical(self, 'Ayuda',text)


def export_to_pdf(self):
    datos_fila = []
    datos_final = []
    filas = self.ui.tableWidget.rowCount()
    if filas <= 0:
        QMessageBox.critical(self, 'ALERTA', 'No existen datos para exportar')
    else:
        for i in range(filas):
            for j in range(5):
                item = self.ui.tableWidget.item(i, j).text()
                datos_fila.append(item)
            datos_final.append(datos_fila)
            datos_fila = []
        exportar(self, datos_final)

def exportar(self, datos):
    pdf = PDF(orientation='P', format='A4', unit='cm')
    pdf.add_page()
    pdf.alias_nb_pages()

    pdf.set_title('Reporte de almacen')
    pdf.set_margins(3.0, 2.5, 3.0)
    pdf.set_font('Arial', '', 6.0)
    y = 3
    for i in range(len(datos)):
        for j in range(5):
            if j == 0:
                dato = str(datos[i][j])
                pdf.set_xy(3,y)
                pdf.cell(9, .5, dato,1,1,'L',False)
            if j == 1:
                pass
            if j == 2:
                dato = str(datos[i][j])
                pdf.set_xy(12, y)
                pdf.cell(1, .5, dato, 1, 1, 'C', False)
            if j == 3:
                dato = str(datos[i][j])
                pdf.set_xy(13, y)
                pdf.cell(3, .5, dato, 1, 1, 'C', False)
            if j == 4:
                dato = str(datos[i][j])
                pdf.set_xy(16, y)
                pdf.cell(2, .5, dato, 1, 1, 'C', False)
        y += .5
        if y >= 27:
            pdf.add_page()
            y = 3

    ruta, _ = QFileDialog.getSaveFileName(self, "Select output file ", "Reporte_ventas.pdf", '*.*')
    pdf.output(ruta, 'F')
    QMessageBox.critical(self, 'Aviso', 'Archivo exportado en '+ruta )


class PDF(FPDF):
    # Encabezado
    def header(self):
        fecha = date.today()
        self.set_text_color(158, 24, 6)
        self.set_font('Arial', 'B', 14.0)
        self.text(3, 1.5, 'REPORTE ALMACEN')

        self.set_font('Arial', 'B', 12.0)
        self.set_text_color(136, 138, 133)
        self.text(3, 2.2, str('fecha de guardado: ' + fecha.strftime('%d/%m/%y')))
        # self.image(os.getcwd() + '/Interfaz/punto-de-venta.png', 15.99, 1, 1.9, 1.4)

        self.set_font('Arial', '', 8)
        # self.set_font('Arial', 'B', 10)
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(64, 100, 133)
        self.set_text_color(255, 255, 255)

        self.set_xy(3, 2.5)
        self.cell(9, .5, 'Producto', 'LTB', 0, 'C', True)
        self.set_xy(12, 2.5)
        self.cell(1, .5, 'Cant', 'LTB', 0, 'C', True)
        self.set_xy(13, 2.5)
        self.cell(3, .5, 'Marca', 'LTB', 0, 'C', True)
        self.set_xy(16, 2.5)
        self.cell(2, .5, 'Codigo', 'RTBL', 0, 'C', True)

    # Pie de pagina
    def footer(self):
        self.set_xy(13, 22.8)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 8)
        self.text(15.8, 27.79, 'Pagina ' + str(self.page_no()) + '/{nb}')


def aplicar_modificacion_productos(self):
    pro = self.ui.lineEdit_9.text()
    marca = self.ui.lineEdit_11.text()
    cant = int(self.ui.lineEdit_10.text())
    precio = float(self.ui.lineEdit_12.text())
    codigo = self.ui.lineEdit_15.text()

    querys_db.actualizar_producto_existente_almacen(pro, marca, cant, precio, codigo, self.id)
    Limpieza_interfaz.limpieza_interfaz_pestaña_3_almacen(self)
    self.ui.tableWidget_3.setDisabled(False)
    self.ui.lineEdit_13.setDisabled(False)
    self.ui.lineEdit_13.setFocus()
    self.ui.tableWidget_3.clearSelection()
    filtro_productos_pest_3(self)

def cancelar_modificaciones_producto(self):
    self.id = None
    self.ui.tableWidget_3.setDisabled(False)
    self.ui.lineEdit_13.setDisabled(False)
    self.ui.lineEdit_9.setText('')
    self.ui.lineEdit_10.setText('')
    self.ui.lineEdit_11.setText('')
    self.ui.lineEdit_12.setText('')
    Limpieza_interfaz.bloqueo_elementos_modificaciom(self)
    self.ui.lineEdit_13.setFocus()
    self.ui.tableWidget_3.clearSelection()

def filtro_productos_pest_3(self):
    pro = self.ui.lineEdit_13.text()
    if pro == '':
        busqueda_total_productos_modificacion(self)
    else:
        info = querys_db.buscar_por_nombre_pest_3(pro)
        if len(info) == 0:
            self.ui.tableWidget_3.setRowCount(0)
        else:
            envio_informacion_tabla_modificacion(self, info)

def mandar_info_modificar_producto(self):
    datos = []
    fila = self.ui.tableWidget_3.currentRow()
    for i in range(5):
        valor = self.ui.tableWidget_3.item(fila, i).text()
        datos.append(valor)
    self.id = querys_db.busqueda_id_producto(datos)
    Limpieza_interfaz.desbloqueo_elementos_modificaciom(self)
    self.ui.lineEdit_9.setText(datos[0])
    self.ui.lineEdit_11.setText(datos[3])
    self.ui.lineEdit_10.setText(datos[2])
    self.ui.lineEdit_12.setText(datos[1])
    self.ui.lineEdit_15.setText(datos[4])
    self.ui.tableWidget_3.setDisabled(True)
    self.ui.lineEdit_13.setDisabled(True)

def colorear_productos_compras(self):
    filas = self.ui.tableWidget.rowCount()
    if filas <= 0:
        pass
    else:
        for i in range(filas):
            cant = int(self.ui.tableWidget.item(i, 2).text())
            if cant <= 5:
                for j in range(5):
                    self.ui.tableWidget.item(i, j).setBackground(QColor(219, 88, 96))
            elif cant <= 20 and cant >=5 :
                for j in range(5):
                    self.ui.tableWidget.item(i, j).setBackground(QColor(237, 212, 0))
            elif cant > 20:
                for j in range(5):
                    self.ui.tableWidget.item(i, j).setBackground(QColor(133,183,88))

def cambio_status_producto_almacen_baja(self, pro, marca):
    try :
        if self.tabs.count() >= 1:
            QMessageBox.critical(self,'Alerta', 'Existen ventas en proceso')
        else:
            resultado = querys_db.busqueda_status_producto(pro, marca)
            if resultado.status == 'baja':
                pass
            elif resultado.status == 'alta':
                querys_db.cambio_status_producto_almacen_baja(pro, marca)
    except AttributeError:
        resultado = querys_db.busqueda_status_producto(pro, marca)
        if resultado.status == 'baja':
            pass
        elif resultado.status == 'alta':
            querys_db.cambio_status_producto_almacen_baja(pro, marca)



def cambio_status_producto_almacen_menu_alta(self, pro, marca):
    try:
        if self.tabs.count() >= 1 :
            QMessageBox.critical(self, 'Alerta', 'Existen ventas en proceso')
        else:
            resultado = querys_db.busqueda_status_producto(pro, marca)
            if resultado.status == 'alta':
                pass
            elif resultado.status == 'baja':
                querys_db.cambio_status_producto_almacen_alta(pro, marca)
    except AttributeError:
        resultado = querys_db.busqueda_status_producto(pro, marca)
        if resultado.status == 'alta':
            pass
        elif resultado.status == 'baja':
            querys_db.cambio_status_producto_almacen_alta(pro, marca)



def filtro_nombre_producto_alta_baja(self):
    texto = self.ui.lineEdit_5.text()
    if texto == '':
        busqueda_total_productos_alta_baja(self)
    else:
        resultado = querys_db.busqueda_productos_nombre_alta_baja(texto)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setColumnCount(5)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
        self.ui.tableWidget_2.setRowCount(len(resultado))
        envio_informacion_tabla_almacen_alta_baja(self, resultado)

def colorear_productos(self):
    filas = self.ui.tableWidget_2.rowCount()
    if filas <= 0:
        pass
    else:
        for i in range(filas):
            pro = self.ui.tableWidget_2.item(i, 0).text()
            marca = self.ui.tableWidget_2.item(i, 3).text()
            resultado = querys_db.busqueda_status_producto(pro, marca)
            if resultado.status == 'alta':
                for j in range(5):
                    self.ui.tableWidget_2.item(i,j).setBackground(QColor(133,183,88))
            else:
                for j in range(5):
                    self.ui.tableWidget_2.item(i, j).setBackground(QColor(219, 88, 96))

def filtro_nombre_producto(self):
    texto = self.ui.lineEdit.text()
    if texto == '':
        resultado = querys_db.productos_existentes()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
        self.ui.tableWidget.setRowCount(len(resultado))
        envio_informacion_tabla_almacen(self, resultado)
    else:
        # Limpieza_interfaz.limpieza_compras_almacen(self)
        resultado = querys_db.buscar_por_nombre(texto)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
        self.ui.tableWidget.setRowCount(len(resultado))
        envio_informacion_tabla_almacen(self, resultado)

def envio_informacion_tabla_almacen(self, resultado):
    for i in range(len(resultado)):
        item = QTableWidgetItem()
        item.setText(str(resultado[i].producto))
        self.ui.tableWidget.setItem(i, 0, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].precio_venta))
        self.ui.tableWidget.setItem(i, 1, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].cantidad_existente))
        self.ui.tableWidget.setItem(i, 2, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].marca))
        self.ui.tableWidget.setItem(i, 3, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].codigo))
        self.ui.tableWidget.setItem(i, 4, item)
    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
    self.ui.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
    self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
    colorear_productos_compras(self)

def envio_informacion_tabla_almacen_alta_baja(self, resultado):
    for i in range(len(resultado)):
        item = QTableWidgetItem()
        item.setText(str(resultado[i].producto))
        self.ui.tableWidget_2.setItem(i, 0, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].precio_venta))
        self.ui.tableWidget_2.setItem(i, 1, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].cantidad_existente))
        self.ui.tableWidget_2.setItem(i, 2, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].marca))
        self.ui.tableWidget_2.setItem(i, 3, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].codigo))
        self.ui.tableWidget_2.setItem(i, 4, item)
    self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
    self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
    self.ui.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)
    colorear_productos(self)


def ingreso_compra_nueva(self):
    pro = self.ui.lineEdit.text()
    marca = self.ui.lineEdit_3.text()
    cantidad = self.ui.lineEdit_4.text()
    codigo = str(self.ui.lineEdit_14.text())
    precio_compra = self.ui.lineEdit_2.text()
    precio_venta = self.ui.lineEdit_16.text()
    if pro == '' or marca == '' or cantidad == '' or precio_compra == '' or  codigo == '':
        QMessageBox.critical(self,'ALERTA','Informacion incompleta')

        for i in range(8):
            if i % 2 == 0:
                self.ui.pushButton_11.setStyleSheet('background-color: rgb(204, 0, 0);')
            else:
                self.ui.pushButton_11.setStyleSheet('background-color: rgb(237, 212, 0);')
            loop = QEventLoop()
            QTimer.singleShot(50, loop.quit)
            loop.exec_()
        self.ui.pushButton_11.setStyleSheet("QPushButton {background-color: transparent; border: 2px solid black; "
                                            "border-radius: 29.4px} QPushButton:pressed " "{background-color: yellow;}")

    else:
        querys_db.actualizar_almacen_compra(pro, marca, int(cantidad), precio_compra, codigo, precio_venta)

        querys_db.ingreso_nueva_compra(pro, marca, cantidad, precio_compra)

        Limpieza_interfaz.limpieza_compras_almacen(self)
        busqueda_total_productos(self)
        self.ui.pushButton_2.setDefault(False)
        self.ui.lineEdit.setFocus()

def cancelar_ingreso_compra(self):
    Limpieza_interfaz.limpieza_compras_almacen(self)
    busqueda_total_productos(self)
    self.ui.lineEdit.setFocus()

def cambio_pestaña_almacen(self):
    if self.ui.tabWidget.currentIndex() == 0:
        Limpieza_interfaz.limpieza_compras_almacen(self)
        self.ui.lineEdit.setFocus()
        self.ui.pushButton_2.setDefault(False)
        busqueda_total_productos(self)
    elif self.ui.tabWidget.currentIndex() == 1:
        Limpieza_interfaz.limpieza_pestaña_2_almacen(self)
        self.ui.lineEdit_5.setFocus()
        busqueda_total_productos_alta_baja(self)
    elif self.ui.tabWidget.currentIndex() == 2:
        Limpieza_interfaz.limpieza_interfaz_pestaña_3_almacen(self)
        busqueda_total_productos_modificacion(self)

def busqueda_total_productos_modificacion(self):
    resultado = querys_db.productos_existentes()
    if len(resultado) == 0:
        pass
    else:
        envio_informacion_tabla_modificacion(self, resultado)

def envio_informacion_tabla_modificacion(self, resultado):
    self.ui.tableWidget_3.setColumnCount(5)
    self.ui.tableWidget_3.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
    self.ui.tableWidget_3.setRowCount(len(resultado))
    for i in range(len(resultado)):
        item = QTableWidgetItem()
        item.setText(str(resultado[i].producto))
        self.ui.tableWidget_3.setItem(i, 0, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].precio_venta))
        self.ui.tableWidget_3.setItem(i, 1, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].cantidad_existente))
        self.ui.tableWidget_3.setItem(i, 2, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].marca))
        self.ui.tableWidget_3.setItem(i, 3, item)
        item = QTableWidgetItem()
        item.setText(str(resultado[i].codigo))
        self.ui.tableWidget_3.setItem(i, 4, item)
    self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
    self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
    self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)

def busqueda_total_productos_alta_baja(self):
    resultado =querys_db.busqueda_total_productos_alta_baja()
    if len(resultado) == 0:
        pass
    else:
        Limpieza_interfaz.limpieza_pestaña_2_almacen(self)
        self.ui.tableWidget_2.setColumnCount(5)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
        self.ui.tableWidget_2.setRowCount(len(resultado))
        envio_informacion_tabla_almacen_alta_baja(self, resultado)

def busqueda_total_productos(self):
    resultado = querys_db.productos_existentes()
    if len(resultado) == 0:
        pass
    else:
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Producto', 'Precio', 'Cantidad', 'marca', 'Codigo'])
        self.ui.tableWidget.setRowCount(len(resultado))
        envio_informacion_tabla_almacen(self, resultado)

def mostrar_pantalla(self):
    if self.ui.stackedWidget.currentIndex() == 2:
        pass
    else:
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.tabWidget.setCurrentIndex(0)
        Limpieza_interfaz.limpieza_compras_almacen(self)
        self.ui.lineEdit.setFocus()
        self.ui.pushButton_2.setDefault(False)
        busqueda_total_productos(self)

def interfaz_usuarios(self):
    if self.ui.stackedWidget.currentIndex() == 3:
        pass
    else:
        self.ui.stackedWidget.setCurrentIndex(3)
