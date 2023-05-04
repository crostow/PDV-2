# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: metodos de la interfaz de reportes                              #
# Autor: Mauricio Roman Ruiz Bárcenas                                        #
# Fecha: 24/03/2021                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget, \
    QMessageBox, QFileDialog, QDialog, QTextEdit
from fpdf import FPDF
from Interfaz import Limpieza_interfaz
from DB import querys_db
from datetime import date, datetime
import os
import sys
import getpass

def busqueda_ventas_fecha_especifica(self):
    fecha = self.ui.dateEdit.text()
    formato = '%d/%m/%y'
    datetime_object = datetime.strptime(fecha, formato)
    date_object = datetime_object.date()
    datos = querys_db.busquedas_ventas_diarias(date_object)
    if len(datos) == 0:
        QMessageBox.critical(self, 'Alerta', 'No existen ventas en esa fecha')
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.label_20.setText('')
        self.ui.label_22.setText('')
    else:
        mandar_info_tabla_reportes(self, datos)

def busqueda_ventas_hoy(self):
    fecha = date.today()
    datos = querys_db.busquedas_ventas_diarias(fecha)
    if len(datos) == 0:
        QMessageBox.critical(self, 'Alerta', 'No se han realizado ventas hoy')
        self.ui.label_20.setText('')
        self.ui.label_22.setText('')
        self.ui.tableWidget_4.setRowCount(0)
    else:
        mandar_info_tabla_reportes(self,datos)

def mandar_info_tabla_reportes(self, datos):
    print(datos)
    Limpieza_interfaz.limpieza_pest_4(self)
    info_linea = []
    self.ui.label_20.setText(str(len(datos)))
    for i in range(len(datos)):
        productos = querys_db.busqueda_productos_ticket(datos[i].ticket)
        info_linea.append((datos[i].ticket))
        for j in range(len(productos)):
            nom = querys_db.obtener_nombre_productos_ventas(productos[j].id)
            info_linea.append(nom)
            info_linea.append(productos[j].cantidad)
            info_linea.append(productos[j].monto)
            self.ui.tableWidget_4.insertRow(self.ui.tableWidget_4.rowCount())
            item = QTableWidgetItem()
            item.setText(str(info_linea[0]))
            self.ui.tableWidget_4.setItem(self.ui.tableWidget_4.rowCount() -1, 0, item)
            item = QTableWidgetItem()
            item.setText(str(info_linea[1]))
            self.ui.tableWidget_4.setItem(self.ui.tableWidget_4.rowCount() - 1, 1, item)
            item = QTableWidgetItem()
            item.setText(str(info_linea[2]))
            self.ui.tableWidget_4.setItem(self.ui.tableWidget_4.rowCount() - 1, 2, item)
            item = QTableWidgetItem()
            item.setText(str(info_linea[3]))
            self.ui.tableWidget_4.setItem(self.ui.tableWidget_4.rowCount() - 1, 3, item)
            info_linea.pop()
            info_linea.pop()
            info_linea.pop()
        info_linea = []
    self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
    self.ui.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)
    calculo_total_ingreso(self)

def calculo_total_ingreso(self):
    suma = 0
    filas = self.ui.tableWidget_4.rowCount()
    for i in range(filas):
        numero = float(self.ui.tableWidget_4.item(i, 3).text())
        suma += numero
    self.ui.label_22.setText(str(suma))

def cambio_pest_reportes(self):
    if self.ui.stackedWidget.currentIndex() == 4:
        pass
    else:
        self.ui.stackedWidget.setCurrentIndex(4)
        Limpieza_interfaz.limpieza_pest_4(self)
        fecha = date.today()
        self.ui.dateEdit.setDate(fecha)


def exportar_pdf(self):
    filas = self.ui.tableWidget_4.rowCount()
    total = self.ui.label_22.text()
    if filas == 0:
        QMessageBox.critical(self, 'Alerta', 'No hay informacion para exportar')
    else:
        info_fila = []
        info_tabla = []
        for i in range(filas):
            for j in range(4):
                item = self.ui.tableWidget_4.item(i, j).text()
                info_fila.append(item)
            info_tabla.append(info_fila)
            info_fila = []
        creacion_pdf(self, info_tabla, total)

def creacion_pdf(self, info,total):
    pdf = PDF(orientation='P', format='A4', unit='cm')
    pdf.add_page()
    pdf.alias_nb_pages()

    pdf.set_title('Reporte de ventas')
    pdf.set_margins(3.0, 2.5, 3.0)

    # pdf.set_line_width(0.0)
    # pdf.rect(3, 2.5, 14.99, 24.69)
    # x = 3.0
    y = 3
    for i in range(len(info)):
        for j in range(4):
            if j == 0:
                dato = str(info[i][j])
                pdf.set_xy(3,y)
                pdf.cell(1.5, .5, dato, 1, 1, 'C', False)
            elif j == 1:
                dato = str(info[i][j])
                pdf.set_xy(4.5, y)
                pdf.cell(10, .5, dato, 1, 1, 'C', False)
            elif j == 2:
                dato = str(info[i][j])
                pdf.set_xy(14.5, y)
                pdf.cell(2, .5, dato, 1, 1, 'C', False)
            elif j == 3:
                dato = str(info[i][j])
                pdf.set_xy(16.5, y)
                pdf.cell(1.5, .5, dato, 1, 1, 'C', False)
        y += .5
        if y >= 27:
            pdf.add_page()
            y = 3

    pdf.set_xy(14.5, y)
    pdf.cell(3.5, .5, 'TOTAL:            '+ str(total), 1, 1, 'C', False)


    ruta, _ = QFileDialog.getSaveFileName(self, "Select output file ", "Reporte_ventas.pdf", '*.*')
    pdf.output(ruta, 'F')
    QMessageBox.critical(self, 'Aviso', 'Archivo exportado en '+ruta )


class PDF(FPDF):
    # Encabezado
    def header(self):
        fecha = date.today()
        self.set_text_color(158, 24, 6)
        self.set_font('Arial', 'B', 14.0)
        self.text(3, 1.5, 'REPORTE PUNTO DE VENTA')

        self.set_font('Arial', 'B', 12.0)
        self.set_text_color(136,138,133 )
        self.text(3, 2.2, str('fecha de guardado: '+fecha.strftime('%d/%m/%y')))
        self.image(os.getcwd()+'/Interfaz/punto-de-venta.png', 15.99, 1, 1.9, 1.4)

        self.set_font('Arial','',8)
        # self.set_font('Arial', 'B', 10)
        self.set_draw_color(0,0,0)
        self.set_fill_color(64,100,133)
        self.set_text_color(255,255,255)

        self.set_xy(3,2.5)
        self.cell(1.5, .5, '# ticket', 'LTB', 0, 'C', True)
        # self.cell(5,5,'# ticket','LTRB',0,'C',True)

        self.set_xy(4.5,2.5)
        self.cell(10, .5, 'Productos', 'LTB', 0, 'C', True)
        # self.multi_cell(8, .5, 'Productos', 1, 'C', True)

        self.set_xy(14.5,2.5)
        self.cell(2, .5, 'Cantidad', 'LTB', 0, 'C', True)

        self.set_xy(16.5,2.5)
        self.cell(1.5, .5, 'Precio', 'RTBL', 0, 'C', True)

        # self.set_xy(15.8,2.5)
        # self.cell(2.2, .5, 'Importe', 'TPR', 0, 'C', True)

    # Pie de pagina
    def footer(self):
        self.set_xy(13, 22.8)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 8)
        self.text(15.8, 27.79,'Pagina '+str(self.page_no()) + '/{nb}')






