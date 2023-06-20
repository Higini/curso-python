texto = ""
while texto != "salir":
    x = 0
    print("la condicion sigue siendo verdadera")
    texto = input("Escribe Salir para terminar el programa")
    while x < 5:
        print(x)
        x += 1
else:
    print("La variable texto = salir")

