import random

u = random.random()

if u < 0.30:
    x = 1
elif u < 0.50:
    x = 2
elif u < 0.85:
    x = 3
else:
    x = 4

print("Número aleatorio:", round(u, 4))
print("Valor de X:", x)