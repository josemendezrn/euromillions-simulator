# Simulador de Euromillones con Python

Este proyecto consiste en un script interactivo en Python desarrollado para cumplir con un reto de lógica de programación y manejo de estructuras de datos.

## 🛠️ Características Técnicas

* **Muestreo Aleatorio Simple:** Se utiliza la librería `random` (específicamente `random.sample`) para garantizar la extracción de elementos únicos sin reemplazo, cumpliendo con las reglas de la lotería europea (5 números del 1 al 50 y 2 estrellas del 1 al 12).
* **Control de Excepciones:** Implementación de un bloque `try-except` manejando `ValueError` para robustecer el programa contra entradas inválidas de usuario.
* **Estructura de Datos Limpia:** Los datos se capturan internamente en diccionarios (`clave-valor`) organizados dentro de una lista, permitiendo una fácil legibilidad y escalabilidad para análisis de datos futuros (ej. migración a DataFrames de Pandas).

## 🚀 Cómo Ejecutarlo

1. Clonar o descargar este repositorio.
2. Ejecutar el archivo en tu consola:
   ```bash
   python euromillones.py
