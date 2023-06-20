from abc import ABC, abstractmethod
class Celular(ABC):
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.color = color
        self.almacenamiento = almacenamiento

    @abstractmethod
    def informacion(self):
        print(f"Color: {self.color}")

    @abstractmethod
    def encender(self):
        print("Encendiendo Celular")

    @abstractmethod
    def apagar(self):
        print("Apagando Celular")

class Android(Celular):

    def __init__(self, color, almacenamiento):
        super(Android, self).__init__(color, almacenamiento)
        
    def informacion(self):
        super(Android, self).informacion()

    def encender(self):
        super(Android, self).encender()
        print("Mostranto logo de Android")
        
    def apagar(self):
        super(Android, self).apagar()

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")

class Iphone(Celular):
    
    def __init__(self, color, almacenamiento):
        super(Iphone, self).__init__(color, almacenamiento)
        
    def informacion(self):
        super(Iphone, self).informacion()
        
    def encender(self):
        super(Iphone, self).encender()
        print("Mostrando logo de Iphone")
        
    def apagar(self):
        super(Iphone, self).apagar()

    def transferir_archivos(self):
        print("Transifiriendo archivos a la computadora")

# objeto = Celular("Blanco", 64)
celular_android = Android("Rojo", 128)
celular_android.encender()

celular_iphone = Iphone("Blanco", 128)
celular_iphone.encender()