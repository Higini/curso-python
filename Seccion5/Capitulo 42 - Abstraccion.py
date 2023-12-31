from abc import ABC, abstractmethod
class Celular(ABC):
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento

    def informacion(self):
        print(f"Color: {self.color}")

    def encender(self):
        print("Encendiendo Celular")

    def apagar(self):
        print("Apagando Celular")

class Android(Celular):

    def __init__(self, color, almacenamiento):
        super(Android, self).__init__(color, almacenamiento)

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")

class Iphone(Celular):

    def transferir_archivos(self):
        print("Transifiriendo archivos a la computadora")

# objeto = Celular("Blanco", 64)
celular_android = Android("Rojo", 128)