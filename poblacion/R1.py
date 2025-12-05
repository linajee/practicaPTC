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


def formatear_numero(numero, decimales=2):
    """
    Formatea un número al estilo español

    Parametros:
        numero (float): Número a formatear
        decimales (int): Número de decimales

    Retorna:
        str: Número formateado  
    """
    # Formateamos primero con el estándar inglés (coma para miles, punto para decimales)
    formato = f"{{:,.{decimales}f}}"
    s = formato.format(numero)
    
    # Reemplazamos temporalmente la coma por un marcador, el punto por coma, y el marcador por punto
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def generar_tabla_html(provincias, variacion_absoluta, variacion_relativa):
    """
    Genera una tabla HTML con la variación absoluta y relativa de la población por provincias

    Parámetros:
        provincias (numpy.ndarray): Array con las provincias
        variacion_absoluta (numpy.ndarray): Array con la variación absoluta de la población por provincias
        variacion_relativa (numpy.ndarray): Array con la variación relativa de la población por provincias

    Retorna:
        None
    """
    generar_estilo_css()
    
    # Años correspondientes a las columnas de variación (2017 a 2011)
    anos = list(range(2017, 2010, -1))
    num_anos = len(anos)
    
    # Construcción del contenido HTML usando concatenación de strings
    paginaHTML = """<!DOCTYPE html><html>
<head><title>Tabla de Variación de Población</title>
<link rel="stylesheet" href="estilo.css">
<meta charset="utf8"></head>
<body>
<h1>Variación de Población por Provincias (2011-2017)</h1>
<table>
"""
    
    # Fila 1: Cabeceras Agrupadas
    paginaHTML += "<tr>"
    paginaHTML += '<th rowspan="2">Provincia</th>'
    paginaHTML += f'<th colspan="{num_anos}" class="group-header">Variación absoluta</th>'
    paginaHTML += f'<th colspan="{num_anos}" class="group-header">Variación relativa</th>'
    paginaHTML += "</tr>"
    
    # Fila 2: Años individuales
    paginaHTML += "<tr>"
    # Años para Variación Absoluta
    for ano in anos:
        paginaHTML += f"<th>{ano}</th>"
    # Años para Variación Relativa
    for ano in anos:
        paginaHTML += f"<th>{ano}</th>"
    paginaHTML += "</tr>"
    
    # Filas de datos
    num_provincias = len(provincias)
    
    for i in range(num_provincias):
        paginaHTML += "<tr>"
        paginaHTML += f"<td style='text-align: left;'>{provincias[i]}</td>"
        
        # Datos Variación Absoluta
        for j in range(num_anos):
            valor = variacion_absoluta[i, j]
            paginaHTML += f"<td>{formatear_numero(valor, 2)}</td>"
        
        # Datos Variación Relativa
        for j in range(num_anos):
            valor = variacion_relativa[i, j]
            paginaHTML += f"<td>{formatear_numero(valor, 2)}</td>"
            
        paginaHTML += "</tr>"
        
    paginaHTML += "</table></body></html>"
    
    # Escritura en fichero
    with open("./resultados/variacionProvincias.html", "w", encoding="utf8") as archivo:
        archivo.write(paginaHTML)


def R1():
    """
    Función principal que ejecuta el módulo R1

    Parámetros:
        None

    Retorna:
        None
    """
    ruta_csv = "./entradas/poblacionProvinciasHM2010-17.csv"
    provincias, poblacion_total, poblacion_hombres, poblacion_mujeres = func.LeerPoblacionProvincias(ruta_csv)
    
    variacion_absoluta = calcular_variacion_absoluta(poblacion_total)
    variacion_relativa = calcular_variacion_relativa(poblacion_total, variacion_absoluta)
    
    generar_tabla_html(provincias, variacion_absoluta, variacion_relativa)