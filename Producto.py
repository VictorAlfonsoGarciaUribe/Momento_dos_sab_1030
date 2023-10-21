class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def registrar_producto(self):
        if self.margen_de_venta <= 0:
            raise ValueError("El margen de venta debe ser mayor que cero")
        
        self.precio_de_venta = self.costo / (1 - self.margen_de_venta)
        producto_info = {
            "ID": self.id,
            "Nombre": self.nombre,
            "Descripción": self.descripcion,
            "Costo": self.costo,
            "Cantidad": self.cantidad,
            "Precio de Venta": self.precio_de_venta
        }
        productos[self.id] = producto_info

def imprimir_productos():
    for producto_id, producto_info in productos.items():
        print(f"Producto {producto_id}:")
        for key, value in producto_info.items():
            print(f"{key}: {value}")
        print("\n")

# Diccionario para almacenar los productos
productos = {}

# Función para agregar un producto
def agregar_producto():
    while True:
        try:
            id = int(input("Ingrese el ID del producto (o 0 para salir): "))
            if id == 0:
                return
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            costo = float(input("Ingrese el costo del producto: "))
            cantidad = int(input("Ingrese la cantidad de productos: "))
            margen_de_venta = float(input("Ingrese el margen de venta (como decimal, ej. 0.1 para 10%): "))
            
            producto = Producto(id, nombre, descripcion, costo, cantidad, margen_de_venta)
            producto.registrar_producto()
        except ValueError:
            print("Por favor, ingrese valores válidos.")

# Menú 
while True:
    print("Victor Alfonso Garcia Uribe sabados 10:30")
    print("Menú:")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        imprimir_productos()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
