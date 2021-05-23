from FIFO_Exceptions import FIFOException, FullListException, RepeatItemListException, IntException, \
    OutOfRangeListException, EmptyListException


class MyQueue:
    def __init__(self, num):
        if not type(num) is int:
            raise TypeError("Only integers are allowed")
        if num < 0:
            raise Exception('You create a queue with a negative number of items')
        try:
            self.arr = []
            self.max_size = num + 1
        except Exception as e:
            print(e)

    def add(self, value):
        try:
            if self.full():
                raise FullListException('Add to full list')
            elif value in self.arr:
                raise RepeatItemListException('The item is in the queue')
            elif type(value) is not int:
                raise IntException('The item is not a natural number')
            elif value > self.max_size:
                raise OutOfRangeListException('The item is out of range')
            self.arr.append(value)
            print(f'Added {value}')
        except FullListException as e:
            print(e)
        except RepeatItemListException as e:
            print(e)
        except IntException as e:
            print(e)
        except OutOfRangeListException as e:
            print(e)

        except FIFOException as e:
            print(e)

    def remove(self):
        try:
            if self.empty():
                raise EmptyListException('You remove an item from an empty queue')
            self.arr.pop(0)
        except EmptyListException as e:
            print(e)
        except FIFOException as e:
            print(e)

    def size(self):
        return len(self.arr)

    def empty(self):
        return len(self.arr) == 0

    def full(self):
        return len(self.arr) == self.max_size

    def print(self):
        print(self.arr)
