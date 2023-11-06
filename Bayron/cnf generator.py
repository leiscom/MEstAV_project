import random
# Nombre del archivo
nombre_archivo = "cnf-.inp"

# Número total de líneas
num_lineas = 10000
segundo=17.09975947

# Abre el archivo en modo escritura
with open(nombre_archivo, "w") as archivo:
    archivo.write(str(num_lineas) + "\n")  # Escribe el número total de líneas
    archivo.write(str(segundo) + "\n")  # Escribe lo segundo

    for i in range(num_lineas):
    #    archivo.write("{:.8f}\n".format(17.09975947))  # Escribe el primer valor en cada línea

        # Genera valores para las posiciones y velocidades
        for j in range(6):
            valor = random.uniform(-10, 10)  # Cambia el rango si es necesario
            archivo.write("{:.10f}    ".format(valor))

        archivo.write("\n")

print(f"Se ha generado el archivo {nombre_archivo} con {num_lineas} líneas.")