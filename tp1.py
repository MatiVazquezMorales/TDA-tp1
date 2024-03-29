import os

BATALLAS = "batallas.txt"
BATALLAS_NUEVO = "nuevo.txt"
BATALLAS_ORDENADO = "ordenado.txt"
SEPARADOR_BATALLAS = ","

#calcula la division entre t_i y b_i, haciendo t_i/b_i y lo escribe en un nuevo archivo txt
def promedio_batallas():
    #abre el archivo batallas.txt en modo lector
    try:
        batallas_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir el archvio de batallas")
        return
    
    #abre el archivo auxiliar para poder escribir el promedio
    try:
        batallas_aux = open(BATALLAS_NUEVO, "w")
    except:
        print("Error al abrir archivo aux")
        return
    
    #va linea por linea (parrafo) del archivo batallas.txt, realiza la division y escribe en el archivo auxiliar todos los t_i, b_i y el resultado de la division
    for batalla in batallas_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        numerador = variables[0]
        divisor = int(variables[1])
        division = int(numerador) / int(divisor)
        batallas_aux.write(f'{numerador},{divisor},{division}'"\n")
    
    #cierra los archivos
    batallas_archivo.close()
    batallas_aux.close()

#ordena todas las batallas de menor a mayor por el resultado de la division entre t_i y b_i
def ordenar_batallas():
    #abre el archivo nuevo donde estan escritos todos los t_i, b_i y los resultados
    try:
        batallas_archivo = open(BATALLAS_NUEVO, "r")
    except:
        print("Error al abrir el archivo aux")
        return
    
    #abre un archivo nuevo para poder ordenar todos las batallas por el resultado de la division
    try:
        batallas_aux = open(BATALLAS_ORDENADO, "w")
    except:
        print("Error al abrir el archivo ordenado")
        return
    
    #lee las lineas del archivo desordenado
    batallas = batallas_archivo.readlines()
    
    #ordena todas las batallas por el resultado de la division
    ordenadas = sorted(batallas, key = lambda parrafo: float(parrafo.split(SEPARADOR_BATALLAS)[2]))
    
    #escribe las batallas ordenadas por ese resultado
    batallas_aux.writelines(ordenadas)
    
    #cierra los archivos
    batallas_archivo.close()
    batallas_aux.close()
    

#cambia de nombre los archivos y borra uno, asi queda un solo archivo batallas.txt
def cambiar_nombres():
        os.rename(BATALLAS_ORDENADO, BATALLAS)
        os.remove(BATALLAS_NUEVO)

#realiza el calculo para saber cual es el resultado de la suma minima
def minimizar_tiempos():
    #abre el archivo batallas.txt
    try: 
        batallas_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir archivo de batallas")
        return
    
    #crea un vector donde se van a almacenar los tiempos, y peso de las batallas
    vector_tiempos = []
    vector_peso = []
    
    #lee linea por linea del archivo separando los numeros de t_i y b_i por la "," y los almacena en los vectores de arriba
    for batalla in batallas_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        vector_tiempos.append(int(variables[0]))
        vector_peso.append(int(variables[1]))
        
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
        
    #cierra los archivos
    batallas_archivo.close()
    
    #devuelve la suma
    return suma

#borra el resultado de la division entre t_i y b_i quedando el orden que se deben hacer las batallas en el archivo batallas.txt
def devolver_orden():
    #abre el achivos batallas.txt
    try:
        batalla_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir archivo final")
        return
    
    #abre un nuevo archivo donde van a estar almacenado solo el orden con el t_i y b_i
    try:
        batalla_archivo_aux = open(BATALLAS_NUEVO, "w")
    except:
        print("Error al abrir archivo final (nuevo)")
        return
    
    #linea por linea separa t_i , b_i y el resultado de la division y escribe solo el t_i y b_i de las batallas 
    for batalla in batalla_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        batalla_archivo_aux.write(f'{variables[0]},{variables[1]}'"\n")
    
    #cierra los archivos y le cambia el nombre asi queda un solo batallas.txt
    batalla_archivo.close()
    batalla_archivo_aux.close()
    os.rename(BATALLAS_NUEVO, BATALLAS)
    
#main
def main():
    promedio_batallas()
    ordenar_batallas()
    cambiar_nombres()
    
    suma_ponderada = minimizar_tiempos()
    devolver_orden()
    print(f"El orden de las batallas que se tienen que hacer estan en el archivo batallas.txt y el tiempo es: {suma_ponderada}")
    
#main
if __name__ == "__main__":
    main()
    