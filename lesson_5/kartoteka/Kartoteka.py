from kartoteka.Osoba import Osoba


class Kartoteka:

    """
    Kartoteka Interface
    """

    def dodaj(self, osoba: Osoba):
        pass

    def usun(self, osoba: Osoba):
        pass

    def rozmiar(self) -> int:
        pass

    def czyZawiera(self, osoba: Osoba) -> bool:
        pass

    def pobierz(self, index: int) -> Osoba:
        pass
