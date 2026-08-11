"""
EJERCICIO 5

1. Lanzar dos dados justos y sumar sus resultados.
2. Guardar cada suma nueva entre 2 y 12.
3. Detener una repeticion cuando ya aparecieron las 11 sumas.
4. Repetir el experimento muchas veces.
5. Promediar la cantidad de lanzamientos utilizados.
"""

import itertools
import math
import random
import statistics


SEMILLA = 23201
SIMULACIONES = 100_000
SUMAS_POSIBLES = tuple(range(2, 13))


def lanzamientos_hasta_completar(rng):
    """Devuelve cuantos lanzamientos se necesitan para ver las 11 sumas."""
    observadas = set()
    lanzamientos = 0

    while len(observadas) < len(SUMAS_POSIBLES):
        dado_1 = rng.randint(1, 6)
        dado_2 = rng.randint(1, 6)
        observadas.add(dado_1 + dado_2)
        lanzamientos += 1

    return lanzamientos


def esperanza_exacta():
    """Calcula la esperanza teorica con inclusion-exclusion."""
    formas = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
    probabilidades = [cantidad / 36 for cantidad in formas]
    total = 0.0

    for tamano in range(1, len(probabilidades) + 1):
        signo = 1 if tamano % 2 == 1 else -1
        for grupo in itertools.combinations(probabilidades, tamano):
            total += signo / sum(grupo)

    return total


rng = random.Random(SEMILLA)
resultados = [lanzamientos_hasta_completar(rng) for _ in range(SIMULACIONES)]

estimacion = statistics.fmean(resultados)
desviacion = statistics.pstdev(resultados)
error_estandar = desviacion / math.sqrt(SIMULACIONES)
valor_exacto = esperanza_exacta()


print("Simulaciones:", f"{SIMULACIONES:,}")
print("Promedio estimado:", round(estimacion, 4))
print("Error estandar:", round(error_estandar, 4))
print("Esperanza teorica:", round(valor_exacto, 4))
print("Diferencia absoluta:", round(abs(estimacion - valor_exacto), 4))
