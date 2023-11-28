from math import sqrt
from Big_O_notation import execution_timer
import time
import cwd
cwd.cwd(".txt")

def isprime(x: int) -> bool:
    if x < 2:
        return False
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0: return False
    return True


def solution(n: int, prime_string: str) -> str:
    return prime_string[n:n+5]

if __name__ == "__main__":
    prime_string = "".join([str(x) for x in range(10005) if isprime(x)])
    solution = "".join([f"Nr {x+1}: {solution(x, prime_string)} " for x in range(10000)])

    with open("solution.txt", "w") as txt:
        txt.write(solution)

