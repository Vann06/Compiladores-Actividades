"""
EJERCICIO 6 

1. Elegir al azar una posicion de la lista.
2. Identificar el elemento seleccionado y cuantas veces aparece.
3. Calcular n * valor(elemento) / frecuencia(elemento).
4. Repetir el muestreo y promediar los resultados.

La division entre la frecuencia corrige el hecho de que los elementos repetidos
tienen mas probabilidad de ser seleccionados.
"""

from collections import Counter
import random
import statistics


SEMILLA = 23201
MUESTRAS = 50_000


def estimar_suma_distintos(lista, valores, muestras, semilla):
    frecuencias = Counter(lista)
    n = len(lista)
    rng = random.Random(semilla)
    estimadores = []

    for _ in range(muestras):
        elemento = lista[rng.randrange(n)]
        estimador = n * valores[elemento] / frecuencias[elemento]
        estimadores.append(estimador)

    return statistics.fmean(estimadores)


lista = ["A"] * 50 + ["B"] * 25 + ["C"] * 15 + ["D"] * 10
valores = {"A": 10, "B": 25, "C": 40, "D": 60}

estimacion = estimar_suma_distintos(lista, valores, MUESTRAS, SEMILLA)
valor_exacto = sum(valores[elemento] for elemento in set(lista))

print("Suma exacta:", valor_exacto)
print("Suma estimada:", round(estimacion, 4))
print("Error absoluto:", round(abs(estimacion - valor_exacto), 4))
