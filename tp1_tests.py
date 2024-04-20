from tp1 import tp1_batallas_solver

# (amount, expected_sum)
amounts = [
    (10,309600),
    (50,5218700),
    (100,780025365),
    (1000,74329021942),
    (5000,1830026958236),
    (10000,7245315862869),
    (100000,728684685661017)
]

for a in amounts:
    sum_, _ = tp1_batallas_solver(f"tests\\data\\{a[0]}.txt")
    print(f"sum for value {a}: {sum_} - ", end="")
    assert sum_ == a[1]
    print("OK!")