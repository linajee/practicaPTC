# Práctica: Análisis de Población (INE) 🇪🇸

Este repositorio contiene la **Práctica Evaluable** de la asignatura **Programación Técnica y Científica** (Grado en Ingeniería Informática, UGR).

El objetivo es procesar datos reales de población del INE (Instituto Nacional de Estadística) utilizando **Python**, `numpy`, `matplotlib` y `BeautifulSoup`, sin hacer uso de la librería Pandas.

## 📋 Descripción del Proyecto

El proyecto consiste en un conjunto de scripts en Python que procesan datos de entrada (CSV y HTML) para generar informes estadísticos en formato web (tablas HTML) y gráficos de evolución demográfica.

**Datos procesados:**
* Población por provincias y sexo (2010-2017).
* Estructura de Comunidades Autónomas y Provincias.

### ⚠️ Requisitos y Restricciones Técnicas
Este proyecto sigue estrictamente las restricciones académicas:
* 🚫 **Prohibido el uso de Pandas** (DataFrames).
* ✅ Uso obligatorio de **Diccionarios** y **Numpy Arrays** como estructuras de datos principales.
* ✅ Modularización mediante `funciones.py`.
* ✅ Compatible con **Ubuntu 24.04** y **Python 3.13.5**.

## 🛠️ Estructura del Proyecto

El proyecto sigue la estructura de directorios obligatoria para la entrega:

```text
poblacion/
├── entradas/                       # Archivos de datos suministrados (CSV y HTML)
│   ├── comunidadAutonoma-Provincia.html
│   ├── comunidadesAutonomas.html
│   └── poblacionProvinciasHM2010-17.csv
├── imagenes/                       # Gráficos generados por matplotlib (R3.png, R5.png)
├── resultados/                     # Tablas HTML generadas (Salida de los scripts)
├── funciones.py                    # Biblioteca de funciones comunes
├── main.py                         # Script principal (lanza R1-R5)
├── R1.py                           # Variación por provincias (Absoluta/Relativa)
├── R2.py                           # Población por CC.AA.
├── R3.py                           # Gráfico de barras (Población 2017)
├── R4.py                           # Variación por CC.AA.
├── R5.py                           # Gráfico de líneas (Evolución 2010-2017)
├── memoria.pdf                     # Documentación del alumno
└── README.md
