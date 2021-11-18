class FixedQueue:

        class Empty(Exception):
            pass
        class Full(Exception):
            pass
        def __init__(self, capacity: int):
            self.no = 0
            self.front = 0
            self.rear = 0
            self.capacity = capacity
            self.que = [None] * capacity

        def __len__(self):
            return self.no
        
        def is_empty(self):
            return self.no <= 0

        def is_full(self):
            return self.no >= self.capacity

        def enque(self, x):
            if self.is_full():
                raise FixedQueue.Full
            self.que[self.rear] = x
            self.rear += 1
            self.no += 1
            if self.rear == self.capacity:
                self.rear = 0

        def deque(self, x):
            if self.is_empty():
                raise FixedQueue.Empty
            x = self.que[self.front]
            self.front += 1
            self.no -= 1
            if self.front == self.capacity:
                self.front = 0
            return x