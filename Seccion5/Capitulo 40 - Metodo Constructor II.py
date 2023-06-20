
class Celular:
    variable_ejemplo = "Ejemplo"


    def __init__(self, color):
        self.color = color

    def encender(self, contrasena):
        print(f"Encendiendo telefono {contrasena}")
        print(self.color)

    def apagar(self):
        print("Apagando Celular")

objeto_celular = Celular("Blanco")
print(objeto_celular.color)
objeto_celular.encender("2546")
