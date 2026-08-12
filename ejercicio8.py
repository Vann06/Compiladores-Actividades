"""
EJERCICIO 8

1. Generar X con su distribucion marginal.
2. Si X = i, aceptar con probabilidad P(Y = j | X = i).
3. Si se acepta, devolver W = i.
4. Si se rechaza, volver a generar X.
5. Comparar las probabilidades simuladas con P(X = i | Y = j).
"""

from collections import Counter
import random


SEMILLA = 23201
SIMULACIONES = 100_000
VALORES_X = (1, 2, 3)
PROBABILIDAD_X = (0.40, 0.35, 0.25)
PROBABILIDAD_YJ_DADO_X = {1: 0.20, 2: 0.50, 3: 0.80}


def generar_w(rng):
    intentos = 0

    while True:
        i = rng.choices(VALORES_X, weights=PROBABILIDAD_X, k=1)[0]
        intentos += 1

        if rng.random() < PROBABILIDAD_YJ_DADO_X[i]:
            return i, intentos


probabilidad_yj = sum(
    p_x * PROBABILIDAD_YJ_DADO_X[i]
    for i, p_x in zip(VALORES_X, PROBABILIDAD_X)
)
exactas = {
    i: p_x * PROBABILIDAD_YJ_DADO_X[i] / probabilidad_yj
    for i, p_x in zip(VALORES_X, PROBABILIDAD_X)
}

rng = random.Random(SEMILLA)
conteos = Counter()
intentos_totales = 0

for _ in range(SIMULACIONES):
    w, intentos = generar_w(rng)
    conteos[w] += 1
    intentos_totales += intentos

print("Aceptaciones:", f"{SIMULACIONES:,}")
print("Promedio de intentos por aceptacion:", round(intentos_totales / SIMULACIONES, 4))
print("i | simulada | exacta")

for i in VALORES_X:
    simulada = conteos[i] / SIMULACIONES
    print(f"{i} | {simulada:.4f}   | {exactas[i]:.4f}")
