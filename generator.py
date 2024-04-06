import random, os

GENERATED_DATA_PATH = "generated"

def generate_random_pairs(x):
    pairs = []
    for _ in range(x):
        pair = (random.randint(1, 999), random.randint(1, 999))
        pairs.append(pair)
    return pairs

def write_to_file(x, pairs):
    try:
        file = open(f'{GENERATED_DATA_PATH}\\{x}.txt', 'w')
    except FileNotFoundError:
        absolute_path = os.path.dirname(__file__)
        relative_path = GENERATED_DATA_PATH
        full_path = os.path.join(absolute_path, relative_path)
        os.mkdir(full_path)
        file = open(f'{GENERATED_DATA_PATH}\\{x}.txt', 'w')

    with file as f:
        f.write("T_i,B_i\n")
        p = len(pairs)
        for i in range(p):
            to_write = f"{pairs[i][0]},{pairs[i][1]}"
            if i < (p - 1):
                to_write += "\n"
            f.write(to_write)

def main():
    amounts = [   10,    50,   100,   500,  1000,   2500, 5000,
                7500, 10000, 15000, 20000, 50000, 100000        ]
    for a in amounts:
        random_pairs = generate_random_pairs(a)
        write_to_file(a, random_pairs)
        print(f"{a} pairs of random numbers have been generated and written to {a}.txt.")

if __name__ == "__main__":
    main()