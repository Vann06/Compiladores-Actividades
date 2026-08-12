"""Ejercicio 9: aproximación Monte Carlo de los incisos 3 al 9."""

import math
import random


SEMILLA = 23201
MUESTRAS = 500_000


def mostrar_resultado(inciso, estimacion, referencia):
    error = abs(estimacion - referencia)
    print(f"{inciso:>6} | {estimacion:>12.6f} | {referencia:>12.6f} | {error:>13.6f}")


rng = random.Random(SEMILLA)
sumas = {inciso: 0.0 for inciso in range(3, 10)}

for _ in range(MUESTRAS):
    # Inciso 3: integral de 0 a 1 de exp(e^x).
    u = rng.random()
    sumas[3] += math.exp(math.exp(u))

    # Inciso 4: integral de 0 a 1 de (1-x^2)^(3/2).
    sumas[4] += (1 - u * u) ** 1.5

    # Inciso 5: integral de -2 a 2 de e^(x+x^2).
    x = -2 + 4 * u
    sumas[5] += 4 * math.exp(x + x * x)

    # Inciso 6: cambio x = u/(1-u), para integrar de 0 a infinito.
    u = rng.random()
    x = u / (1 - u)
    sumas[6] += x * (1 + x * x) ** -2 / (1 - u) ** 2

    # Inciso 7: cambio x = tan(pi(u-1/2)), para integrar en toda la recta.
    u = rng.random()
    x = math.tan(math.pi * (u - 0.5))
    sumas[7] += math.exp(-x * x) * math.pi * (1 + x * x)

    # Inciso 8: integral doble sobre el cuadrado [0,1] x [0,1].
    x = rng.random()
    y = rng.random()
    sumas[8] += math.exp((x + y) ** 2)

    # Inciso 9: P(Y < X), con X y Y exponenciales independientes de tasa 1.
    x = rng.expovariate(1)
    y = rng.expovariate(1)
    sumas[9] += 1 if y < x else 0


referencias = {
    3: 6.3165638390,
    4: 3 * math.pi / 16,
    5: 93.1627532924,
    6: 0.5,
    7: math.sqrt(math.pi),
    8: 4.8991588511,
    9: 0.5,
}

print(f"Muestras por inciso: {MUESTRAS:,}")
print("Inciso |   Estimación |   Referencia | Error absoluto")
print("--------|--------------|--------------|---------------")

for inciso in range(3, 10):
    estimacion = sumas[inciso] / MUESTRAS
    mostrar_resultado(inciso, estimacion, referencias[inciso])
