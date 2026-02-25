from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from db import db, init_db
from products import agregar_producto, eliminar_producto, actualizar_producto, ver_inventario
from sales import registrar_venta

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuración base de datos (MySQL con SQLAlchemy)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
init_db(app)

# Usuarios de ejemplo para autenticación básica
usuarios = {
    "admin": "admin123",
    "user": "user123"
}

@auth.verify_password
def verificar_usuario(usuario, contrasena):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        return usuario
    return None


# ------------------- ENDPOINTS -------------------

@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = ver_inventario()
    return jsonify(productos)


@app.route('/productos', methods=['POST'])
@auth.login_required
def crear_producto():
    data = request.get_json()

    nombre = data.get('nombre')
    categoria = data.get('categoria')
    precio = data.get('precio')
    stock = data.get('stock')

    if nombre and categoria and precio is not None and stock is not None:
        agregar_producto(nombre, categoria, precio, stock)
        return jsonify({"mensaje": "Producto agregado exitosamente"}), 201

    return jsonify({"error": "Faltan datos necesarios"}), 400


@app.route('/productos/<int:id>', methods=['PUT'])
@auth.login_required
def actualizar_producto_endpoint(id):
    data = request.get_json()

    actualizar_producto(
        id,
        data.get('nombre'),
        data.get('categoria'),
        data.get('precio'),
        data.get('stock')
    )

    return jsonify({"mensaje": "Producto actualizado exitosamente"})


@app.route('/productos/<int:id>', methods=['DELETE'])
@auth.login_required
def eliminar_producto_endpoint(id):
    eliminar_producto(id)
    return jsonify({"mensaje": "Producto eliminado exitosamente"})


@app.route('/ventas', methods=['POST'])
@auth.login_required
def registrar_venta_endpoint():
    data = request.get_json()

    producto_id = data.get('producto_id')
    cantidad_vendida = data.get('cantidad_vendida')

    if producto_id and cantidad_vendida:
        registrar_venta(producto_id, cantidad_vendida)
        return jsonify({"mensaje": "Venta registrada exitosamente"})

    return jsonify({"error": "Faltan datos necesarios"}), 400


if __name__ == '__main__':
    app.run(debug=True)