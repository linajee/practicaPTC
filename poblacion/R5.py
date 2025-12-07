"""
R5.py
Módulo que genera un gráfico de líneas mostrando la evolución de la población total
(2010-2017) para las 10 comunidades autónomas con mayor población media.
El gráfico se inserta en el HTML de variación por comunidades autónomas.

Autores: Jose Daniel Ojeda Tro & Javier Linaje Vallejo 
Fecha: 2025-12-07
"""
import matplotlib.pyplot as plt
import funciones as func
from R2 import TablaPoblacionMediaCCAA
from R3 import ObtenerTopCCAA, AñadirImagenHtml


def GraficoLineasEvolucion(nombres, datos_totales):
    """
    Genera un gráfico de líneas mostrando la evolución de población total 
    para las CCAA indicadas durante el período 2010-2017.
    
    Parámetros:
        nombres (list): Lista con los nombres de las CCAA
        datos_totales (numpy.ndarray): Matriz con datos de población total (años 2010-2017)
                                        Forma: (n_ccaa, 8 años)
    
    Retorna:
        None (guarda el gráfico en ./imagenes/evolucion_poblacion_ccaa.png)
    """
    plt.figure(figsize=(12, 6))
    plt.title("Evolución de la Población Total por CCAA (2010-2017)")
    
    años = list(range(2010, 2018))  # 2010 a 2017 inclusive
    
    # Dibujar una línea por cada CCAA
    for i, nombre in enumerate(nombres):
        plt.plot(años, datos_totales[i], marker='o', label=nombre, linewidth=2)
    
    plt.xlabel("Año")
    plt.ylabel("Población Total")
    plt.legend(loc='best', fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('./imagenes/evolucion_poblacion_ccaa.png')
    print("Gráfico guardado en './imagenes/evolucion_poblacion_ccaa.png'")


def R5():
    """
    Función principal que ejecuta el módulo R5.
    
    Genera un gráfico de líneas con la evolución de población de las 10 CCAA
    con mayor población media y lo inserta en el HTML de variación por comunidades.
    
    Parámetros:
        None
    
    Retorna:
        None
    """
    provincias, total, p_hombres, p_mujeres = func.LeerPoblacionProvincias('./entradas/poblacionProvinciasHM2010-17.csv')
    
    tabla = TablaPoblacionMediaCCAA(provincias, total, p_hombres, p_mujeres)
    
    tabla_top10 = ObtenerTopCCAA(tabla, n=10)
    
    comunidades_sin_cod = [s[3:] for s in tabla_top10[:, 0]]
    
    # Extraer datos de población total (columnas 1:9 corresponden a 2010-2017)
    datos_totales = tabla_top10[:, 1:9].astype(float)
    
    # Generar gráfico de líneas
    GraficoLineasEvolucion(comunidades_sin_cod, datos_totales)
    
    # Insertar imagen en el HTML de R4
    AñadirImagenHtml(
        html_path="./resultados/variacionComAutonomas.html",
        imagen_path="../imagenes/evolucion_poblacion_ccaa.png",
        ancho=1000,
        alto=600
    )
    
    print("Gráfico añadido a './resultados/variacionComAutonomas.html'")
