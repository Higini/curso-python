# Ejercicio #2
# Escribe un programa que le pida al usuario un numero de horas de trabajo diarias y una tarifa por hora para calcular el salario
# Al final imprimir el salario

horas = int(input("Introduzca el numero de horas de trabajo: "))
tarifa = float(input("Introduzca la tarifa por hora: "))
salario = horas*tarifa
print(f"El salario al dia es de: {salario}")
