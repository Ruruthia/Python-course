import math
from timeit import default_timer as timer
from functools import reduce


def doskonale_imperatywna(n):
    doskonale = []
    i = 1
    sum = 1
    while (sum < n):
        sum += 2 ** i
        # UWAGA: w teście z treści zadania jest błąd (8128 jest zdecydowanie większe niż 1000), tu koryguje go
        # warunek sum*2**i<=n, bez niego wynik jest jak w zadaniu
        if is_prime(sum) and sum * 2 ** i <= n:
            doskonale.append(sum * 2 ** i)
        i += 1
    return doskonale


def doskonale_skladana(n):
    potegi = [2 ** i for i in range(0, math.ceil(math.log2(n)))]
    sumy = [(potegi[i - 1], sum(potegi[0:i])) for i in range(1, len(potegi))]
    pierwsze = [item for item in sumy if is_prime(item[1])]
    doskonale = [item[0] * item[1] for item in pierwsze if item[0] * item[1] <= n]
    return doskonale


def doskonale_funkcyjna(n):
    wykladniki = range(math.ceil(math.log2(n)))
    potegi = list(map(lambda x: 2 ** x, wykladniki))
    sumy = []
    for i in range(1, len(potegi)):
        sumy.append((reduce(lambda x, y: x + y, potegi[0:i], 0), i - 1))
    pierwsze = list(filter(lambda x: is_prime(x[0]), sumy))
    doskonale = list(map(lambda x: x[0] * 2 ** x[1], pierwsze))
    doskonale = list(filter(lambda x: x <= n, doskonale))
    return doskonale


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
print(*doskonale_imperatywna(10000))
end = timer()
print('Imperatywnie: ', end - start)
start = timer()
print(*doskonale_skladana(10000))
end = timer()
print('Lista składana: ', end - start)
start = timer()
print(*doskonale_funkcyjna(10000))
end = timer()
print('Funkcyjnie: ', end - start)
