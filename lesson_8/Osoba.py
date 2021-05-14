from Klient import Klient


class Osoba(Klient):
    def __init__(self, imie: str, nazwisko: str, PESEL: str):
        super().__init__()
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__PESEL = PESEL
