import os

BATALLAS = "batallas.txt"
BATALLAS_NUEVO = "nuevo.txt"
BATALLAS_ORDENADO = "ordenado.txt"
SEPARADOR_BATALLAS = ","


def promedio_batallas():
    try:
        batallas_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir el archvio de batallas")
        return
    
    try:
        batallas_aux = open(BATALLAS_NUEVO, "w")
    except:
        print("Error al abrir archivo aux")
        return
    
    for batalla in batallas_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        numerador = variables[0]
        divisor = int(variables[1])
        division = int(numerador) / int(divisor)
        batallas_aux.write(f'{numerador},{divisor},{division}'"\n")
    
    batallas_archivo.close()
    batallas_aux.close()

def ordenar_batallas():
    try:
        batallas_archivo = open(BATALLAS_NUEVO, "r")
    except:
        print("Error al abrir el archivo aux")
        return
    
    try:
        batallas_aux = open(BATALLAS_ORDENADO, "w")
    except:
        print("Error al abrir el archivo ordenado")
        return
    
    batallas = batallas_archivo.readlines()
    
    ordenadas = sorted(batallas, key = lambda parrafo: float(parrafo.split(SEPARADOR_BATALLAS)[2]))
    
    batallas_aux.writelines(ordenadas)
    
    batallas_archivo.close()
    batallas_aux.close()
    

def cambiar_nombres():
        os.rename(BATALLAS_ORDENADO, BATALLAS)
        os.remove(BATALLAS_NUEVO)
    
def minimizar_tiempos():
    try: 
        batallas_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir archivo de batallas")
        return
    
    vector_tiempos = []
    vector_peso = []
    acumulador = 0
    
    for batalla in batallas_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        vector_tiempos.append(int(variables[0]))
        vector_peso.append(int(variables[1]))
        
    vector_tiempos_sumado = []
    
    for i in range(0, len(vector_tiempos)):
        acumulador += int(vector_tiempos[i])
        vector_tiempos_sumado.append(acumulador)
        
    
    vector_final = []
    
    for i in range(0, len(vector_tiempos_sumado)):
        vector_final.append(int(vector_tiempos_sumado[i]) * int(vector_peso[i]))
    
    suma = 0
    
    for i in range(0, len(vector_final)):
        suma += int(vector_final[i])
        
    
    batallas_archivo.close()
    
    return suma
    
def devolver_orden():
    try:
        batalla_archivo = open(BATALLAS, "r")
    except:
        print("Error al abrir archivo final")
        return
    
    try:
        batalla_archivo_aux = open(BATALLAS_NUEVO, "w")
    except:
        print("Error al abrir archivo final (nuevo)")
        return
    
    for batalla in batalla_archivo:
        variables = batalla.split(SEPARADOR_BATALLAS)
        batalla_archivo_aux.write(f'{variables[0]},{variables[1]}'"\n")
    
    batalla_archivo.close()
    batalla_archivo_aux.close()
    os.rename(BATALLAS_NUEVO, BATALLAS)
    
        
def main():
    promedio_batallas()
    ordenar_batallas()
    cambiar_nombres()
    
    suma_ponderada = minimizar_tiempos()
    devolver_orden()
    print(f"El orden de las batallas que se tienen que hacer estan en el archivo batallas.txt y el tiempo es: {suma_ponderada}")
    
if __name__ == "__main__":
    main()
    