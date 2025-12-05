import csv, numpy as np

def LectorCsv(ruta, delimitador : str, ini : str, fin : str): 

  if len(delimitador) !=1:
    raise ValueError("El delimitador debe ser un solo caracter")

  lista_csv = []
  escribir = False
  
  with open(ruta, encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo, delimiter=delimitador)
    for reg in entrada:
        if reg[-1] == '':
          reg = reg[:-1]
        if fin in reg:
          escribir = False
        if ini in reg or escribir:
          escribir = True
          lista_csv.append(reg)
        

  np_csv = np.array(lista_csv)  
  return np_csv


def LeerPoblacionProvincias(ruta : str):

  datos = LectorCsv(
      ruta=ruta,
      delimitador=";",
      ini="Total Nacional",
      fin="Notas:"
  )

  provincias = datos[:,0]
  total = np.round(datos[:,1:9].astype(float),2)
  hombres_2017 = np.round(datos[:,9:17].astype(float))
  mujeres_2017 = np.round(datos[:,17:].astype(float))

  return provincias,total, hombres_2017, mujeres_2017


def GenerarHtml(titulo, cabecera, datos, salida):
    """
    Genera una tabla HTML con la variación absoluta y relativa de la población por provincias

    Parámetros:
        provincias (numpy.ndarray): Array con las provincias
        variacion_absoluta (numpy.ndarray): Array con la variación absoluta de la población por provincias
        variacion_relativa (numpy.ndarray): Array con la variación relativa de la población por provincias

    Retorna:
        None
    """
    
    # Construcción del contenido HTML usando concatenación de strings
    paginaHTML = """<!DOCTYPE html><html>
    <head><title>Tabla de Variación de Población</title>
    <link rel="stylesheet" href="estilo.css">
    <meta charset="utf8"></head>
    <body>
    <h1>{}</h1>
    <table>
    """.format(titulo)

    
    # Fila 1: Cabeceras Agrupadas
    paginaHTML += cabecera
    
    for i in range(datos.shape[0]):
        paginaHTML += "<tr>"
        paginaHTML += f"<td style='text-align: left;'>{datos[i][0]}</td>"
        
        for j in range(1,datos.shape[1]):
            valor = datos[i][j]
            valor = formatear_numero(valor, 2)

            paginaHTML += f"<td>{valor}</td>"
            
        paginaHTML += "</tr>"
        
    paginaHTML += "</table></body></html>"
    #print("Tabla HTML generada.")
    # Escritura en fichero
    with open(salida, "w", encoding="utf8") as archivo:
        archivo.write(paginaHTML)
  
    archivo.close()


def formatear_numero(numero, decimales=2):
    """
    Formatea un número al estilo español

    Parametros:
        numero (float): Número a formatear
        decimales (int): Número de decimales

    Retorna:
        str: Número formateado  
    """
  
    try:
      # Formateamos primero con el estándar inglés (coma para miles, punto para decimales)
      numero = float(numero)
      formato = f"{{:,.{decimales}f}}"
      s = formato.format(numero)
      
      # Reemplazamos temporalmente la coma por un marcador, el punto por coma, y el marcador por punto
      s = s.replace(",", "X").replace(".", ",").replace("X", ".")
      return s
    except:
      return numero