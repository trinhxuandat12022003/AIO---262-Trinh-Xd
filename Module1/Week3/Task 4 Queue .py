class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            print('Queue is full, can not enqueue anymore')
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty, can not dequeue anymore')
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            print('Queue is empty')
        return self.__queue[0]


queue1 = MyQueue ( capacity =5)
queue1 . enqueue (1)
assert queue1 . is_full () == False
queue1 . enqueue (2)
print ( queue1 . front () )
