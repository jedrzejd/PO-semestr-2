import time

from kartoteka.Osoba import Osoba
from kartoteka.impl.Kartoteka import Kartoteka
# from kartoteka.mockup.Karoteka import Kartoteka

def print_option():
    print('Wybierz jedną opcje')
    print('1) Dodaj osobe do kartoteki\n2) Usun osobe z kartoteki\n3) Podaj rozmiar kartoteki')
    print('4) Sprawdz czy osoba wystepuje w kartotece\n5) Wypisz osobe z kartoteki o podanym numerze')
    print('6) Zakoncz program')


kartoteka = Kartoteka()

while True:
    print_option()

    try:
        input_number = int(input('Wybrana opcja = '))

        assert(1 <= input_number <= 6)

        if input_number == 1:
            input_name = input('Podaj imie ')
            input_surname = input('Podaj nazwisko ')
            kartoteka.dodaj(Osoba(input_name, input_surname))

        elif input_number == 2:
            input_name = input('Podaj imie ')
            input_surname = input('Podaj nazwisko ')
            kartoteka.usun(Osoba(input_name, input_surname))

        elif input_number == 3:
            print(f'\nRozmiar kartoteki wynosi = {kartoteka.rozmiar()}')

        elif input_number == 4:
            input_name = input('Podaj imie ')
            input_surname = input('Podaj nazwisko ')
            print(kartoteka.czyZawiera(Osoba(input_name, input_surname)))

        elif input_number == 5:
            if kartoteka.rozmiar() == 0:
                print('\nKartoteka jest pusta')
                break

            print(f'\nPodaj index  0 - {kartoteka.rozmiar()}')

            input_index = int(input('Podaj index '))
            print(kartoteka.pobierz(input_index))

        elif input_number == 6:
            print('The End')
            break
        print('')
    except Exception as _e:
        print('Podaj liczbe od 1 do 6\n')
        time.sleep(1)
