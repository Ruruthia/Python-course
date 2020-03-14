from abc import ABC, abstractmethod


class Dzielenie_przez_zero(ZeroDivisionError):
    pass


class Nieprzypisana_zmienna(Exception):
    pass


class Wyrazenie:

    @abstractmethod
    def oblicz(self, zmienne):
        pass

    @abstractmethod
    def __init__(self):
        pass


class Dodaj(Wyrazenie):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz(self, zmienne):
        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            a = self.a.oblicz(zmienne)
        elif type(self.a) is Zmienna:
            if isinstance(zmienne, int):
                a = self.a.oblicz(zmienne)
            elif len(zmienne):
                a = self.a.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            a = self.a.wartosc
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            b = self.b.oblicz(zmienne)
        elif type(self.b) is Zmienna:
            if isinstance(zmienne, int):
                b = self.b.oblicz(zmienne)
            elif len(zmienne):
                b = self.b.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            b = self.b.wartosc
        return a + b

    def __str__(self):

        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            answ = "(" + str(self.a) + ")"
        else:
            answ = str(self.a)
        answ += "+"
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            answ += "(" + str(self.b) + ")"
        else:
            answ += str(self.b)
        return answ


class Odejmij(Wyrazenie):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz(self, zmienne):
        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            a = self.a.oblicz(zmienne)
        elif type(self.a) is Zmienna:
            if isinstance(zmienne, int):
                a = self.a.oblicz(zmienne)
            elif len(zmienne):
                a = self.a.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            a = self.a.wartosc
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            b = self.b.oblicz(zmienne)
        elif type(self.b) is Zmienna:
            if isinstance(zmienne, int):
                b = self.b.oblicz(zmienne)
            elif len(zmienne):
                b = self.b.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            b = self.b.wartosc
        return a - b

    def __str__(self):

        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            answ = "(" + str(self.a) + ")"
        else:
            answ = str(self.a)
        answ += "-"
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            answ += "(" + str(self.b) + ")"
        else:
            answ += str(self.b)
        return answ


class Pomnoz(Wyrazenie):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz(self, zmienne):
        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            a = self.a.oblicz(zmienne)
        elif type(self.a) is Zmienna:
            if isinstance(zmienne, int):
                a = self.a.oblicz(zmienne)
            elif len(zmienne):
                a = self.a.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            a = self.a.wartosc
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            b = self.b.oblicz(zmienne)
        elif type(self.b) is Zmienna:
            if isinstance(zmienne, int):
                b = self.b.oblicz(zmienne)
            elif len(zmienne):
                b = self.b.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            b = self.b.wartosc
        return a * b

    def __str__(self):

        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            answ = "(" + str(self.a) + ")"
        else:
            answ = str(self.a)
        answ += "*"
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            answ += "(" + str(self.b) + ")"
        else:
            answ += str(self.b)
        return answ


class Podziel(Wyrazenie):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz(self, zmienne):

        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            a = self.a.oblicz(zmienne)
        elif type(self.a) is Zmienna:
            if isinstance(zmienne, int):
                a = self.a.oblicz(zmienne)
            elif len(zmienne):
                a = self.a.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            a = self.a.wartosc
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            b = self.b.oblicz(zmienne)
        elif type(self.b) is Zmienna:
            if isinstance(zmienne, int):
                b = self.b.oblicz(zmienne)
            elif len(zmienne):
                b = self.b.oblicz(zmienne.pop(0))
            else:
                raise Nieprzypisana_zmienna()
        else:
            b = self.b.wartosc
        if b == 0:
            raise Dzielenie_przez_zero()
        return a / b

    def __str__(self):

        if (type(self.a) is Dodaj) or (type(self.a) is Odejmij) or (type(self.a) is Pomnoz) or (
                type(self.a) is Podziel):
            answ = "(" + str(self.a) + ")"
        else:
            answ = str(self.a)
        answ += "/"
        if (type(self.b) is Dodaj) or (type(self.b) is Odejmij) or (type(self.b) is Pomnoz) or (
                type(self.b) is Podziel):
            answ += "(" + str(self.b) + ")"
        else:
            answ += str(self.b)
        return answ


class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def oblicz(self, zmienne):
        return zmienne

    def __str__(self):
        return self.nazwa


class Stala(Wyrazenie):

    def __init__(self, wartosc):
        self.wartosc = wartosc

    def oblicz(self, zmienne):
        return self.wartosc

    def __str__(self):
        return str(self.wartosc)


class Program:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def wykonaj(self, zmienne, zmienne1):
        pass


class Przypisz(Program):

    def __init__(self, zmienna):
        self.zmienna = zmienna

    def wykonaj(self, zmienne):
        self.wartosc = self.zmienna.oblicz(zmienne)

    def __str__(self):
        try:
            return self.zmienna.nazwa + " = " + str(self.wartosc)
        except TypeError:
            return self.zmienna.nazwa + " = ?"
        except AttributeError:
            return self.zmienna.nazwa + " = ?"


class Warunek(Program):

    def __init__(self, wyrazenie, instrukcja):
        self.wyrazenie = wyrazenie
        self.instrukcja = instrukcja

    def wykonaj(self, zmienne, zmienne1):
        if self.wyrazenie.oblicz(zmienne) != 0:
            return self.instrukcja.wykonaj(zmienne1)
        else:
            print("Warunek nie jest spelniony")

    def __str__(self):
        answ = f"""If({self.wyrazenie.__str__()}):
        {self.instrukcja.__str__()}"""
        return answ


class Petla(Program):

    def __init__(self, warunek, instrukcja):
        self.warunek = warunek
        self.instrukcja = instrukcja

    def wykonaj(self, zmienne, zmienne1):

        while self.warunek.oblicz(zmienne):
            if type(self.instrukcja) is Program:
                print(self.instrukcja.wykonaj(zmienne1))
            else:
                print(self.instrukcja.oblicz(zmienne1))

    def __str__(self):
        answ = f"""For({self.warunek.__str__()}):
        {self.instrukcja.__str__()}"""
        return answ



