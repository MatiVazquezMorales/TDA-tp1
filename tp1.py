TIEMPO = 0
PESO = 1
BATALLAS = "batallas.txt"
SEPARADOR_BATALLAS = ","
HEADER_BATALLAS = "T_i,B_i"

#Leer el archivo txt para almacenar los valores en una lista de lista
def cargarVariable(batallas, nombre_de_archivo):
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
    
def minimizar_tiempos(batallas):

    #crea un vector donde se van a almacenar los tiempos, y peso de las batallas
    vector_tiempos = []
    vector_peso = []
    
    #lee linea por linea del archivo separando los numeros de t_i y b_i por la "," y los almacena en los vectores de arriba
    for batalla in batallas:
        vector_tiempos.append(int(batalla[TIEMPO]))
        vector_peso.append(int(batalla[PESO]))
        
    #crea un vector donde se van a sumar todos los tiempos
    vector_tiempos_sumado = []
    acumulador = 0

    #se suman todos los tiempos de la forma t1, t1+t2, t1+t2+t3 ... hasta el ultimo sumando t1+t2+t_i y los almacena en el vector tiempos sumados
    for i in range(0, len(vector_tiempos)):
        acumulador += int(vector_tiempos[i])
        vector_tiempos_sumado.append(acumulador)
        
    #crea el vector donde se van a multiplicar el t_i y b_i
    vector_final = []
    
    #multiplica todos los t_i y b_i, ahora los t_i son de la forma t1, t1+t2, etc
    for i in range(0, len(vector_tiempos_sumado)):
        vector_final.append(int(vector_tiempos_sumado[i]) * int(vector_peso[i]))
    
    suma = 0
    
    #suma todos los numeros almacenados en el vector final
    for i in range(0, len(vector_final)):
        suma += int(vector_final[i])
    
    #devuelve la suma
    return suma

#Ordenar la lista segun sea la relacion t_i / b_i
def ordenar_batallas(elementos):
    return sorted(elementos, key=lambda e: int(e[TIEMPO])/int(e[PESO]))


def batallas_greedy(elementos):
    elementos_ord = ordenar_batallas(elementos)

    return minimizar_tiempos(elementos_ord), elementos_ord

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
    cargarVariable(batallas, batallas_path)
    suma_ponderada, batallas_ordenadas = batallas_greedy(batallas)
    return suma_ponderada, batallas_ordenadas

def main():
    suma_ponderada, batallas_ordenadas = tp1_batallas_solver(BATALLAS)
    escribir_resultados(BATALLAS, batallas_ordenadas)
    print(f"El orden de las batallas que se tienen que hacer estan en el archivo {BATALLAS} y el tiempo es: {suma_ponderada}")

#main
if __name__ == "__main__":
    main()
    
