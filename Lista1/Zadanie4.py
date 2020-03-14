def xor(message, key):
    for letter in message:
        print(chr(ord(letter) ^ key), end="")
    print()


def dexor(code, key):
    for letter in code:
        print(chr(ord(letter) ^ key), end="")
    print()


xor("Python", 7)
dexor("W~sohi", 7)