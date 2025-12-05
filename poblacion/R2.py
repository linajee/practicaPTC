import funciones as func

datos = func.LeerPaginaWeb('./entradas/variacionProvincias2011-17.htm')
comunidades_autonomas = func.LeerPaginaWeb('./entradas/comunidadesAutonomas.htm')
provincias, _, _, _ = func.LeerPoblacionProvincias('./entradas/poblacionProvinciasHM2010-17.csv')
provincias = provincias[1:]
print( comunidades_autonomas)