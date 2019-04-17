import sys
from functools import lru_cache

@lru_cache
def _g(previous_value):
    return (previous_value * 1103515245 + 12345) % 2**24

def g(n):
    previous_value = 1
    for i in range(1, n):
        previous_value = _g(previous_value)
    return previous_value

def find_k(n):
    gn = g(n)
    k = 1
    value = gn
    while True:
        value = _g(value)
        k += 1
        # print(f'Testing K : {k}, value {value}')
        if value == gn:
            break
    return k-1



k = find_k(2)
val = g(2)
val_prime = g(k+2)
# assert val == val_prime

print(k)


