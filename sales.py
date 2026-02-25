from db import db
from datetime import datetime
from products import Producto

class Venta(db.Model):
    __tablename__ = "ventas"

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad_vendida = db.Column(db.Integer, nullable=False)
    fecha_venta = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)

    producto = db.relationship('Producto', backref=db.backref('ventas', lazy=True))
    
    def __init__(self, producto_id, cantidad_vendida):
        self.producto_id = producto_id
        self.cantidad_vendida = cantidad_vendida
        self.total = self.calcular_total()
    
    def calcular_total(self):
        producto = Producto.query.get(self.producto_id)
        if producto:
            return producto.precio * self.cantidad_vendida
        return 0.0
    
    def to_dict(self):
        return {
            "id": self.id,
            "producto_id": self.producto_id,
            "cantidad_vendida": self.cantidad_vendida,
            "fecha_venta": self.fecha_venta,
            "total": self.total
        }
