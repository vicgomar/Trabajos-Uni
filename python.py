import math
from functools import reduce

numeros = range(1, 21)

resultado = reduce(math.lcm, numeros)

print(resultado)