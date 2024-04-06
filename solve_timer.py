import os, time
from tp1 import tp1_batallas_solver

DATASET_PATH = "generated"

def solve_batallas_problem(dataset_filepath):
    start_time = time.time()
    suma_ponderada = tp1_batallas_solver(dataset_filepath)
    end_time = time.time()
    return suma_ponderada, (end_time - start_time)

def main():
    try:
        dataset = os.listdir(DATASET_PATH)
    except:
        print("Could not find generated data folder. First run generator.py")
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