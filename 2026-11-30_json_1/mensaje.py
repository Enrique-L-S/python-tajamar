import abc
import json

class Mensaje(abc.ABC):
    def __init__(self, tipo: str, cuerpo):
        self.tipo = tipo
        self.cuerpo = cuerpo

    @abc.abstractmethod
    def importar_fichero(self):
        pass

    def exportar_fichero(self, ruta):
        pass

class MensajeTXT(Mensaje):
    def __init__(self, cuerpo):
        super().__init__("txt", cuerpo)

    def importar_fichero(self, ruta):
        with open(ruta, "r") as f:
            self.cuerpo = f.read()

    def exportar_fichero(self, ruta):
        with open(ruta, "w") as f:
            f.write(self.cuerpo)

class MensajeJSON(Mensaje):
    def __init__(self, cuerpo):
        super().__init__("json", cuerpo)

    def importar_fichero(self, ruta):
        with open(ruta, "r") as f:
            self.cuerpo = json.load(f)

    def exportar_fichero(self, ruta):
        with open(ruta, "w") as f:
            json.dump(self.cuerpo, f)