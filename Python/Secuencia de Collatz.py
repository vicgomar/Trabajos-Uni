numero_mayor = 0
cadena_mas_larga = 0

for numero_inicial in range(1, 1000000):
    n = numero_inicial
    terminos = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        terminos += 1

    if terminos > cadena_mas_larga:
        cadena_mas_larga = terminos
        numero_mayor = numero_inicial

print("PROBLEMA DE COLLATZ")
print("-------------------------")
print("Número inicial:", numero_mayor)
print("Cantidad de términos:", cadena_mas_larga)
