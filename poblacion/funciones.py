import csv, numpy as np
from bs4 import BeautifulSoup


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
        paginaHTML += f"<td style='width:100px;'>{datos[i][0]}</td>"
        
        for j in range(1,datos.shape[1]):
            valor = datos[i][j]
            valor = FormatearNumero(valor, 2)

            paginaHTML += f"<td>{valor}</td>"
            
        paginaHTML += "</tr>"
        
    paginaHTML += "</table></body></html>"
    #print("Tabla HTML generada.")
    # Escritura en fichero
    with open(salida, "w", encoding="utf8") as archivo:
        archivo.write(paginaHTML)
  
    archivo.close()


def FormatearNumero(numero, decimales=2):
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

  
def GenerarEstiloCss():
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
    table th:first-child,
    table td:first-child {
        text-align: center;
        width: 100px;
        white-space: nowrap;
    }
    """
    with open("./resultados/estilo.css", "w", encoding="utf8") as f:
        f.write(contenido_css)


def LeerPaginaWeb(fichero):      
    archivo = open(fichero, 'r', encoding="utf8")
    comString = archivo.read()
    archivo.close()

    # --- Usando BeautifulSoup ---
    soup = BeautifulSoup(comString, 'html.parser')

    # Leer TD
    td_soup = soup.find_all('td')
    celdas = [td.get_text() for td in td_soup]


    # Puedes elegir qué devolver:
    return celdas