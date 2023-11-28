import math
import random
import decimal

def archimedes_pi(sides):
    polygon_sides = 6
    for i in range(sides):
        polygon_sides *= 2
        apothem = 1
        side_length = math.sqrt(2 - 2 * math.sqrt(1 - apothem**2))
        perimeter = polygon_sides * side_length
    return perimeter / 2

def gregory_leibniz_pi(terms):
    pi = 0
    sign = 1
    for i in range(terms):
        pi += sign / (2 * i + 1)
        sign = -sign
    return pi * 4

def nilakantha_pi(terms):
    pi = 3
    sign = 1
    for i in range(1, terms + 1):
        pi += sign * 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
        sign = -sign
    return pi

def gauss_legendre_pi(iterations):
    a = 1
    b = 1 / math.sqrt(2)
    t = 0.25
    p = 1

    for i in range(iterations):
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next)**2
        a = a_next
        p *= 2

    pi = (a + b)**2 / (4 * t)
    return pi

def monte_carlo_pi(samples):
    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inside_circle += 1
    return 4 * inside_circle / samples

def chudnovsky_pi(iterations):
    decimal.getcontext().prec = iterations + 2
    C = 426880 * decimal.Decimal(math.sqrt(10005))
    K = decimal.Decimal(6 * math.factorial(3 * iterations) * (3 * iterations + 1) * (3 * iterations + 2))
    pi = C / K
    return pi

def main():
    print("Approximations of π using different algorithms:")
    print("Archimedes' Method:", archimedes_pi(10000))
    print("Gregory-Leibniz Series:", gregory_leibniz_pi(10000000))
    print("Nilakantha's Series:", nilakantha_pi(1000000))
    print("Gauss-Legendre Algorithm:", gauss_legendre_pi(10000))
    print("Monte Carlo Method:", monte_carlo_pi(1000000))
    print("Chudnovsky Algorithm:", chudnovsky_pi(1000))

if __name__ == "__main__":
    main()
