import sys


def min_coins(coins, V):
    m = len(coins)
    table = [[0, 0] for i in range(V + 1)]
    table[0] = [0, 0]
    for i in range(1, V + 1):
        table[i][0] = sys.maxsize
    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]][
                    0]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i][0]):
                    table[i] = [sub_res + 1, coins[j]]
    coins_count = table[V][0]
    denominals = [0] * (table[V][0])
    denominals[0] = table[V][1]
    for i in range(1, table[V][0]):
        denominals[i] = (table[V - table[V][1]][1])
        V -= table[V][1]
    return coins_count, denominals


def print_coins(coins, coins_count, denominals):
    print(f'Potrzeba {coins_count} monet. Nominaly: ')
    for item in coins:
        if denominals.count(item) != 0:
            print(f'{item}zl x {denominals.count(item)}')


coins = [1, 2, 5, 10]
coins_count, denominals = min_coins(coins, 123)
print_coins(coins, coins_count, denominals)
