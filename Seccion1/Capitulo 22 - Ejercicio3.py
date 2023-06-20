# Ejercicio #3
# Crea un programa que pida al usuario una temperatura en Celcius y los convierta a fahrenheit
# Formula: (°C * 9/5) + 32 = °F
# Imprimir grados celcius y grados fahrenheit

celcius = int(input("Introduzca la temperatura en celcius: ")) # Pedir temperatura en grados celcius al usuario
fahrenheit = (celcius * 9 / 5) + 32 # Conversion de celcius a fahrenheit

print(f"{celcius} grados Celcius es igual a {fahrenheit} grados fahrenheit")