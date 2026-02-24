import sqlite3

def registrar_venta(producto_id, cantidad_vendida):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    # Verificar stock antes de realizar la venta
    cursor.execute('SELECT stock FROM productos WHERE id = ?', (producto_id,))
    stock_actual = cursor.fetchone()

    if stock_actual and stock_actual[0] >= cantidad_vendida:
        # Actualizar el stock después de la venta
        nuevo_stock = stock_actual[0] - cantidad_vendida
        cursor.execute('UPDATE productos SET stock = ? WHERE id = ?', (nuevo_stock, producto_id))
        
        conn.commit()
        print(f"Venta registrada. {cantidad_vendida} productos vendidos.")
    else:
        print("No hay suficiente stock para realizar la venta.")
    
    conn.close()