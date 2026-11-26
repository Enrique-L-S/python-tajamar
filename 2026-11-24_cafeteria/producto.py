import abc
import time
from almacen import Almacen

class InterfazProducto(abc.ABC):
    def __init__(self, nombre: str, tiempo_preparacion: int, ingredientes: dict, icono=None):
        self.nombre = nombre
        self.tiempo_preparacion = tiempo_preparacion
        self.ingredientes = ingredientes
        self.icono = icono

    def buscar_ingredientes(self, almacen):
        print("Espera, que voy a mirar en el almacén")
        
        time.sleep(2)

        for ingrediente in self.ingredientes:
            if ingrediente not in almacen.productos or almacen.productos[ingrediente] <= 0:
                print(f"No hay suficiente {ingrediente} para preparar {self.nombre}.")
                return False

        return True

    @abc.abstractmethod
    def preparar(self, almacen):
        pass


class Coctel(InterfazProducto):
    def __init__(self, nombre: str, tiempo_preparacion: int, ingredientes: dict, icono="🍸"):
        super().__init__(nombre, tiempo_preparacion, ingredientes, icono)

    def preparar(self, almacen: Almacen):
        # Saber primero si hay ingredientes en el almacen
        if not self.buscar_ingredientes(almacen):
            return

        # Consumimos del almacen
        for ingrediente, cantidad in self.ingredientes.items():
            almacen.consumir_producto(ingrediente, cantidad)

        print(f"Mezclando {self.nombre}...")

        time.sleep(self.tiempo_preparacion)

        print(f"{self.nombre} listo!")
        print(f"{"_" * 100}{self.icono}" if self.icono else "")


class Desayuno(InterfazProducto):
    def __init__(self, nombre: str, tiempo_preparacion: int, ingredientes: dict, icono=None):
        super().__init__(nombre, tiempo_preparacion, ingredientes, icono)

    def preparar(self, almacen: Almacen):
        if "vegano" in self.nombre or "vegana" in self.nombre:
            q = self.ingredientes["Leche"]
            del self.ingredientes["Leche"]
            self.ingredientes["Leche de soja"] = q

        if not self.buscar_ingredientes(almacen):
            return

        # Consumimos del almacen
        for ingrediente, cantidad in self.ingredientes.items():
            almacen.consumir_producto(ingrediente, cantidad)

        print(f"Calentando {self.nombre}...")

        time.sleep(self.tiempo_preparacion)

        print(f"{self.nombre} listo!")
        print(f"{"_" * 100}{self.icono}" if self.icono else "")

class Postre(InterfazProducto):
    def __init__(self, nombre: str, tiempo_preparacion: int, ingredientes: dict, icono=None):
        super().__init__(nombre, tiempo_preparacion, ingredientes, icono)

    def preparar(self, almacen: Almacen):
        if not self.buscar_ingredientes(almacen):
            return

        # Consumimos del almacen
        for ingrediente, cantidad in self.ingredientes.items():
            almacen.consumir_producto(ingrediente, cantidad)

        print(f"Mezclando {self.nombre}...")

        time.sleep(self.tiempo_preparacion / 3)

        print(f"Metiendo en el horno el/la {self.nombre}...")

        time.sleep(self.tiempo_preparacion / 2)

        print(f"Dejando enfriar el/la {self.nombre}...")
        
        time.sleep(self.tiempo_preparacion / 6)

        print(f"{self.nombre} listo!")
        print(f"{"_" * 100}{self.icono}" if self.icono else "")
