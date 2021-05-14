class Konto:
    def __init__(self, nr: str, saldo: float):
        self.__nr = nr
        self.__saldo = saldo

    @classmethod
    def default(cls):
        return cls('', 0)

    def getSaldo(self):
        return self.__saldo

    def getNr(self):
        return self.__nr

    def wplac(self, kwota: float):
        self.__saldo += kwota

    def wyplac(self, kwota: float):
        self.__saldo -= kwota
