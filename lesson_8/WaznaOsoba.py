from Osoba import Osoba


class WaznaOsoba(Osoba):
    def __init__(self, imie: str, nazwisko: str, PESEL: str):
        super().__init__(imie, nazwisko, PESEL)
