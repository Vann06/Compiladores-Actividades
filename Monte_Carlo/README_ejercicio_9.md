# Ejercicio 9 generalizado

Este programa resuelve por simulación integrales de la forma

\[
\int_0^\infty\int_0^x f(x,y)\,dy\,dx.
\]

No contiene una función ni una respuesta fija: toma ambas (la respuesta exacta es opcional) de `ejercicio_9.txt`. Es adecuado para el dominio del ejercicio 9; no se debe usar sin modificarlo para regiones distintas.

## Uso

Desde la carpeta `Monte_Carlo`, ejecute:

```powershell
.\.venv\Scripts\python.exe .\ejercicio_9_general.py
```

También se puede usar otro archivo de entrada y decidir el nombre del reporte:

```powershell
.\.venv\Scripts\python.exe .\ejercicio_9_general.py .\mi_integral.txt --salida .\mi_reporte.md
```

El programa imprime la respuesta y guarda un reporte Markdown que documenta el planteamiento, el método, la estimación, el error estándar y el intervalo de confianza aproximado del 95 %.

## Formato del archivo de entrada

Cada línea tiene la forma `clave = valor`. Las líneas que empiezan con `#` son comentarios.

| Clave | Obligatoria | Descripción |
| --- | --- | --- |
| `funcion` | Sí | Expresión de `x` e `y`; por ejemplo, `exp(-(x+y))`. |
| `muestras` | Sí | Número de réplicas Monte Carlo (mínimo 2). |
| `tasa_exponencial` | Sí | Parámetro positivo de la distribución auxiliar. |
| `semilla` | No | Entero para repetir exactamente la simulación. Si se omite, cada corrida es diferente. |
| `valor_exacto` | No | Número usado únicamente para comparar; el programa no lo calcula ni lo supone. |

Las funciones permitidas son `exp`, `sin`, `cos`, `tan`, `sqrt`, `log` y `abs`; también se permiten las constantes `pi` y `e`.

## Justificación del método

La región es infinita, por lo que no conviene generar puntos uniformes en un rectángulo artificial. Se generan puntos con `X` exponencial de tasa \(\lambda\) y, una vez obtenido `X=x`, se toma `Y` uniforme entre 0 y `x`. Así, todos los puntos están en la región requerida. Cada observación se corrige con su peso de importancia; el promedio de esos pesos estima la integral.

La tasa exponencial puede influir en la variabilidad. Conviene escoger una tasa que produzca más puntos donde la función tenga valores importantes. Si se cambia la tasa, la integral objetivo no cambia, pero sí pueden cambiar el error estándar y el intervalo de confianza.
