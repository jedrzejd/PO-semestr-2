from Konto import Konto


class Klient:
    def __init__(self):
        self.__arr = []

    def dodajKonto(self, Konto: Konto):
        self.__arr.append(Konto)

    def getKonta(self):
        return self.__arr

    def getSaldoWszystkich(self):
        sum = 0
        for x in self.__arr:
            sum += x.getSaldo()
        return sum
