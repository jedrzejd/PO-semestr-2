from kartoteka.Kartoteka import Kartoteka
from kartoteka.Osoba import Osoba


class Kartoteka(Kartoteka):

    def dodaj(self, osoba):
        pass

    def usun(self, osoba):
        pass

    def rozmiar(self):
        return 1

    def czyZawiera(self, osoba):
        return True

    def pobierz(self, index):
        return Osoba('Gall', 'Anonim')
