import os, time, math
from tp1 import tp1_batallas_solver, escribir_resultados

DATASET_PATH = "generated"

def solve_batallas_problem(data_filepath):
    start_time = time.time()
    suma_ponderada, batallas_ordenadas = tp1_batallas_solver(data_filepath)
    end_time = time.time()

    escribir_resultados(data_filepath, batallas_ordenadas)

    return suma_ponderada, (end_time - start_time)

def main():
    try:
        dataset = os.listdir(DATASET_PATH)
    except:
        print("Could not find dataset folder.")
        return
    
    print(f"batallas_amount,time_in_seconds")

    batallas = []

    for filename in dataset:
        suma, time = solve_batallas_problem(f"{DATASET_PATH}\\{filename}")
        batallas.append((filename.split(".")[0], time))
    
    for b in sorted(batallas, key=lambda x: int(x[0])):
        print(f"{b[0]},{b[1]}")
    
if __name__ == "__main__":
    main()