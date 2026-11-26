import abc
import time

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