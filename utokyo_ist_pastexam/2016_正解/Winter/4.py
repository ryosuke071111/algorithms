import sys
from functools import lru_cache
from time import time

def _f(previous_value):
    return (previous_value * 161 +  2457) % 2**24

def f(n):
    previous_value = 1
    for i in range(1, n):
        previous_value = _f(previous_value)
    return previous_value

start = time()
value= f(10000000)
duration = time() - start 
print(value)
print(duration)


