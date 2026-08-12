# INTEGRALES SIMPLES CON MONTE CARLO

import random
import math

texto = input("Ingrese la función en x: ")
a = float(input("Límite inferior: "))
b = float(input("Límite superior: "))
n = int(input("Cantidad de números aleatorios: "))

def f(x):
    return eval(texto, {"__builtins__": {}}, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "exp": math.exp,
        "log": math.log,
        "pi": math.pi
    })

# Generar n números aleatorios entre a y b
puntos = [random.uniform(a, b) for _ in range(n)]

# Evaluar la función en cada número aleatorio
valores = [f(x) for x in puntos]

# Sumar los valores y dividirlos entre n
promedio = sum(valores) / n

# Multiplicar el promedio por el ancho del intervalo
integral = (b - a) * promedio

print("Promedio de los valores:", promedio)
print("Resultado aproximado:", integral)