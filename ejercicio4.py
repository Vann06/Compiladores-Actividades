"""
EJERCICIO 4 

1. Iniciar una lista de 25 unos, porque 1 tiene probabilidad 0.8.
2. Generar las distancias entre los ceros con una variable geometrica.
3. Colocar un cero cada vez que la posicion calculada quede dentro de la lista.
4. Contar cuantos numeros aleatorios fueron necesarios.

Este procedimiento es mas eficiente que generar un numero aleatorio para cada
posicion cuando los ceros son poco frecuentes.
"""

import math
import random


SEMILLA = 23201
CANTIDAD = 25
PROBABILIDAD_DE_UNO = 0.8

rng = random.Random(SEMILLA)
valores = [1] * CANTIDAD
posicion = 0
numeros_usados = 0

while True:
    # U queda en el intervalo (0, 1], lo que evita calcular log(0).
    u = 1 - rng.random()
    numeros_usados += 1

    # Y es geometrica con probabilidad 0.2 y representa la distancia
    # hasta el siguiente cero.
    y = int(math.log(u) / math.log(PROBABILIDAD_DE_UNO)) + 1
    posicion += y

    if posicion > CANTIDAD:
        break

    valores[posicion - 1] = 0

print("Secuencia generada:", valores)
print("Cantidad de unos:", valores.count(1))
print("Cantidad de ceros:", valores.count(0))
print("Numeros aleatorios utilizados:", numeros_usados)
