class Almacen:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad

    def consumir_producto(self, nombre, cantidad):
        if nombre in self.productos:
            if self.productos[nombre] >= cantidad:
                self.productos[nombre] -= cantidad
                if self.productos[nombre] == 0:
                    del self.productos[nombre]
            else:
                print(f"No hay suficiente {nombre} en el almacén.")
        else:
            print(f"{nombre} no se encuentra en el almacén.")

    def mostrar_productos(self):
        for nombre, cantidad in self.productos.items():
            print(f"{nombre}: {cantidad}")