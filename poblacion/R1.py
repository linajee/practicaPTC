"""
R1.py
Módulo que calcula la variación de la población por provincias
y generando UNA página web con la tabla de resultados

Autores: Jose Daniel Ojeda Tro & Javier Linaje Vallejo 
Fecha: 2025-12-05
"""
import numpy as np
import funciones as func


def calcular_variacion_absoluta(poblacion_total):
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


def calcular_variacion_relativa(poblacion_total, variacion_absoluta):
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


def generar_estilo_css():
    """
    Genera el archivo CSS para la tabla.
    
    Parametros:
        None
    
    Retorna:
        None
    """
    contenido_css = """
    table {
        border-collapse: collapse;
        width: 100%;
        font-family: Arial, Helvetica, sans-serif;
    }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: center;
        font-size: 12px;
    }
    th {
        background-color: #ffffff;
        font-weight: bold;
    }
    /* Estilo para las cabeceras agrupadas */
    th.group-header {
        background-color: #f2f2f2;
    }
    """
    with open("./resultados/estilo.css", "w", encoding="utf8") as f:
        f.write(contenido_css)



def CrearCabecera(variacion_absoluta, variacion_relativa):
    cabecera = "<tr>"
    cabecera += '<th rowspan="2">Provincia</th>'
    cabecera += f'<th colspan="{variacion_absoluta.shape[1]}" class="group-header">Variación absoluta</th>'
    cabecera += f'<th colspan="{variacion_relativa.shape[1]}" class="group-header">Variación relativa</th>'
    cabecera += "</tr>"

    # Fila 2: Años individuales
    cabecera += "<tr>"
    # Años para Variación Absoluta
    for ano in range(2017, 2010, -1):
        cabecera += f"<th>{ano}</th>"
    # Años para Variación Relativa
    for ano in range(2017, 2010, -1):
        cabecera += f"<th>{ano}</th>"
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

    generar_estilo_css()
    ruta_csv = "./entradas/poblacionProvinciasHM2010-17.csv"
    provincias, poblacion_total, _ , _ = func.LeerPoblacionProvincias(ruta_csv)
    
    variacion_absoluta = calcular_variacion_absoluta(poblacion_total)
    variacion_relativa = calcular_variacion_relativa(poblacion_total, variacion_absoluta)

    datos = np.hstack((provincias.reshape(-1,1), variacion_absoluta, variacion_relativa))

    cabecera =  CrearCabecera(variacion_absoluta, variacion_relativa)
    
    func.GenerarHtml(
        titulo="Variación de Población por Provincias (2011-2017)",
        cabecera=cabecera,
        datos=datos,
        salida="./resultados/variacionProvincias.html"
    )
    print("Página HTML generada en './resultados/variacionProvincias.html'")
        


R1()
    