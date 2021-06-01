class Stos:
    def __init__(self, maxsize):
        self.arr = []
        self.maxsize = maxsize

    def pop(self):
        try:
            self.arr.pop()
        except Exception as e:
            print(e)

    def push(self, item):
        try:
            assert (len(self.arr) < self.maxsize)
            self.arr.append(item)
        except Exception:
            print("Stack is full")

    def top(self):
        try:
            return self.arr[-1]
        except Exception:
            print("Stack is empty")

    def size(self):
        return len(self.arr)

    def empty(self):
        return len(self.arr) == 0

    def full(self):
        return len(self.arr) == self.maxsize

    def destroy(self):
        self.arr = []

