# Actividades de Modelación y Simulación

Repositorio con nueve ejercicios de simulación escritos en Python. Cada archivo se ejecuta de forma independiente y muestra sus resultados en la terminal. Los ejercicios usan una semilla cuando es importante poder repetir el experimento.

## Requisitos y ejecución

Se requiere Python 3.10 o superior. El repositorio incluye un entorno virtual en `Monte_Carlo/.venv`; desde la raíz se pueden ejecutar todos los ejercicios con:

```powershell
$python = .\Monte_Carlo\.venv\Scripts\python.exe
1..9 | ForEach-Object { & $python ".\ejercicio$_.py" }
```

Para ejecutar uno solo:

```powershell
.\Monte_Carlo\.venv\Scripts\python.exe .\ejercicio5.py
```

## Resumen de ejercicios

| Archivo | Tema | Resultado principal |
| --- | --- | --- |
| `ejercicio1.py` | Inventario de botellas | Simula 15 días de demanda, ventas, sobrantes y pérdidas. |
| `ejercicio2.py` | Variable discreta | Genera una variable aleatoria con cuatro posibles valores. |
| `ejercicio3.py` | Baraja aleatoria | Estima la esperanza y varianza de cartas que quedan en su posición. |
| `ejercicio4.py` | Variables geométricas | Genera una secuencia binaria de 25 posiciones de manera eficiente. |
| `ejercicio5.py` | Lanzamiento de dados | Estima cuántos lanzamientos se necesitan para observar todas las sumas posibles. |
| `ejercicio6.py` | Estimación por muestreo | Aproxima la suma de valores distintos en una lista con repeticiones. |
| `ejercicio7.py` | Adelgazamiento | Simula una variable de riesgo discreto con tasa variable. |
| `ejercicio8.py` | Aceptación y rechazo | Genera la distribución condicional de `X` dado un evento de `Y`. |
| `ejercicio9.py` | Integración Monte Carlo | Ejecuta los incisos 3–9 y compara cada estimación con su referencia. |

## Ejercicio 9: integrales por Monte Carlo

El programa ejecuta las siete integrales de los incisos 3–9 con 500,000 muestras por inciso. Al finalizar muestra una tabla con la estimación de Monte Carlo, la referencia exacta o numérica y el error absoluto. La semilla está definida para poder repetir los mismos resultados.
