numero = 600851475143
factor = 2

while numero > 1:
    if numero % factor == 0:
        numero = numero // factor
    else:
        factor += 1

print("El mayor factor primo es:", factor)