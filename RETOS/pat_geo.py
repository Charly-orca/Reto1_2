def generar_triangulo_rectangulo(altura):
    for i in range(altura, 0, -1):
        fila = ""
        for j in range(i, 0, -1):
            fila += str(j) + " "
        print(fila)

try:
    altura_triangulo = int(input("Ingresa la altura del triángulo (número entero positivo): "))
    if altura_triangulo > 0:
        generar_triangulo_rectangulo(altura_triangulo)
    else:
        print("Por favor, ingresa un número entero positivo.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
