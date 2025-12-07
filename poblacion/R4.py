"""
R4.py
Módulo que calcula la variación de la población por comunidades autónomas
y desagregando la información por sexos generando UNA página web con la tabla de 
resultados.

Autores: Jose Daniel Ojeda Tro & Javier Linaje Vallejo 
Fecha: 2025-12-06
"""
import numpy as np
import funciones as func
from R1 import CalcularVariacionAbsoluta, CalcularVariacionRelativa
import R2 as r2


def SepararPorSexos(sumas, num_anos):
    """
    Separa la matriz de sumas agrupadas en Hombres y Mujeres.
    
    Parámetros:
        sumas (numpy.ndarray): Matriz con poblaciones agrupadas por CCAA
        num_anos (int): Número de columnas que corresponden a cada sexo
    
    Retorna:
        tuple: (ccaa_hombres, ccaa_mujeres)
    """
    ccaa_hombres = sumas[:, :num_anos]
    ccaa_mujeres = sumas[:, num_anos:]
    
    return ccaa_hombres, ccaa_mujeres


def CrearCabecera(var_abs_hombres, var_rel_hombres, var_abs_mujeres, var_rel_mujeres):
    """
    Genera la cabecera HTML para la tabla de variaciones por sexo.
    
    Parámetros:
        var_abs_hombres (numpy.ndarray): Variación absoluta de hombres
        var_rel_hombres (numpy.ndarray): Variación relativa de hombres
        var_abs_mujeres (numpy.ndarray): Variación absoluta de mujeres
        var_rel_mujeres (numpy.ndarray): Variación relativa de mujeres
    
    Retorna:
        str: Cabecera HTML con estructura de 3 filas
    """
    cabecera = "<tr>"
    cabecera += '<th rowspan="3">CCAA</th>'
    cabecera += f'<th colspan="{(var_abs_hombres.shape[1] + var_abs_mujeres.shape[1])}" class="group-header">Variación Absoluta</th>'
    cabecera += f'<th colspan="{(var_rel_hombres.shape[1] + var_rel_mujeres.shape[1])}" class="group-header">Variación Relativa</th>'
    cabecera += "</tr>"

    cabecera += "<tr>"
    cabecera += f'<th colspan="{var_abs_hombres.shape[1]}" class="group-header">Hombres</th>'
    cabecera += f'<th colspan="{var_abs_mujeres.shape[1]}" class="group-header">Mujeres</th>'
    cabecera += f'<th colspan="{var_rel_hombres.shape[1]}" class="group-header">Hombres</th>'
    cabecera += f'<th colspan="{var_rel_mujeres.shape[1]}" class="group-header">Mujeres</th>'
    cabecera += "</tr>"

    cabecera += "<tr>"
    celdas_ano = "".join(f"<th>{ano}</th>" for ano in range(2017, 2010, -1))

    cabecera += celdas_ano * 4
    cabecera += "</tr>"
    return cabecera 


def R4():
    """
    Función principal que ejecuta el módulo R4.
    
    Genera un archivo HTML con las variaciones absolutas y relativas
    de población por Comunidades Autónomas, desagregadas por sexo.
    Parámetros:
        None
    Retorna:
        None
    """
    
    ruta_csv = "./entradas/poblacionProvinciasHM2010-17.csv"
    provincias, _, poblacion_hombres, poblacion_mujeres = func.LeerPoblacionProvincias(ruta_csv)
    
    provincias, tabla = r2.QuitarFilaTotales(provincias, None, poblacion_hombres, poblacion_mujeres)
    
    diccionario_comunidades = r2.DatosComuniadesAutonomasProvincias()
    comunidades, sumas = r2.AgruparProvinciasPorComunidadAutonoma(provincias, tabla, diccionario_comunidades)

    num_anos = poblacion_hombres.shape[1]

    ccaa_hombres, ccaa_mujeres = SepararPorSexos(sumas, num_anos)

    var_abs_hombres = CalcularVariacionAbsoluta(ccaa_hombres)
    var_rel_hombres = CalcularVariacionRelativa(ccaa_hombres, var_abs_hombres)

    var_abs_mujeres = CalcularVariacionAbsoluta(ccaa_mujeres)
    var_rel_mujeres = CalcularVariacionRelativa(ccaa_mujeres, var_abs_mujeres)

    datos = np.hstack((
        comunidades.reshape(-1, 1),
        var_abs_hombres,
        var_abs_mujeres,
        var_rel_hombres,
        var_rel_mujeres
    ))
    
    cabecera = CrearCabecera(var_abs_hombres, var_rel_hombres, var_abs_mujeres, var_rel_mujeres)
    
    func.GenerarHtml(
        titulo="Variación de Población por Comunidades Autónomas y Sexos (2011-2017)",
        cabecera=cabecera,
        datos=datos,
        salida="./resultados/variacionComAutonomas.html"
    )

    print("Página HTML generada en './resultados/variacionComAutonomas.html'")