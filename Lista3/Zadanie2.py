# Korzystamy z podanego wzoru, obliczajac kolejne square_sum czyli m^2 z powyższej idei.
# Root to m, czyli górna granica sumowania z podanego wzoru.


def pierwiastek(n):
    square_sum = 0
    root = 0
    while square_sum < n:
        root += 1
        square_sum += (2 * root) - 1
    if square_sum == n:
        return root
    else:
        return root - 1
