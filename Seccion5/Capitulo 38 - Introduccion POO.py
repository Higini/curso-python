class Celular:
    variable_ejemplo = "Ejemplo"


variable_contenedora_objeto_celular = Celular()

# print(variable_contenedora_objeto_celular.variable_ejemplo)

objeto2 = Celular()
# print(objeto2.variable_ejemplo)
objeto2.variable_ejemplo = "Ejemplo - Objeto 2"

print(variable_contenedora_objeto_celular.variable_ejemplo)
print(objeto2.variable_ejemplo)

