
class Celular:
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento

    def informacion(self):
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}Gb")

    def encender(self):
        print("Encendiendo Celular")

    def apagar(self):
        print("Apagando Celular")

class Android(Celular):

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")

class Iphone(Celular):

    def transferir_archivos(self):
        print("Transifiriendo archivos a la computadora")


celular_android = Android("Blanco", 64)
# celular_android.expandir_almacenamiento()
# celular_android.informacion()
# celular_android.transferir_archivos()

celular_iphone = Iphone("Azul", 128)
celular_iphone.transferir_archivos()
celular_iphone.expandir_almacenamiento()

