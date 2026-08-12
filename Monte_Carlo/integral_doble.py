
# INTEGRALES DOBLE CON MONTE CARLO 
import random
import math

texto = input("Ingrese la función en x y y: ")

a = float(input("Límite inferior de x: "))
b = float(input("Límite superior de x: "))

c = float(input("Límite inferior de y: "))
d = float(input("Límite superior de y: "))

n = int(input("Cantidad de puntos aleatorios: "))

def f(x, y):
    return eval(texto, {"__builtins__": {}}, {
        "x": x,
        "y": y,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "exp": math.exp,
        "log": math.log,
        "pi": math.pi
    })

# Generar puntos aleatorios (x, y)
puntos = [
    (
        random.uniform(a, b),
        random.uniform(c, d)
    )
    for _ in range(n)
]

# Evaluar la función en cada punto
valores = [f(x, y) for x, y in puntos]

# Calcular el promedio
promedio = sum(valores) / n

# Área del rectángulo
area = (b - a) * (d - c)

# Integral aproximada
integral = area * promedio

print("Promedio de los valores:", promedio)
print("Área de la región:", area)
print("Resultado aproximado:", integral)