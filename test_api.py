import pytest
from app import app
import base64


# Crear header de autenticación básica
def get_auth_headers():
    credentials = base64.b64encode(b"admin:admin123").decode("utf-8")
    return {
        "Authorization": f"Basic {credentials}"
    }


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Prueba para obtener todos los productos
def test_obtener_productos(client):
    response = client.get('/productos')
    assert response.status_code == 200
    assert isinstance(response.json, list)


# Prueba para agregar un producto
def test_agregar_producto(client):
    producto = {
        "nombre": "Producto de Prueba",
        "categoria": "Categoria Test",
        "precio": 10.0,
        "stock": 50
    }

    response = client.post(
        '/productos',
        json=producto,
        headers=get_auth_headers()
    )

    assert response.status_code == 201
    assert response.json['mensaje'] == 'Producto agregado exitosamente'


# Prueba para registrar una venta
def test_registrar_venta(client):
    venta = {
        "producto_id": 1,
        "cantidad_vendida": 5
    }

    response = client.post(
        '/ventas',
        json=venta,
        headers=get_auth_headers()
    )

    assert response.status_code == 200
    assert response.json['mensaje'] == 'Venta registrada exitosamente'