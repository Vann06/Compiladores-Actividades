"""
Simulación de una baraja de cartas
Hay un acierto cuando la carta está exactamente en la posición que le corresponde 

"""
import random 

repeticiones = 100000
resultados = []

for i in range(repeticiones):
    # baraja de cartas
    cartas = list(range(1, 101))

    # barajear cartas
    random.shuffle(cartas)

    # contar los aciertos 
    aciertos = 0

    for j in range(len(cartas)):
        if cartas[j] == j + 1:
            aciertos += 1

    resultados.append(aciertos)


# Calcular la esperanza 
esperanza = sum(resultados) / repeticiones

# Calcular la varianza
suma = 0 
for x in resultados:
    suma += (x - esperanza) ** 2

varianza = suma / repeticiones

print("Esperanza:", round(esperanza, 4))
print("Varianza:", round(varianza, 4))