# Funkcja kompresujaca tekst zgodnie z trescia polecenia


def kompresja(tekst):
    tekst = list(tekst)
    for i in range(len(tekst)):
        count = 0
        for search in range(i, len(tekst)):
            if tekst[i] == tekst[search]:
                count += 1
            else:
                break
        if count > 1:
            tekst[i + 1:i + count] = tekst[i]
            tekst[i] = str(count)

    tekst = ''.join(tekst)
    return tekst


def dekompresja(tekst_skompresowany):
    tekst = list(tekst_skompresowany)
    length = len(tekst)
    i = 0
    while i < length:
        if tekst[i].isdigit():
            digit = int(tekst[i])
            letter = tekst[i + 1]
            tekst.pop(i)
            tekst.pop(i)
            tekst.insert(i, digit * letter)
            length -= 1
        i += 1
    tekst = ''.join(tekst)
    return tekst

