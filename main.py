from products import agregar_producto, eliminar_producto, actualizar_producto, ver_inventario
from sales import registrar_venta
from db import create_db

def menu():
    create_db()  # Asegura que la base de datos y las tablas se creen al iniciar

    while True:
        print("\n---- Sistema de Gestión de Inventario ----")
        print("1. Ver Inventario")
        print("2. Agregar Producto")
        print("3. Eliminar Producto")
        print("4. Actualizar Producto")
        print("5. Registrar Venta")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            ver_inventario()
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            stock = int(input("Cantidad en stock: "))
            agregar_producto(nombre, categoria, precio, stock)
        elif opcion == '3':
            producto_id = int(input("ID del producto a eliminar: "))
            eliminar_producto(producto_id)
        elif opcion == '4':
            producto_id = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            categoria = input("Nueva categoría (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            stock = input("Nuevo stock (dejar vacío para no cambiar): ")

            precio = float(precio) if precio else None
            stock = int(stock) if stock else None
            
            actualizar_producto(producto_id, nombre or None, categoria or None, precio, stock)
        elif opcion == '5':
            producto_id = int(input("ID del producto a vender: "))
            cantidad_vendida = int(input("Cantidad vendida: "))
            registrar_venta(producto_id, cantidad_vendida)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Llamar al menú
menu()