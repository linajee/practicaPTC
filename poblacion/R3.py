import matplotlib.pyplot as plt
import numpy as np
import funciones as func
from R2 import TablaPoblacionMediaCCAA

def GraficaBarrasPares(nombres, par1, par2):
    """
    Genera una gráfica de barras que muestra la población por sexo en las CCAA para el año 2017.
    La gráfica se guarda en un archivo PNG.
    """
    plt.figure("lineal")
    plt.title("Polación por sexo en el año 2017 (CCAA)")

    x = np.arange(len(nombres))
    ancho = 0.20
    plt.bar(x - ancho/2, par1, width=ancho, label='Hombres', color='blue')
    plt.bar(x + ancho/2, par2, width=ancho, label='Mujeres', color='red')

    plt.xticks(x, nombres, rotation=80, ha='right')  # cada grupo tiene un nombre

    plt.legend()
    plt.tight_layout()
    plt.savefig('./imagenes/poblacion_por_sexo_ccaa.png')

def AñadirImagenHtml(html_path, imagen_path, ancho=None, alto=None):
    """
    Añade una imagen al final de un HTML existente, justo antes del cierre del body.

    Parámetros:
        html_path (str): Ruta del archivo HTML existente.
        imagen_path (str): Ruta de la imagen que se quiere insertar.
        ancho (int, opcional): Ancho de la imagen en píxeles.
        alto (int, opcional): Alto de la imagen en píxeles.
    """
    # Leer el HTML existente
    with open(html_path, "r", encoding="utf8") as f:
        html_content = f.read()
    
    # Crear el tag de la imagen con atributos opcionales
    atributos = ""
    if ancho:
        atributos += f' width="{ancho}"'
    if alto:
        atributos += f' height="{alto}"'
    
    img_tag = f'<img src="{imagen_path}"{atributos} style="display:block; margin:20px auto;">\n'
    
    # Insertar la imagen justo antes de </body>
    if "</body>" in html_content:
        html_content = html_content.replace("</body>", img_tag + "</body>")
    else:
        # Si no hay body, añadir al final
        html_content += img_tag
    
    # Guardar el HTML modificado
    with open(html_path, "w", encoding="utf8") as f:
        f.write(html_content)

def R3():
    """
    Función principal que ejecuta el módulo R4

    Parámetros:
        Ninguno

    Retorna:
        Ninguno
    """
    provincias, total, p_hombres, p_mujeres = func.LeerPoblacionProvincias('./entradas/poblacionProvinciasHM2010-17.csv')
    tabla = TablaPoblacionMediaCCAA(provincias, total, p_hombres, p_mujeres)

    #Calcular las 10 CCAA con mayor población media
    medias = np.mean(tabla[:, 1:9].astype(float), axis=1)
    orden = np.argsort(medias)[-10:][::-1]

    tabla = tabla[orden]

    # Quitamos los codigos de las comunidades autónomas
    comunidades_sin_cod = list([s[3:] for s in tabla[:, 0]])


    diccionario = {str(comunidades_sin_cod[i]): {'Hombres': float(tabla[i][9]),'Mujeres' : float(tabla[i][17])} for i in range(len(tabla))}


    hombres = [diccionario[com]['Hombres'] for com in comunidades_sin_cod]
    mujeres = [diccionario[com]['Mujeres'] for com in comunidades_sin_cod]

    GraficaBarrasPares(comunidades_sin_cod, hombres, mujeres)

    AñadirImagenHtml(
        html_path="./resultados/poblacionComAutonomas.html",
        imagen_path="../imagenes/poblacion_por_sexo_ccaa.png",
        ancho=800,
        alto=600
    )