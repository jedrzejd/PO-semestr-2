from Bank import Bank
from Firma import Firma
from Konto import Konto
from Osoba import Osoba
from DuzaFirma import DuzaFirma
from WaznaOsoba import WaznaOsoba
from random import randint

pko = Bank()
firma = Firma('dom', '123')
firma2 = Firma('domek', '100')
osoba = Osoba('jan', 'karol', '982')
duzaFirma = DuzaFirma('dom', '256')
waznaOsoba = WaznaOsoba('Andy', 'Kamysz', '111')

pko.dodajKlienta(firma)
pko.dodajKlienta(firma2)
pko.dodajKlienta(osoba)
pko.dodajKlienta(duzaFirma)
pko.dodajKlienta(waznaOsoba)

for klient in pko.getKlienci():
    cnt = 0
    for _x in range(randint(1, 3)):
        klient.dodajKonto( Konto( str(randint(1, 111) ) , cnt) )
        cnt += 1

cnt = 0
for klient in pko.getKlienci():
    print(f'Klient = {cnt} ')
    cnt += 1
    for konto in klient.getKonta():
        print(konto.getNr(), konto.getSaldo())

print(pko.get_suma_kasy_firm())