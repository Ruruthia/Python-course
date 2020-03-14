import math
from timeit import default_timer as timer


def pierwsze_imperatywna(n):
    pierwsze = [True] * (n + 1)
    pierwsze[0] = False
    pierwsze[1] = False
    i = 2
    while i * i < n:
        if pierwsze[i]:
            for j in range(i * 2, n + 1, i):
                pierwsze[j] = False
        i += 1
    wynik = []
    for i in range(n + 1):
        if pierwsze[i]:
            wynik.append(i)
    return wynik


def pierwsze_skladana(n):
    pierwsze = [i for i in range(2, n + 1)]
    zlozone = [item for i in range(2, math.ceil(math.sqrt(n))) for item in pierwsze if item % i == 0 and item != i]
    pierwsze = [item for item in pierwsze if item not in zlozone]
    return pierwsze


def pierwsze_funkcyjna(n):
    pierwsze = range(2, n + 1)
    for i in range(2, math.ceil(math.sqrt(n))):
        pierwsze = list(filter(lambda x: x % i or x == i, pierwsze))
    return pierwsze


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    is_complex = False
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0 and n != i:
            is_complex = True
    return not is_complex


start = timer()
print(*pierwsze_imperatywna(40))
end = timer()
print('Imperatywnie: ', end - start)
start = timer()
print(*pierwsze_skladana(40))
end = timer()
print('Lista składana: ', end - start)
start = timer()
print(*pierwsze_funkcyjna(40))
end = timer()
print('Funkcyjnie: ', end - start)
