from db import db
from products import Producto


def registrar_venta(producto_id, cantidad_vendida):
    producto = Producto.query.get(producto_id)

    if not producto:
        return False

    if producto.stock >= cantidad_vendida:
        producto.stock -= cantidad_vendida
        db.session.commit()
        return True

    return False