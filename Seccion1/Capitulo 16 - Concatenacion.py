numero_entero = 20
numero_flotante = 3.14159
nombre = "Gregory"

# Formas de concatenacion de numeros enteros
print("El valor es:", numero_entero, "asda", 10)
print("El valor es: %i %i" %(numero_entero, 7.5) )
print("El valor es: " + str(numero_entero) + " asdfasdf")
print(f"El valor es {numero_entero} {numero_entero}")

# Formas de concatenacion de numeros flotantes
print("El valor es:", numero_flotante)
print("El valor es: %.3f" %(numero_flotante))
print("El valor es: " + str(numero_flotante))
print(f"El valor es {numero_flotante}")

# Formas de concatenacion de cadenas
print("El nombre es:", nombre)
print("El nombre es: %s, la edad es: %i " %(nombre, numero_entero))
print("El nombre es: " + nombre)
print(f"El nombre es {nombre}, la edad es: {numero_entero}")
