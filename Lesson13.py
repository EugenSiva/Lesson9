class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, char):
        if self.is_full():
            print("Queue is full!")
        else:
            self.queue.append(char)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue.pop(0)

    def show(self):
        print("Queue:", self.queue)

q = Queue(5)
q.enqueue("Eugen")
q.show()




