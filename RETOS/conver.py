def decimal_a_binario(decimal):
    return bin(decimal).replace("0b", "")

try:
    numero_decimal = int(input("Ingresa un número entero decimal: "))
    if numero_decimal >= 0:
        binario = decimal_a_binario(numero_decimal)
        print(f"El equivalente binario de {numero_decimal} es {binario}.")
    else:
        print("Por favor, ingresa un número entero positivo.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
