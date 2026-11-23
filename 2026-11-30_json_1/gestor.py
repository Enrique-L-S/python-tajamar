# Ejercicio:
# Hacer un gestor de mensajes, que pueda manejar mensajes (tanto enviar como recibir), por otra parte, tenemos que tener mensajes que se puedan gestionar como txt, y mensajes que se puedan gestionar como json
# Lo que el usuario tendrá es o bien un json o txt, y tendremos que conseguir que eso sea un mensaje, y que la info este en un objeto
# O bien al contrario, un mensaje de uno de esos dos tipos, y que se convierta en un json o txt
# Todo a través del gestor!
# Puntos extra si dividimos un poco el código en varios módulos!
# Por cierto, el código debería de poder adaptar fácilmente otro tipo de mensajes (SMS, email, HTML, etc...)
import json
import mensaje

class GestorMensajes:
    def __init__(self):
        self.mensajes = []
    
    def importar_mensaje(self, ruta, tipo):
        if tipo == "txt":
            mensaje_txt = mensaje.MensajeTXT("")
            mensaje_txt.importar_fichero(ruta)
            self.mensajes.append(mensaje_txt)
        elif tipo == "json":
            mensaje_json = mensaje.MensajeJSON("")
            mensaje_json.importar_fichero(ruta)
            self.mensajes.append(mensaje_json)
        else:
            raise ValueError("Tipo de mensaje no soportado")
    
    def exportar_mensaje(self, ruta):
        mensaje_a_exportar = self.mensajes[0]
        if isinstance(mensaje_a_exportar, mensaje.MensajeTXT):
            with open(ruta, "w") as f:
                f.write(mensaje_a_exportar.cuerpo)
        elif isinstance(mensaje_a_exportar, mensaje.MensajeJSON):
            with open(ruta, "w") as f:
                json.dump(mensaje_a_exportar.cuerpo, f)
        else:
            raise ValueError("Tipo de mensaje no soportado para exportación")

    def enviar_mensaje(self):
        if not self.mensajes:
            print(">>> No hay mensajes en cola")
        else:
            mensaje_a_enviar = self.mensajes[0]
            print(f"Enviando mensaje de tipo {mensaje_a_enviar.tipo}: {mensaje_a_enviar.cuerpo}")
            # Quitar de la cola de mensajes
            self.mensajes.pop(0)


gestor = GestorMensajes()
gestor.importar_mensaje("mensaje.txt", "txt")
gestor.importar_mensaje("mensaje.json", "json")
gestor.enviar_mensaje()
gestor.enviar_mensaje()
gestor.enviar_mensaje()

gestor.importar_mensaje("mensaje.txt", "txt")
gestor.exportar_mensaje("mensaje_exportado.txt")