
class Celular:
    variable_ejemplo = "Ejemplo"

    def __init__(self):
        self.color = "Rojo"

    def encender(self):
        print("Encendiendo telefono")

    def apagar(self):
        print("Apagando Celular")

objeto_celular = Celular()
print(objeto_celular.color)
objeto_celular.encender()
