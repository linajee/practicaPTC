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
  total = datos[:,1:9].astype(float)
  hombres_2017 = datos[:,9:17].astype(float)
  mujeres_2017 = datos[:,17:].astype(float)

  return provincias,total, hombres_2017, mujeres_2017