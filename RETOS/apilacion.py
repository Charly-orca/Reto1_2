def es_apilado_triangular(num):
    suma_total = 0
    nivel = 1

    while suma_total < num:
        suma_total += nivel
        nivel += 1

    return suma_total == num

try:
    numero_latas = int(input("Ingresa la cantidad de latas de mermelada a apilar: "))
    if es_apilado_triangular(numero_latas):
        print(f"{numero_latas} es adecuado para apilar.")
    else:
        print(f"{numero_latas} no es adecuado para apilar.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
8