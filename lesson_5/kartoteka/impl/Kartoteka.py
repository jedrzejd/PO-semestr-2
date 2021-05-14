from kartoteka.Kartoteka import Kartoteka
from kartoteka.Osoba import Osoba


class Kartoteka(Kartoteka):

    def __init__(self):
        self.arr = []

    def dodaj(self, osoba):
        self.arr.append(osoba)
        print('\nOsoba dodana poprawnie do kartoteki')

    def usun(self, osoba):
        try:
            self.arr.remove(osoba)
            print('\nOsoba usunieta poprawnie z kartoteki')
        except Exception as _e:
            print(f'\nOsoba {osoba.getImie()} {osoba.getNazwisko()} nie wystepuje w kartotece')

    def rozmiar(self):
        return len(self.arr)

    def czyZawiera(self, osoba):
        return osoba in self.arr

    def pobierz(self, index):
        try:
            return Osoba(self.arr[index].getImie(), self.arr[index].getNazwisko())
        except Exception as _e:
            print(f'\nIndeks poza wartosciami 0 - {self.rozmiar()}')
