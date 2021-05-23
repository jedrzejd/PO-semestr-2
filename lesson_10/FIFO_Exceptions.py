class FIFOException(Exception):
    def __init__(self, mess):
        super().__init__(mess)


class ListException(FIFOException):
    def __init__(self, mess):
        super().__init__(mess)


class FullListException(ListException):
    def __init__(self, mess):
        super().__init__(mess)


class EmptyListException(ListException):
    def __init__(self, mess):
        super().__init__(mess)


class RepeatItemListException(ListException):
    def __init__(self, mess):
        super().__init__(mess)


class OutOfRangeListException(ListException):
    def __init__(self, mess):
        super().__init__(mess)


class BadNumberException(FIFOException):
    def __init__(self, mess):
        super().__init__(mess)


class IntException(BadNumberException):
    def __init__(self, mess):
        super().__init__(mess)


class NegativeNumberException(IntException):
    def __init__(self, mess):
        super().__init__(mess)
