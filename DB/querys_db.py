# -*- coding: utf-8 -*-
##############################################################################
# Programa: PDV                                                              #
# Proposito: conexion con la BD                                              #
# Autor: Mauricio Roman Ruiz Bárcenas                                        #
# Fecha: 15/07/2020                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
# Nota: Si utilizas este codigo o lo modificas solo has referencia           #
#       de donde lo tomaste gracias.                                         #
##############################################################################

from DB import PDV_DB as tabla
from datetime import date
# from pony.orm.dbproviders.sqlite

from pony.orm import *

@db_session
def obtener_nombre_productos_ventas(id):
    nombre = tabla.Almacen.get(id = id)
    return nombre.producto

@db_session
def busqueda_productos_ticket(ticket):
    pro = select(c for c in tabla.Ventas if int(c.ticket) == ticket)[:]
    return pro

@db_session
def busquedas_ventas_diarias(fecha):
    bus = select(c for c  in tabla.Ticket if c.fecha == fecha )[:]
    return bus

@db_session
def actualizar_producto_existente_almacen(pro, marca, cant, precio, codigo, id):
    pro_exis = tabla.Almacen.get(id = id)
    pro_exis.producto = pro
    pro_exis.precio = precio
    pro_exis.cantidad_existente = cant
    pro_exis.marca = marca
    pro_exis.codigo = codigo

@db_session
def busqueda_id_producto(datos):
    producto = tabla.Almacen.get(producto = datos[0], marca = datos[3])
    return producto.id

@db_session
def devolver_producto_venta_click_derecho(pro, marca, cantidad):
    producto = tabla.Almacen.get(producto=pro, marca=marca)
    producto.cantidad_existente += cantidad

@db_session
def devolver_producto_venta(pro, marca):
    producto = tabla.Almacen.get(producto=pro, marca=marca)
    producto.cantidad_existente += 1

@db_session
def restar_producto_venta_click_derecho(pro, marca, cantidad):
    producto = tabla.Almacen.get(producto = pro, marca = marca)
    producto.cantidad_existente -= cantidad
    # commit()

@db_session
def devolver_productos_cancelados_venta(fila):
    producto = select(c for c in tabla.Almacen if c.producto == fila[0] and c.marca == fila[2])[:]
    producto[0].cantidad_existente += int(fila[3])

@db_session
def ingreso_producto_ticket(fila, ticket):
    producto = select(c for c in tabla.Almacen if c.producto == fila[0] and c.marca == fila[2])[:]
    tabla.Ventas(producto = producto[0].id,
                 precio_venta = float(producto[0].precio_venta),
                 cantidad = int(fila[3]),
                 monto = float(fila[4]),
                 ticket = int(ticket),
                 marca = fila[2])
    commit()

@db_session
def registrar_ticket(ticket, vendedor):
    tabla.Ticket(ticket = ticket,
                 vendedor = vendedor)
    commit()

@db_session
def ultimo_folio():
    ticket = max(c.ticket for c in tabla.Ticket)
    return ticket

@db_session
def restar_producto_venta(pro, marca):
    producto = tabla.Almacen.get(producto = pro, marca = marca)
    producto.cantidad_existente -= 1
    commit()

@db_session
def filtro_busqueda_venta(pro):
    resultado = select(c for c in tabla.Almacen if (pro in c.producto or pro in c.codigo) and c.status == 'alta')[:]
    return resultado

@db_session
def cambio_status_producto_almacen_baja(pro, marca):
    p = tabla.Almacen.get(producto = pro, marca = marca)
    p.set(status = 'baja')

@db_session
def cambio_status_producto_almacen_alta(pro, marca):
    p = tabla.Almacen.get(producto = pro, marca = marca)
    p.set(status = 'alta')

@db_session
def busqueda_status_producto(pro, marca):
    resultado = tabla.Almacen.get(producto = pro, marca = marca)
    return resultado

@db_session
def busqueda_productos_nombre_alta_baja(texto):
    resultado = select(c for c in tabla.Almacen if (texto in c.producto or texto in c.codigo))[:]
    return resultado

@db_session
def busqueda_total_productos_alta_baja():
    resultado = select(c for c in tabla.Almacen)[:]
    return resultado

@db_session
def buscar_por_nombre_pest_3(dato):
    busqueda = select(c for c in tabla.Almacen if (dato in c.producto or dato in c.codigo )and c.status == 'alta')[:]
    return busqueda

@db_session
def buscar_por_nombre(dato):
    busqueda = select(c for c in tabla.Almacen if (dato in c.producto or dato in c.codigo) )[:]
    return busqueda

@db_session
def actualizar_almacen_compra(pro, marca, cantidad, precio_compra, codigo, precio_venta):
    # producto_almacen = tabla.Almacen.get(producto = pro)
    producto_almacen = select(c for c in tabla.Almacen if c.producto == pro and c.marca == marca)[:]
    if len(producto_almacen) == 0:
        # ingreso producto nuevo
        tabla.Almacen(producto = pro,
                      precio_venta = precio_compra,
                      cantidad_existente = cantidad,
                      marca = marca,
                      status = 'alta',
                      codigo = codigo)
        commit()
    else:
        producto_almacen[0].cantidad_existente += cantidad
        producto_almacen[0].precio_venta = precio_venta

@db_session
def ingreso_nueva_compra(pro, marca, cantidad, precio_compra):
    id_pro = select(c for c in tabla.Almacen if c.producto == pro and c.marca == marca)[:]
    tabla.Compras(producto = id_pro[0].id,
                  marca = marca,
                  cantidad = cantidad,
                  precio_compra = precio_compra)
    commit()

@db_session
def productos_existentes():
    pro = select(c for c in tabla.Almacen if c.status == 'alta')[:]
    return pro

@db_session
def status_usuario(nombre):
    usuario = tabla.Usuarios.get(nombre = nombre)
    return usuario

@db_session
def modificar_usuario(nombre, password, permisos):
    usuario = tabla.Usuarios.get(nombre = nombre)
    usuario.set(password = password,
                permisos = permisos)

@db_session
def busqueda_usuarios_activos():
    resultado = select(c for c in tabla.Usuarios if c.status == 'alta')[:]
    return resultado

@db_session
def baja_usuarios(nombre, status):
    usuario = tabla.Usuarios.get(nombre = nombre)
    usuario.set(status = status)

@db_session
def busqueda_usuarios_baja_alta():
    busqueda = select(c for c in tabla.Usuarios )[:]
    return busqueda


@db_session
def busqueda_usuarios(nombre):
    # inicio
    resultado = select(c for c in tabla.Usuarios if  c.nombre == nombre and  c.status == 'alta' )[:]
    return resultado


@db_session
def ingreso_nuevo(nombre, password, permisos):
    print(nombre, password, permisos)
    tabla.Usuarios(nombre = nombre,
                   password = password,
                   permisos = permisos,
                   status = 'alta')
    commit()
