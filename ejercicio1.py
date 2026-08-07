 
"""""
DEMANDA DE BOTELLAS 
1. Generar numero aleatorio entre 0 y 1 
2. Convertir a demanda de 0 a 5 botellas 
3. Comparar esa demanda contra las 3 botellas disponibles 
4. Guardar 
5. Repetir 15 veces/dias
6. Concluir
"""

import random 

# acumuladores 
demanda_total = 0
ventas_totales = 0
sobrantes_totales = 0
perdidas_totales = 0

dias_sobrante = 0
dias_exactos = 0
dias_faltante = 0

# lo que ya tenemos
inventario = 3

# lo corremos por los 15 dias
for dia in range(1, 16):

    numero = random.random()

    # Convertir el número aleatorio a demanda de botellas
    if numero < 0.05:
        demanda = 0
    elif numero < 0.20:
        demanda = 1
    elif numero < 0.50:
        demanda = 2
    elif numero < 0.80:
        demanda = 3
    elif numero < 0.95:
        demanda = 4
    else:
        demanda = 5

    # Comparar la demanda con el inventario y calcular ventas, sobrantes y pérdidas
    if demanda < inventario:
        ventas = demanda
        sobrantes = inventario - demanda
        perdidas = 0
        resultado = "Sobró inventario"
    # Si es igual se vende todo y no hay sobrantes ni pérdidas
    elif demanda == inventario:
        ventas = demanda
        sobrantes = 0
        perdidas = 0
        resultado = "Inventario exacto"
    # hizo falta :/ 
    else:
        ventas = inventario
        sobrantes = 0
        perdidas = demanda - inventario
        resultado = "Faltó inventario"

    # ir guardando los totales
    demanda_total += demanda
    ventas_totales += ventas
    sobrantes_totales += sobrantes
    perdidas_totales += perdidas

    if resultado == "Sobró inventario":
        dias_sobrante += 1

    elif resultado == "Inventario exacto":
        dias_exactos += 1

    else:
        dias_faltante += 1

    # Reporte del dia 
    print("Día:", dia)
    print("Número aleatorio:", round(numero, 4))
    print("Demanda:", demanda)
    print("Ventas:", ventas)
    print("Sobrantes:", sobrantes)
    print("Ventas perdidas:", perdidas)
    print("Resultado:", resultado)
    print()


promedio_demanda = demanda_total / 15

print("----- RESUMEN DE LA SIMULACIÓN -----")
print("Demanda total:", demanda_total)
print("Ventas totales:", ventas_totales)
print("Botellas sobrantes:", sobrantes_totales)
print("Ventas perdidas:", perdidas_totales)
print("Días con inventario sobrante:", dias_sobrante)
print("Días con inventario exacto:", dias_exactos)
print("Días con inventario insuficiente:", dias_faltante)
print("Promedio de demanda diaria:", round(promedio_demanda, 2))