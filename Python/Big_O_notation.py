import time
from functools import wraps
from itertools import chain, combinations
import random as rd
import numpy as np

def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        total_time = end - start
        print(f'Function {func.__name__} Took {total_time} seconds')
        return result
    return wrapper

@execution_timer
def add_one(array: np.ndarray) -> None:
    array = [x+1 for x in array]

@execution_timer
def find_element_3(array: np.ndarray) -> None:
    array = array[3]

@execution_timer
def square_array(array: np.ndarray) -> None:
    array = [x for x in array for x in array]

@execution_timer
def powerset(array: np.ndarray) -> None:
    array = list(chain.from_iterable(combinations(array, r) for r in np.arange(len(array)+1)))

@execution_timer
def binary_search(array: np.ndarray) -> None:
    item = rd.choice(array)
    left, right = 0, len(array)-1

    while left <= right:
        middle = left + (right - left)//2
        if item == array[middle]:
            break
        elif array[middle] < item:
           left = middle + 1
        else:
           right = middle - 1
if __name__ == "__main__":
    print("""\nBig O Notation, a program by Mihail Zabolotnic
        (michail.zabolotnic@gmail.com)""")
    
    n = None

    while not isinstance(n, int):
        try:
            n = int(input("Please input your desired range as a number: "))
            
        except ValueError:
            n = int(input("Please input your desired range as a number: "))
    array = np.arange(n)
    
    find_element_3(array)
    binary_search(array)
    add_one(array)
    square_array(array)
    powerset(array)