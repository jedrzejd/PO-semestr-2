class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def default(cls):
        return Punkt(0, 0)

    def __eq__(self, other):
        if isinstance(other, Punkt):
            return other.x == self.x and other.y == self.y

    def print(self):
        return self.x, self.y


class Figura:
    def __init__(self, value):
        self._color = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


class Trojkat(Figura):
    def __init__(self, a: Punkt, b: Punkt, c: Punkt, value):
        super().__init__(value)
        self.a = a
        self.b = b
        self.c = c

    def wypisz_punkty(self):
        return self.a.print(), self.b.print(), self.c.print()


class Czworokat(Figura):
    def __init__(self, a: Punkt, b: Punkt, c: Punkt, d: Punkt, value):
        super().__init__(value)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def wypisz_punkty(self):
        return self.a.print(), self.b.print(), self.c.print(), self.d.print()


class Prostokat(Czworokat):
    def __init__(self, left_top: Punkt, right_down: Punkt, value):
        p1 = left_top
        p2 = Punkt(right_down.x, left_top.y)
        p3 = right_down
        p4 = Punkt(left_top.x, right_down.y)
        super().__init__(p1, p2, p3, p4, value)


class Kwadrat(Prostokat):
    def __init__(self, left_top: Punkt, dl_boku, value):
        self.dl_boku = dl_boku
        super().__init__(left_top, Punkt(left_top.x + dl_boku, left_top.y - dl_boku), value)




ABCD = Kwadrat(Punkt(5, 0), 5, "czerwony")
print(ABCD.color)
ABCD.color = "Kolorowy"
print(ABCD.color)

ABC = Trojkat(Punkt(5, 0), Punkt(0, 0), Punkt(10, 0), "fabryczny")

ABCDpro = Prostokat(Punkt(5, 0), Punkt(0, 5), "iżbinowy")

print('\npetla\n')

arr = [ABCD, ABC, ABCDpro]

for it in arr:
    print(it.__class__.__name__, it.color, it.wypisz_punkty())