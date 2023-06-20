from abc import ABC, abstractmethod


class Celular(ABC):
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.__color = color
        self.__almacenamiento = almacenamiento
        self.__volumen = 5

    @abstractmethod
    def informacion(self):
        print(f"Color: {self.__color}")
        print(f"Almacenamiento: {self.__almacenamiento}")
        print(f"Nivel Volumen: {self.__volumen}")

    @abstractmethod
    def encender(self):
        print("Encendiendo Celular")

    @abstractmethod
    def apagar(self):
        print("Apagando Celular")

    # def obtener_volumen(self):
    #     return self.__volumen
    #
    # def subir_volumen(self):
    #     self.__volumen += 1
    #     print(f"Nivel de volumen actual: {self.__volumen}")
    #
    # def bajar_volumen(self):
    #     self.__volumen -= 1
    #     print(f"Nivel de volumen actual: {self.__volumen}")

    @property
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, valor):
        self.__volumen = valor

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
# celular_android = Android("Rojo", 128)
# celular_android.informacion()
# celular_android.



# celular_android.encender()

celular_iphone = Iphone("Blanco", 128)
# celular_iphone.encender()
celular_iphone.informacion()

celular_iphone.volumen = 12
print(celular_iphone.volumen)
celular_iphone.informacion()