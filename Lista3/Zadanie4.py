import random

# Funkcja upraszcza zdanie według sposobu opisanego w treści zadania. Nie zostało sprecyzowane jak traktować przecinki.
# Ja przyjęłam, że są one częścią słowa, w przeciwieństwie do ., ! i ?. W przypadku testu z Panem Tadeuszem utwór kończy sie liczbą.
# W takiej sytuacji zmieniam ja na kropke dla estetyki.

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    slowa = tekst.split()
    ostatnie_slowo = slowa[len(slowa) - 1]
    if ostatnie_slowo[len(ostatnie_slowo) - 1] is "." or ostatnie_slowo[len(ostatnie_slowo) - 1] is "!" or \
            ostatnie_slowo[len(ostatnie_slowo) - 1] is "?":
        zakonczenie = ostatnie_slowo[len(ostatnie_slowo) - 1]
    else:
        zakonczenie = '.'
    slowa = [slowo for slowo in slowa if len(slowo) <= dl_slowa]
    for i in range(len(slowa) - liczba_slow):
        slowa.pop(random.randint(0, len(slowa) - 1))
    tekst = ' '.join(slowa)
    ostatnie_slowo = slowa[len(slowa) - 1]
    if ostatnie_slowo[len(ostatnie_slowo) - 1] is not zakonczenie:
        tekst = tekst + zakonczenie
    tekst = tekst.capitalize()
    return tekst


