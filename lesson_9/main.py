from math import pi, sqrt


class Figura:
    def __init__(self, points,  color):
        self.color = color
        self.points = points

    """
    Zakładam poprawną kolejność punktów z których składa się figura
    """
    def obwod(self):
        sum = 0
        a, b = self.points[0]
        for x, y in self.points[1:]:
            sum += sqrt((x-a)**2 + (y-b)**2)
            a, b = x, y
        x, y = self.points[0]
        sum += sqrt((x - a) ** 2 + (y - b) ** 2)
        return sum

    def pole(self):
        p = 0.0
        for _i in range(len(self.points)):
            x1, y1 = self.points[_i]
            x2, y2 = self.points[(_i+1)%len(self.points)]
            p += (x1 + x2) * (y1 - y2)
        return abs(p/2)


    def przesun(self, vec):
        for point in self.points:
            point += vec

    def __str__(cls):
        return \
            str(cls.__class__.__name__+'\n'+f'Obwod = {cls.obwod()}\n'+f'Pole = {cls.pole()}\n'+'Punkty'+str([(x, y) for x, y in cls.points]))


class Kolo(Figura):
    def __init__(self, radius):
        self.radius = radius

    def obwod(self):
        return 2 * pi * self.radius

    def pole(self):
        return pi * self.radius ** 2

    def skaluj(self, x):
        self.radius *= x

    def __str__(cls):
        return \
            str(cls.__class__.__name__+'\n'+f'Obwod = {cls.obwod()}\n'+f'Pole = {cls.pole()}\n'+f'Promien = {cls.radius}')


class Kwadrat(Figura):
    def __init__(self, side):
        self.side = side

    def obwod(self):
        return self.side * 4

    def pole(self):
        return self.side ** 2

    def skaluj(self, x):
        self.side *= x

    def __str__(cls):
        return \
            str(cls.__class__.__name__+'\n'+f'Obwod = {cls.obwod()}\n'+f'Pole = {cls.pole()}\n'+f'Bok = {cls.side}')


def summary(fig_arr):
    sum_area = 0
    sum_perimeter = 0
    for x in fig_arr:
        print('-'*20)
        print(x)
        sum_area += x.pole()
        sum_perimeter += x.obwod()
    print(f'Suma pól = {sum_area}')
    print(f'Łączny obwód = {sum_perimeter}\n')


figura = Figura([(0, 0), (5,0), (5, 5), (0, 5)], 'fiolet')
kwadrat = Kwadrat(5)
kolo = Kolo(5)


fig_arr = [figura, kwadrat, kolo]

summary(fig_arr)


fig_arr[0].przesun((1, 1))

summary(fig_arr)

fig_arr[1].skaluj(2)
fig_arr[2].skaluj(2)

summary(fig_arr)