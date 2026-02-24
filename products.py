import sqlite3

def agregar_producto(nombre, categoria, precio, stock):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO productos (nombre, categoria, precio, stock)
    VALUES (?, ?, ?, ?)
    ''', (nombre, categoria, precio, stock))
    
    conn.commit()
    conn.close()

def eliminar_producto(producto_id):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM productos WHERE id = ?', (producto_id,))
    
    conn.commit()
    conn.close()

def actualizar_producto(producto_id, nombre=None, categoria=None, precio=None, stock=None):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    if nombre:
        cursor.execute('UPDATE productos SET nombre = ? WHERE id = ?', (nombre, producto_id))
    if categoria:
        cursor.execute('UPDATE productos SET categoria = ? WHERE id = ?', (categoria, producto_id))
    if precio:
        cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (precio, producto_id))
    if stock is not None:
        cursor.execute('UPDATE productos SET stock = ? WHERE id = ?', (stock, producto_id))
    
    conn.commit()
    conn.close()

def ver_inventario():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    if productos:
        print("ID | Nombre | Categoría | Precio | Stock")
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]}")
    else:
        print("No hay productos en el inventario.")

    conn.close()