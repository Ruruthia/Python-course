from Zadanie1 import *
import io
import unittest
import unittest.mock

A = Dodaj(Zmienna("x"), Zmienna("y"))
B = Odejmij(Zmienna("x"), Zmienna("y"))
C = Pomnoz(Zmienna("x"), Zmienna("y"))
D = Podziel(Zmienna("x"), Zmienna("y"))
E = Podziel(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y"))
F = Dodaj(Pomnoz(Zmienna("x"), Zmienna("y")), Dodaj(Zmienna("z"), Zmienna("v")))
G = Dodaj(Dodaj(Zmienna("x"), Zmienna("y")), Zmienna("z"))
P = Przypisz(Zmienna("x"))
Q = Warunek(G, Przypisz(Zmienna("x")))
R = Petla(G, Odejmij(A, Stala(2)))


class TestDodaj(unittest.TestCase):
    """Test Dodaj class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(A)
        self.assertEqual(mock_stdout.getvalue(), "x+y\n")

    def test_oblicz(self):
        self.assertEqual(A.oblicz([2, 3]), 5)

    def test_error(self):
        with self.assertRaises(Nieprzypisana_zmienna): A.oblicz([1])


class TestOdejmij(unittest.TestCase):
    """Test Odejmij class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(B)
        self.assertEqual(mock_stdout.getvalue(), "x-y\n")

    def test_oblicz(self):
        self.assertEqual(B.oblicz([2, 3]), -1)

    def test_error(self):
        with self.assertRaises(Nieprzypisana_zmienna): B.oblicz([1])


class TestPomnoz(unittest.TestCase):
    """Test Pomnoz class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(C)
        self.assertEqual(mock_stdout.getvalue(), "x*y\n")

    def test_oblicz(self):
        self.assertEqual(C.oblicz([2, 3]), 6)

    def test_error(self):
        with self.assertRaises(Nieprzypisana_zmienna): C.oblicz([1])


class TestPodziel(unittest.TestCase):
    """Test Podziel class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(D)
        self.assertEqual(mock_stdout.getvalue(), "x/y\n")

    def test_oblicz(self):
        self.assertEqual(D.oblicz([3, 2]), 1.5)

    def test_error(self):
        with self.assertRaises(Nieprzypisana_zmienna): D.oblicz([1])

    def test_zero(self):
        with self.assertRaises(Dzielenie_przez_zero): D.oblicz([1, 0])


class TestWyrazenie(unittest.TestCase):
    """Test complex expressions class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(E)
        self.assertIn("(x+2)/y\n", mock_stdout.getvalue())
        print(F)
        self.assertIn("(x*y)+(z+v)\n", mock_stdout.getvalue())
        print(G)
        self.assertIn("(x+y)+z\n", mock_stdout.getvalue())

    def test_oblicz(self):
        self.assertEqual(E.oblicz([8, 2]), 5)
        self.assertEqual(F.oblicz([2, 3, 4, 5]), 15)
        self.assertEqual(G.oblicz([7, 9, 11]), 27)

    def test_error(self):
        with self.assertRaises(Nieprzypisana_zmienna): E.oblicz([1])
        with self.assertRaises(Nieprzypisana_zmienna): F.oblicz([1, 3, 4])
        with self.assertRaises(Nieprzypisana_zmienna): G.oblicz([5, 6])

    def test_zero(self):
        with self.assertRaises(Dzielenie_przez_zero): E.oblicz([1, 0])


class TestPrzypisz(unittest.TestCase):
    """Test Przypisz class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(P)
        self.assertIn("x = ?\n", mock_stdout.getvalue())
        P.wykonaj(2)
        print(P)
        self.assertIn("x = 2\n", mock_stdout.getvalue())


class TestWarunek(unittest.TestCase):
    """Test Warunek class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(Q)
        self.assertIn("""If((x+y)+z):\n        x = ?\n""", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wykonaj(self, mock_stdout):
        Q.wykonaj([1, 2, 3], 5)
        print(Q)
        self.assertIn("""If((x+y)+z):\n        x = 5\n""", mock_stdout.getvalue())
        Q.wykonaj([0, 0, 0], 5)
        print(Q)
        self.assertIn("""Warunek nie jest spelniony\n""", mock_stdout.getvalue())


class TestPetla(unittest.TestCase):
    """Test Petla class"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        print(R)
        self.assertIn("""For((x+y)+z):\n        (x+y)-2\n""", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wykonaj(self, mock_stdout):
        R.wykonaj([1, 2, 3, 4, 6, 7, 5, 8, 2, 0, 0, 0], [1, 2, 3, 5, 5, 1])
        self.assertIn("""1\n6\n4\n""", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
