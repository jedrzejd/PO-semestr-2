class Stos:
    
    arr = None
    maxsize = 0

    def __init__(self):
        self.arr = []

    def init(self, maxsize):
        self.maxsize = maxsize


    def pop(self):
        try:
            self.arr.pop()
        except:
            print("Stack is empty")

    
    def push(self, item):
        try:
            assert(len(self.arr) < self.maxsize)
            self.arr.append(item)
        except:
            print("Stack is full")


    def top(self):
        try:
            return self.arr[-1]
        except:
            print("Stack is empty")


    def empty(self):
        return len(self.arr) == 0


    def full(self):
        return len(self.arr) == self.maxsize


    def destroy(self):
        self.arr = []



stos1, stos2 = Stos(), Stos()

stos1.init(20)
stos2.init(20)

for i in range(10):
    x = input()
    stos1.push(x)

for i in range(10):
    x = stos1.top()
    print(x)
    stos1.pop()
    stos2.push(x)

for i in range(10):
    x = stos2.top()
    stos2.pop()
    stos1.push(x)
