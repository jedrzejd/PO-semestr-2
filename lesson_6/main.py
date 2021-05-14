import math
from random import randrange
import copy


class Punkt:

    def __init__(self, x, y):
        # print(f"Punkt init x = {x}, y = {y}")
        self.x = x
        self.y = y

    @classmethod
    def default(cls):
        # print("Punkt domyslny kontruktor")
        return Punkt(randrange(10), randrange(10))

    def __eq__(self, other):
        if isinstance(other, Punkt):
            return other.x == self.x and other.y == self.y

    def przesun(self, a, b):
        self.x += a
        self.y += b

    def wypisz(self):
        return self.x, self.y


class Linia:

    def __init__(self, p: Punkt, q: Punkt):
        # print(f"Linia init a = {p.wypisz()}, b = {q.wypisz()}")
        self.a = p
        self.b = q

    @classmethod
    def default(cls):
        # print("Linia domyslny kontruktor")
        return Linia(Punkt.default(), Punkt.default())

    def __eq__(self, other):
        if isinstance(other, Linia):
            return (other.a == self.a and other.b == self.b) or (other.a == self.b and other.b == self.a)

    def przesun(self, a, b):
        self.a.przesun(a, b)
        self.b.przesun(a, b)

    def podaj_dlugosc(self):
        return math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)

    def wypisz_linie(self):
        return self.a.wypisz(), self.b.wypisz()


class Trojkat:
    def __init__(self, a: Linia, b: Linia, c: Linia):
        # print(f"Linia init a = {p.wypisz()}, b = {q.wypisz()}")
        self.bok_a = a.podaj_dlugosc()
        self.bok_b = b.podaj_dlugosc()
        self.bok_c = c.podaj_dlugosc()
        self.ab = a
        self.bc = b
        self.ca = c
        self.boki = sorted([self.bok_a, self.bok_b, self.bok_c])
        self.obwod = self.bok_a + self.bok_b + self.bok_c
        s = self.obwod / 2

        self.pole = (s * (s - self.bok_a) * (s - self.bok_b) * (s - self.bok_c)) ** 0.5

    @classmethod
    def default(cls):
        return Trojkat(Linia(Punkt(5, 0), Punkt(0, 5)), Linia(Punkt(0, 5), Punkt(0, 0)),
                       Linia(Punkt(0, 0), Punkt(5, 0)))

    def __eq__(self, other):
        if isinstance(other, Trojkat):
            return self.boki == other.boki

    def przesun(self, a1, b1):
        self.ab.przesun(a1, b1)
        self.bc.przesun(a1, b1)
        self.ca.przesun(a1, b1)

    def wypisz_obwod(self):
        return self.obwod

    def wypisz_pole(self):
        return self.pole

    def wypisz_boki(self):
        return [x for x in self.boki]


class Czworokat:
    def __init__(self, a: Linia, b: Linia, c: Linia, d: Linia):
        # print(f"Linia init a = {p.wypisz()}, b = {q.wypisz()}")
        self.bok_a = a.podaj_dlugosc()
        self.bok_b = b.podaj_dlugosc()
        self.bok_c = c.podaj_dlugosc()
        self.bok_d = d.podaj_dlugosc()
        self.ab = a
        self.bc = b
        self.cd = c
        self.da = d
        self.boki = sorted([self.bok_a, self.bok_b, self.bok_c, self.bok_d])
        self.obwod = self.bok_a + self.bok_b + self.bok_c + self.bok_d

    @classmethod
    def default(cls):
        return Czworokat(Linia(Punkt(0, 0), Punkt(5, 0)), Linia(Punkt(5, 0), Punkt(5, 5)),
                         Linia(Punkt(5, 5), Punkt(0, 5)), Linia(Punkt(0, 5), Punkt(0, 0)))

    def przesun(self, a1, b1):
        self.ab.przesun(a1, b1)
        self.bc.przesun(a1, b1)
        self.cd.przesun(a1, b1)
        self.da.przesun(a1, b1)

    def wypisz_obwod(self):
        return self.obwod

    def wypisz_boki(self):
        return [x for x in self.boki]


class Obraz:
    def __init__(self):
        self._arr = []

    def wypisz(self):
        return self._arr

    def dodaj(self, x):
        self._arr.append(x)



p = Punkt(10, 5)
q = Punkt(5, 10)
r = Punkt(5, 5)

ab = Linia(p, q)
bc = Linia(q, r)
ca = Linia(r, p)

ABC = Trojkat.default()

DEF = Trojkat(ab, bc, ca)

print(ABC == DEF)
