from Klient import Klient


class Firma(Klient):
    def __init__(self, nazwa: str, KRS: str):
        super().__init__()
        self._nazwa = nazwa
        self._KRS = KRS
