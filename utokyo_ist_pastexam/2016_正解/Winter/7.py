import sys

def _g(previous_value):
    return (previous_value * 1103515245 + 12345) % 2**26

def g(n):
    previous_value = 1
    for i in range(1, n):
        previous_value = _g(previous_value)
    return previous_value

def _h(previous_value):
    return (previous_value * 1103515245 + 12345) % 2**10

def h(n):
    previous_value = 1
    for i in range(1, n):
        previous_value = _h(previous_value)
    return previous_value

def find_k(n):
    hn = h(n)
    k = 1
    value = hn
    while True:
        value = _h(value)
        k += 1
        # print(f'Testing K : {k}, value {value}')
        if value == hn:
            break
    return k-1


for i in range(2, 100):
    k = find_k(i)
    print(f'K : {k}')
    val = h(i)
    val_prime = h(k+i)
    print(val, val_prime)
    val = g(i)%2**10
    val_prime = g(k+i)%2**10
    print(val, val_prime)


# from tqdm import tqdm

# for i in tqdm(range(2, 10000)):
#     assert h(i) == g(i) %2**10