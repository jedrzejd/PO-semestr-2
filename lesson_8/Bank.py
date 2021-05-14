from Klient import Klient
from Firma import Firma
from DuzaFirma import DuzaFirma
from Osoba import Osoba
from WaznaOsoba import WaznaOsoba


class Bank:
    def __init__(self):
        self.__arr = []

    def dodajKlienta(self, Klient: Klient):
        self.__arr.append(Klient)

    def getKlienci(self):
        return self.__arr

    def get_suma_kasy_firm(self):
        suma = 0
        for x in self.__arr:
            if isinstance(x, Firma):
                suma += x.getSaldoWszystkich()
        return suma

    def get_suma_kasy_duzych_firm(self):
        suma = 0
        for x in self.__arr:
            if isinstance(x, DuzaFirma):
                suma += x.getSaldoWszystkich()
        return suma

    def get_suma_kasy_osob(self):
        suma = 0
        for x in self.__arr:
            if isinstance(x, Osoba):
                suma += x.getSaldoWszystkich()
        return suma

    def get_suma_kasy_waznych_osob(self):
        suma = 0
        for x in self.__arr:
            if isinstance(x, WaznaOsoba):
                suma += x.getSaldoWszystkich()
        return suma
