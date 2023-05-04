# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: Manejador bd                                                    #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 07/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################
# from datetime import date
from datetime import date
from decimal import Decimal
from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='PDV_DB', create_db=True)

class Usuarios(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str, unique= True)
    password =  Required(str)
    permisos = Required(int)
    status = Required(str)
    fecha = Required(date, default = lambda : date.today())

class Almacen(db.Entity):
    id = PrimaryKey(int, auto= True)
    producto = Required(str)
    precio_venta = Required(Decimal)
    cantidad_existente = Required(int)
    marca = Required(str)
    status = Required(str)
    codigo = Required(str)
    fecha = Required(date, default = lambda : date.today())
    ventas = Set('Ventas')
    compras = Set('Compras')

class Ticket(db.Entity):
    id = PrimaryKey(int, auto=True)
    ticket = Required(int, unique=True)
    fecha = Required(date, default=lambda: date.today())
    vendedor = Required(str)
    folio = Set('Ventas')

class Ventas(db.Entity):
    id = PrimaryKey(int, auto=True)
    producto = Required(Almacen)
    precio_venta = Required(Decimal)
    cantidad = Required(int)
    monto = Optional(Decimal)
    fecha = Required(date, default = lambda : date.today())
    ticket = Required(Ticket)
    marca = Required(str)


class Compras(db.Entity):
    id = PrimaryKey(int, auto=True)
    producto = Required(Almacen)
    marca = Required(str)
    cantidad = Required(int)
    precio_compra = Required(Decimal)
    fecha = Required(date, default = lambda : date.today())

db.generate_mapping(create_tables=True)