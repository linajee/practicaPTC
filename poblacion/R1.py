"""
R1.py
Módulo que calcula la variación de la población por provincias
y generando UNA página web con la tabla de resultados

Autores: Jose Daniel Ojeda Tro & Javier Linaje Vallejo 
Fecha: 2025-12-05
"""
import numpy as np
import funciones as func


def CalcularVariacionAbsoluta(poblacion_total):
    """
    Calcula la variación absoluta de la población por provincias

    Parámetros:
        poblacion_total (numpy.ndarray): Array con la población total por provincias

    Retorna:
        numpy.ndarray: Array con la variación absoluta de la población por provincias
    """    
    # variacion_absoluta 2017 = poblacion 2017 - poblacion 2016
    # [:, :-1] = Para todas las provincias y todos los años menos 2010 (2017-2011)
    # [:, 1:] = Para todas las provincias y todos los años menos 2017 (2016-2010)
    return poblacion_total[:, :-1] - poblacion_total[:, 1:]


def CalcularVariacionRelativa(poblacion_total, variacion_absoluta):
    """
    Calcula la variación relativa de la población por provincias

    Parámetros:
        poblacion_total (numpy.ndarray): Array con la población total por provincias
        variacion_absoluta (numpy.ndarray): Array con la variación absoluta de la población por provincias

    Retorna:
        numpy.ndarray: Array con la variación relativa de la población por provincias
    """
    # variacion_relativa 2017 = (variacion_absoluta 2017 / poblacion 2016) * 100
    # [:, 1:] = Para todas las provincias y todos los años menos 2017 (2016-2010)
    return variacion_absoluta / poblacion_total[:, 1:] * 100


def CrearCabecera(variacion_absoluta, variacion_relativa):
    """
    Genera la cabecera HTML para la tabla de variaciones de población.
    
    Parámetros:
        variacion_absoluta (numpy.ndarray): Array con la variación absoluta
        variacion_relativa (numpy.ndarray): Array con la variación relativa
    
    Retorna:
        str: Código HTML de la cabecera de la tabla
    """
    cabecera = "<tr>"
    cabecera += '<th rowspan="2">Provincia</th>'
    cabecera += f'<th colspan="{variacion_absoluta.shape[1]}" class="group-header">Variación absoluta</th>'
    cabecera += f'<th colspan="{variacion_relativa.shape[1]}" class="group-header">Variación relativa</th>'
    cabecera += "</tr>"

    cabecera += "<tr>"

    celdas_ano = "".join(f"<th>{ano}</th>" for ano in range(2017, 2010, -1))
    cabecera += celdas_ano
    cabecera += celdas_ano

    cabecera += "</tr>"

    return cabecera 


def R1():
    """
    Función principal que ejecuta el módulo R1

    Parámetros:
        None

    Retorna:
        None
    """
    
    ruta_csv = "./entradas/poblacionProvinciasHM2010-17.csv"
    provincias, poblacion_total, _ , _ = func.LeerPoblacionProvincias(ruta_csv)
    
    variacion_absoluta = CalcularVariacionAbsoluta(poblacion_total)
    variacion_relativa = CalcularVariacionRelativa(poblacion_total, variacion_absoluta)

    datos = np.hstack((provincias.reshape(-1,1), variacion_absoluta, variacion_relativa))

    cabecera =  CrearCabecera(variacion_absoluta, variacion_relativa)
    
    func.GenerarHtml(
        titulo="Variación de Población por Provincias (2011-2017)",
        cabecera=cabecera,
        datos=datos,
        salida="./resultados/variacionProvincias.html"
    )

    print("Página HTML generada en './resultados/variacionProvincias.html'")
        
