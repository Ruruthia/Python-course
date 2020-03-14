import math
from timeit import default_timer as timer
from functools import reduce

import tabulate


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    is_complex = False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0 and n != i:
            is_complex = True
    return not (is_complex)


def pierwsze_imperatywna(n):
    pierwsze = [True] * (n + 1)
    pierwsze[0] = False
    pierwsze[1] = False
    i = 2
    while (i * i < n):
        if (pierwsze[i] == True):
            for j in range(i * 2, n + 1, i):
                pierwsze[j] = False
        i += 1
    wynik = []
    for i in range(n + 1):
        if pierwsze[i] == True:
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


class CountPrime:

    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        while True:
            if is_prime(num):
                self.num = num + 1
                return num
            num += 1


def pierwsze_iterator(k):
    c = CountPrime()
    val = 1
    pierwsze = []
    while val < k:
        val = next(c)
        pierwsze.append(val)
    pierwsze.pop()
    return pierwsze

def suma_dzielnikow(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma


def doskonale_iterator(k):
    n = 1
    while n < k:
        n += 1
        if n == suma_dzielnikow(n):
            yield n


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


def wypisz_czasy(fun1, fun2, fun3, fun4):
    table = [[" ", "imperatywna", "funkcyjna", "skladana", "iterator"]]
    n = 100
    while n < 100000:
        start = timer()
        fun1(n)
        end = timer()
        time1 = end - start
        start = timer()
        fun2(n)
        end = timer()
        time2 = end - start
        start = timer()
        fun3(n)
        end = timer()
        time3 = end - start
        start = timer()
        fun4(n)
        end = timer()
        time4 = end - start
        table.append(
            [n, "{:10.6f}".format(time1), "{:10.6f}".format(time2), "{:10.6f}".format(time3), "{:10.6f}".format(time4)])
        n *= 10
    print(tabulate.tabulate(table, tablefmt="grid"))


wypisz_czasy(pierwsze_imperatywna, pierwsze_skladana, pierwsze_funkcyjna, pierwsze_iterator)

wypisz_czasy(doskonale_imperatywna, doskonale_skladana, doskonale_funkcyjna, doskonale_iterator)

