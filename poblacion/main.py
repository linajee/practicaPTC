"""
main.py
Script principal que ejecuta todos los módulos de análisis de población (R1-R5).

Este script ejecuta secuencialmente:
- R1: Variación de población por provincias
- R2: Población por comunidades autónomas
- R3: Gráfico de barras (Top 10 CCAA por sexo)
- R4: Variación de población por comunidades autónomas
- R5: Gráfico de evolución temporal (Top 10 CCAA)

Autores: Jose Daniel Ojeda Tro & Javier Linaje Vallejo
Fecha: 2025-12-07
"""
import R1 as r1
import R2 as r2
import R3 as r3
import R4 as r4
import R5 as r5

r1.R1()
r2.R2()
r3.R3()
r4.R4()
r5.R5()