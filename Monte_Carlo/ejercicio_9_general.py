"""Aproximación Monte Carlo para el ejercicio 9.

La región del ejercicio es D = {(x, y): 0 <= x < infinito, 0 <= y <= x}.
Los datos de la integral se leen desde un archivo de texto; por tanto, la
función no está escrita de forma fija dentro del programa.
"""

from __future__ import annotations

import argparse
import ast
import configparser
import math
import random
import statistics
from pathlib import Path


FUNCIONES_PERMITIDAS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "exp": math.exp,
    "log": math.log,
    "abs": abs,
    "pi": math.pi,
    "e": math.e,
}


def validar_expresion(expresion: str) -> None:
    """Comprueba que la expresión usa solo x, y y funciones matemáticas autorizadas."""
    try:
        arbol = ast.parse(expresion, mode="eval")
    except SyntaxError as error:
        raise ValueError(f"La expresión no es válida: {error.msg}") from error

    nombres = {"x", "y", *FUNCIONES_PERMITIDAS}
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Name) and nodo.id not in nombres:
            raise ValueError(f"El nombre '{nodo.id}' no está permitido en la función.")
        if isinstance(nodo, ast.Call) and not isinstance(nodo.func, ast.Name):
            raise ValueError("Solo se permiten llamadas directas a funciones matemáticas.")
        if isinstance(nodo, (ast.Attribute, ast.Subscript, ast.List, ast.Dict, ast.Set)):
            raise ValueError("La expresión contiene una construcción no permitida.")


def crear_funcion(expresion: str):
    validar_expresion(expresion)
    codigo = compile(expresion, "<funcion del archivo>", "eval")

    def funcion(x: float, y: float) -> float:
        valor = eval(codigo, {"__builtins__": {}}, {**FUNCIONES_PERMITIDAS, "x": x, "y": y})
        valor = float(valor)
        if not math.isfinite(valor):
            raise ValueError("La función produjo un valor no finito.")
        return valor

    return funcion


def leer_configuracion(ruta: Path) -> dict[str, str]:
    """Lee pares clave=valor en un .txt, ignorando líneas vacías y comentarios #."""
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {ruta}")

    # ConfigParser evita escribir un analizador manual y mantiene el formato .txt sencillo.
    contenido = "[ejercicio_9]\n" + ruta.read_text(encoding="utf-8")
    parser = configparser.ConfigParser(inline_comment_prefixes=("#",), interpolation=None)
    parser.optionxform = str
    parser.read_string(contenido)
    datos = dict(parser["ejercicio_9"])

    requeridas = {"funcion", "muestras", "tasa_exponencial"}
    faltantes = requeridas - datos.keys()
    if faltantes:
        raise ValueError("Faltan claves obligatorias: " + ", ".join(sorted(faltantes)))
    return datos


def estimar(funcion, muestras: int, tasa: float, semilla: int | None) -> tuple[float, float]:
    """Aplica muestreo por importancia sobre la región triangular no acotada."""
    if muestras < 2:
        raise ValueError("'muestras' debe ser un entero mayor o igual que 2.")
    if tasa <= 0:
        raise ValueError("'tasa_exponencial' debe ser positiva.")

    generador = random.Random(semilla)
    estimadores = []
    for _ in range(muestras):
        # X ~ Exp(tasa) y, condicionado a X=x, Y ~ Uniforme(0, x).
        x = generador.expovariate(tasa)
        y = generador.uniform(0.0, x)
        # q(x,y) = tasa*exp(-tasa*x)/x; por ello f(x,y)/q(x,y) es:
        peso = funcion(x, y) * x * math.exp(tasa * x) / tasa
        if not math.isfinite(peso):
            raise ValueError("El peso de importancia no fue finito; pruebe otra tasa o función.")
        estimadores.append(peso)

    media = statistics.fmean(estimadores)
    error_estandar = statistics.stdev(estimadores) / math.sqrt(muestras)
    return media, error_estandar


def construir_reporte(datos: dict[str, str], aproximacion: float, error: float) -> str:
    muestras = int(datos["muestras"])
    tasa = float(datos["tasa_exponencial"])
    inferior, superior = aproximacion - 1.96 * error, aproximacion + 1.96 * error
    semilla = datos.get("semilla", "aleatoria")
    lineas = [
        "# Reporte: ejercicio 9 — Monte Carlo",
        "",
        "## Planteamiento",
        "",
        "Se aproxima la integral doble sobre la región triangular no acotada",
        "\\(D=\\{(x,y): 0\\le y\\le x,\\;0\\le x<\\infty\\}\\).",
        "",
        f"- Función leída: `f(x, y) = {datos['funcion']}`",
        f"- Número de muestras: {muestras:,}",
        f"- Semilla: {semilla}",
        "",
        "## Método",
        "",
        f"Se usó muestreo por importancia: \\(X\\sim Exp({tasa:g})\\) y, dado \\(X=x\\), \\(Y\\sim U(0,x)\\).",
        "La densidad conjunta es \\(q(x,y)=\\lambda e^{-\\lambda x}/x\\), de modo que cada réplica es",
        "",
        "\\[ Z_i=f(X_i,Y_i)\\frac{X_i e^{\\lambda X_i}}{\\lambda}. \\]",
        "",
        "La estimación final es el promedio de las réplicas \\((1/n)\\sum Z_i\\). Esta transformación permite",
        "simular una región infinita sin imponer arbitrariamente un límite superior para \\(x\\).",
        "",
        "## Resultados",
        "",
        f"- Estimación Monte Carlo: **{aproximacion:.8f}**",
        f"- Error estándar estimado: **{error:.8f}**",
        f"- Intervalo de confianza aproximado al 95 %: **[{inferior:.8f}, {superior:.8f}]**",
    ]

    exacto_texto = datos.get("valor_exacto", "").strip()
    if exacto_texto:
        exacto = float(exacto_texto)
        diferencia = abs(aproximacion - exacto)
        relativo = diferencia / abs(exacto) * 100 if exacto != 0 else None
        lineas += [
            f"- Valor exacto proporcionado: **{exacto:.8f}**",
            f"- Error absoluto: **{diferencia:.8f}**",
            "- Error relativo: **no definido**" if relativo is None else f"- Error relativo: **{relativo:.4f} %**",
        ]
    else:
        lineas += [
            "",
            "No se proporcionó `valor_exacto`; por ello el programa reporta la incertidumbre estadística,",
            "pero no inventa una respuesta analítica para comparar.",
        ]

    lineas += [
        "",
        "## Conclusión",
        "",
        "El resultado es una estimación aleatoria, no un valor exacto. Al aumentar el número de muestras,",
        "el error estándar suele disminuir aproximadamente en proporción a \\(1/\\sqrt{n}\\). Para repetir",
        "exactamente el experimento debe conservarse la misma semilla.",
        "",
    ]
    return "\n".join(lineas)


def main() -> None:
    directorio = Path(__file__).resolve().parent
    argumentos = argparse.ArgumentParser(description="Ejercicio 9: integral doble por Monte Carlo.")
    argumentos.add_argument("entrada", nargs="?", type=Path, default=directorio / "ejercicio_9.txt")
    argumentos.add_argument("--salida", type=Path, default=directorio / "reporte_ejercicio_9.md")
    args = argumentos.parse_args()

    datos = leer_configuracion(args.entrada)
    funcion = crear_funcion(datos["funcion"])
    semilla = int(datos["semilla"]) if datos.get("semilla", "").strip() else None
    aproximacion, error = estimar(funcion, int(datos["muestras"]), float(datos["tasa_exponencial"]), semilla)
    reporte = construir_reporte(datos, aproximacion, error)
    args.salida.write_text(reporte, encoding="utf-8")
    print(reporte)
    print(f"Reporte guardado en: {args.salida.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, configparser.Error, OverflowError) as error:
        raise SystemExit(f"Error: {error}")
