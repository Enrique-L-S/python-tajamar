import producto
from almacen import Almacen

class Pedido:
    def __init__(self, productos):
        self.productos = productos

    def procesar_pedido(self, almacen: Almacen):
        for producto in self.productos:
            producto.preparar(almacen)

# Ejemplo de uso

almacen = Almacen()
almacen.agregar_producto("Leche", 10)
almacen.agregar_producto("Café", 10)
almacen.agregar_producto("Pan", 10)
almacen.agregar_producto("Tomate", 10)
almacen.agregar_producto("Ron", 3)
almacen.agregar_producto("Lima", 3)
almacen.agregar_producto("Hielo", 100)
almacen.agregar_producto("Menta", 5)
almacen.agregar_producto("Salmón", 2)

# Ver los productos en el almacén
print(f"Productos en el almacén:")
almacen.mostrar_productos()

# Definir productos
cafe = producto.Desayuno("Café con leche", 2, {"Leche": 1, "Café": 1}, "☕")
tosta = producto.Desayuno("Tosta con tomate", 3, {"Pan": 1, "Tomate": 1}, "🍞")
coctel = producto.Coctel("Mojito", 5, {"Ron": 1, "Lima": 1, "Hielo": 1, "Menta": 1})
cafe_vegano = producto.Desayuno("Café con leche vegano", 3, {"Leche": 1, "Café": 1}, "☕")
tarta = producto.Postre("Tarta de queso", 10, {"Queso": 2, "Sirope": 1, "Azúcar": 2})

# Crear un pedido
pedido1 = Pedido([cafe, tosta])
pedido2 = Pedido([coctel])

# Procesar los pedidos
print("\nProcesando pedido 1:")
pedido1.procesar_pedido(almacen)

print("\nProcesando pedido 2:")
pedido2.procesar_pedido(almacen)

almacen.agregar_producto("Queso", 5)
almacen.agregar_producto("Sirope", 5)
almacen.agregar_producto("Azúcar", 100)

# Ver los productos en el almacén
print(f"Productos en el almacén:")
almacen.mostrar_productos()

print("\nProcesando pedido 3:")
pedido3 = Pedido([cafe_vegano])
pedido3.procesar_pedido(almacen)

print("\nProcesando pedido 3:")
pedido4 = Pedido([cafe, tarta])
pedido4.procesar_pedido(almacen)