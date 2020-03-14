def romb(n):
    for first_half in range(1, n + 1):
        print(" " * (n - first_half + 1), end="")
        print("*" * ((first_half * 2) - 1), end="")
        print()

    for second_half in range(n + 1, 2 * n):
        print(" " * (second_half - n + 1), end="")
        print("*" * ((2 * n - second_half) * 2 - 1), end="")
        print()


romb(2)
romb(4)
romb(7)
