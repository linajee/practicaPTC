from funciones import LeerPoblacionProvincias

provincias, total, hombres, mujeres = LeerPoblacionProvincias("./entradas/poblacionProvinciasHM2010-17.csv")

print("Provincias: {} ...\n".format( provincias[0:2]))
print("Total Poblacion por provincias:\n", total[0:2])
print("\nHombres por provincias:\n", hombres[0:2])  
print("\nMujeres por provincias:\n", mujeres[0:2]) 