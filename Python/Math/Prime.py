from math import sqrt
import numpy as np
import sys

sys.set_int_max_str_digits(1000)

def isprime(x: int) -> bool:
    if x < 2:
        return False
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0:
            return False
    return True
    
def primes(start: int, finish: int) -> None:   
    for x in range(start, finish):
        if isprime(x):
            print(x)

if __name__ == "__main__":
    print(isprime(2221))

    
    