import mensaje as m

class GestorMensajes:
    def __init__(self):
        self.mensajes = []
    
    def importar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)
    
    def exportar_mensaje(self, ruta):
        self.mensajes[0].exportar_fichero(ruta)
        self.mensajes.pop(0)

    def enviar_mensaje(self):
        if not self.mensajes:
            print(">>> No hay mensajes en cola")
        else:
            mensaje_a_enviar = self.mensajes[0]
            print(f"Enviando mensaje de tipo {mensaje_a_enviar.tipo}: {mensaje_a_enviar.cuerpo}")
            # Quitar de la cola de mensajes
            self.mensajes.pop(0)


gestor = GestorMensajes()

mensaje_txt = m.MensajeTXT("")
mensaje_txt.importar_fichero("mensaje.txt")
mensaje_json = m.MensajeJSON("")
mensaje_json.importar_fichero("mensaje.json")

gestor.importar_mensaje(mensaje_txt)
gestor.importar_mensaje(mensaje_json)
gestor.enviar_mensaje()
gestor.enviar_mensaje()
gestor.enviar_mensaje()

mensaje_txt_exportacion = m.MensajeTXT("")
mensaje_txt_exportacion.importar_fichero("mensaje_a_exportar.txt")

gestor.importar_mensaje(mensaje_txt_exportacion)

gestor.exportar_mensaje("mensaje_exportado.txt")