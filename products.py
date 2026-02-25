from db import db


class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


def agregar_producto(nombre, categoria, precio, stock):
    nuevo_producto = Producto(
        nombre=nombre,
        categoria=categoria,
        precio=precio,
        stock=stock
    )
    db.session.add(nuevo_producto)
    db.session.commit()


def eliminar_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if producto:
        db.session.delete(producto)
        db.session.commit()


def actualizar_producto(producto_id, nombre=None, categoria=None, precio=None, stock=None):
    producto = Producto.query.get(producto_id)

    if not producto:
        return

    if nombre:
        producto.nombre = nombre
    if categoria:
        producto.categoria = categoria
    if precio is not None:
        producto.precio = precio
    if stock is not None:
        producto.stock = stock

    db.session.commit()


def ver_inventario():
    productos = Producto.query.all()

    inventario = []
    for producto in productos:
        inventario.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "stock": producto.stock
        })

    return inventario