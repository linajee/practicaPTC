import funciones as func
import numpy as np

def AgruparProvinciasPorComunidadAutonoma(provincias, poblaciones, diccionario_comunidades):

    resultado = np.zeros((len(diccionario_comunidades), poblaciones.shape[1]))
    
    for i, comunidad in enumerate(diccionario_comunidades): 
        for j in range(len(provincias)):
            if provincias[j] in diccionario_comunidades[comunidad]:
                resultado[i] += poblaciones[j]
    return resultado
            

def DiccionarioComunidadProvincia(datos):
    comunidades_autonomas = {}
    i = 0
    
    while i < len(datos):
        comunidad = datos[i]
        provincia = datos[i+1]

        if comunidad not in comunidades_autonomas:
            
            comunidades_autonomas[comunidad] = []
        comunidades_autonomas[comunidad].append(provincia)

        i += 2  # Saltar a la siguiente comunidad autónoma
    
    return comunidades_autonomas

def CrearCabecera(total, hombres, mujeres): 
    cabecera = "<tr>"
    cabecera += '<th rowspan="2" style="width:100px;">CCAA</th>'
    cabecera += f'<th colspan="{total.shape[1]}" class="group-header">Total</th>'
    cabecera += f'<th colspan="{hombres.shape[1]}" class="group-header">Hombre</th>'
    cabecera += f'<th colspan="{mujeres.shape[1]}" class="group-header">Mujer</th>'
    cabecera += "</tr>"

    # Fila 2: Años individuales
    cabecera += "<tr>"
    celdas_ano = "".join([f"<th>{ano}</th>" for ano in range(2017, 2009, -1)])
    cabecera += celdas_ano * 3
    cabecera += "</tr>"

    return cabecera 

def DatosComuniadesAutonomasProvincias():
  # Leer datos de la página web
  datos = func.LeerPaginaWeb('./entradas/comunidadAutonoma-Provincia.htm')

  # Limpiar y organizar los datos
  datos = [d for d in datos if d != '' and d != 'Ciudades    Autónomas:']
  comunidades_provincias = [datos[i] + " " + datos[i+1] for i in range(0, len(datos), 2)]
  # Crear diccionario de comunidades autónomas y provincias
  diccionario_comunidades = DiccionarioComunidadProvincia(comunidades_provincias)

  return diccionario_comunidades

def R2():

  func.GenerarEstiloCss()
  # Leer datos de población 
  provincias, total, p_hombres, p_mujeres = func.LeerPoblacionProvincias('./entradas/poblacionProvinciasHM2010-17.csv')

  # Quitar la fila de totales
  provincias = provincias[1:]
  tabla = np.hstack((total, p_hombres, p_mujeres))
  tabla = tabla[1:,:] 

  diccionario_comunidades = DatosComuniadesAutonomasProvincias()

  # Sumar poblaciones por comunidad autónoma
  sumas = AgruparProvinciasPorComunidadAutonoma(provincias, tabla, diccionario_comunidades)
  comunidades = np.array(list(diccionario_comunidades.keys()))

  tabla = np.column_stack((comunidades, sumas))
  cabecera = CrearCabecera(total, p_hombres, p_mujeres)




  func.GenerarHtml(
      titulo="Poblacion total de las comunidades autónomas (2011-2017)",
      cabecera=cabecera,
      datos=tabla,
      salida="./resultados/comunidadesAutonomas.html"
  )
  print("Página HTML generada en './resultados/comunidadesAutonomas.html'")

