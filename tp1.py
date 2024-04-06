from functools import reduce
import os, time


TIEMPO = 0
PESO = 1
BATALLAS = "batallas.txt"
SEPARADOR_BATALLAS = ","
HEADER_BATALLAS = "T_i,B_i"

# "generated" -> using generator.py
# DATASET_PATH = "generated"
DATASET_PATH = f"tests\\data"


#Leer el archivo txt para almacenar los valores en una lista de lista
def leer_batallas(batallas, nombre_de_archivo):
    #Abrir archivo 
    try:
        batallas_archivo = open(nombre_de_archivo, "r")
    except:
        print("Error al abrir el archivo de batallas")
        return
    
    #Archivo con header "T_i,B_i"
    next(batallas_archivo)
    
    #Recorrer el archivo y agregar en la lista
    for batalla in batallas_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        batallas.append(variables)

    #Cerrar archivo
    batallas_archivo.close()
    

def obtener_suma_ponderada(batallas):
    tiempo = [0]
    def obtener_producto(batalla):
        tiempo[0] += int(batalla[TIEMPO])
        return int(tiempo[0]) * int(batalla[PESO])
    return reduce(
        lambda b1, b2: b1 + b2,
        map(obtener_producto, batallas),
        0
    )


#Ordenar la lista segun sea la relacion t_i / b_i
def ordenar_batallas(batallas):
    return sorted(batallas, key=lambda e: int(e[TIEMPO])/int(e[PESO]))


def batallas_greedy(batallas):
    batallas_ordenadas = ordenar_batallas(batallas)
    suma_ponderada = obtener_suma_ponderada(batallas_ordenadas)
    return suma_ponderada, batallas_ordenadas


def escribir_resultados(batallas_path, batallas_ordenadas):
    solved_path = "".join(batallas_path.split(".")[0:-1]) \
        + "_solved." \
        + batallas_path.split(".")[-1]
    
    archivo_resultados = open(f"{solved_path}", "w")
    archivo_resultados.write(HEADER_BATALLAS)

    for i in range(len(batallas_ordenadas)):
        batalla = batallas_ordenadas[i]
        to_write = f"\n{batalla[0].replace("\n", "")},{batalla[1].replace("\n", "")}"
        archivo_resultados.write(to_write)
    

def tp1_batallas_solver(batallas_path):
    batallas = []
    leer_batallas(batallas, batallas_path)
    suma_ponderada, batallas_ordenadas = batallas_greedy(batallas)
    return suma_ponderada, batallas_ordenadas


def resolver_problema_batallas(data_filepath):
    start_time = time.time()
    suma_ponderada, batallas_ordenadas = tp1_batallas_solver(data_filepath)
    end_time = time.time()

    escribir_resultados(data_filepath, batallas_ordenadas)

    return suma_ponderada, (end_time - start_time)


def main():
    try:
        archivos_batallas = sorted( \
            os.listdir(DATASET_PATH), \
            key = lambda x: int(x.split(".txt")[0]) \
        )
    except:
        print("Could not find dataset folder.")
        return

    batallas = []

    for nombre_archivo in archivos_batallas:
        suma_ponderada, tiempo = resolver_problema_batallas(f"{DATASET_PATH}\\{nombre_archivo}")
        batallas.append((nombre_archivo.split(".")[0], tiempo))

        print(f"El orden de las batallas resuelto está \
              en el archivo {nombre_archivo} y la suma ponderada \
              de los tiempos de finalización es: {suma_ponderada}")
    
    print("batallas,time_in_seconds")
    for b in sorted(batallas, key=lambda x: int(x[0])):
        print(f"{b[0]},{b[1]}")


if __name__ == "__main__":
    main()
    