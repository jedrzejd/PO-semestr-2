from my_queue import MyQueue

k1 = MyQueue(4)

k1.add(3)
k1.add(3123)
k1.add(3)
k1.add(123)
k1.add(4)
k1.add(0)
k1.add(2)
k1.add(1)
print(k1.size())

k1.remove()
k1.remove()
k1.remove()
k1.remove()
k1.remove()
k1.remove()
