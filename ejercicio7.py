"""
EJERCICIO 7 

1. Generar una distancia Y geometrica con parametro lambda.
2. Sumar Y para obtener un tiempo candidato S.
3. Aceptar S con probabilidad lambda_S / lambda.
4. Si se rechaza, generar otra distancia y continuar.

El metodo adelgaza una tasa constante lambda para obtener las tasas variables
lambda_n solicitadas.
"""

import math
import random
import statistics


SEMILLA = 23201
SIMULACIONES = 100_000
LAMBDA_MAXIMA = 0.35


def tasa_riesgo(n):
    """Ejemplo de tasas lambda_n acotadas por 0.35."""
    return min(0.05 + 0.015 * n, LAMBDA_MAXIMA)


def generar_x(rng):
    s = 0

    while True:
        u = 1 - rng.random()
        y = int(math.log(u) / math.log(1 - LAMBDA_MAXIMA)) + 1
        s += y

        if rng.random() <= tasa_riesgo(s) / LAMBDA_MAXIMA:
            return s


rng = random.Random(SEMILLA)
resultados = [generar_x(rng) for _ in range(SIMULACIONES)]

print("Simulaciones:", f"{SIMULACIONES:,}")
print("Promedio de X:", round(statistics.fmean(resultados), 4))
print("n | lambda_n | riesgo estimado")

for n in range(1, 9):
    en_riesgo = sum(x >= n for x in resultados)
    eventos = resultados.count(n)
    riesgo_estimado = eventos / en_riesgo
    print(f"{n:1d} | {tasa_riesgo(n):.4f}   | {riesgo_estimado:.4f}")
