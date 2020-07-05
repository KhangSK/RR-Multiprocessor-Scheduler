class CircularQueue:
    #Constructor
    def __init__(self):
        self.queue = [None] * 8
        self.head = 0
        self.tail = 0
        self.size = 0
        self.maxSize = 8

    #Adding elements to the queue
    def enqueue(self,data):
        if self.size == self.maxSize:
            print("Queue full! Increasing size...")
            self.increase_size(self.maxSize + 8)
            return self.enqueue(data)

        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.maxSize
        self.size += 1

        return True

    #Removing elements from the queue
    def dequeue(self):
        if self.empty():
            print("Error. Try to dequeue an empty queue!")
            return None
        
        data = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.maxSize
        self.size -= 1

        return data

    #Check if queue empty
    def empty(self):
        return self.size == 0

    def increase_size(self, newsize):
        newqueue = [None] * newsize
        i = 0
        
        while True:
            newqueue[i] = self.queue[self.head]
            i += 1
            self.head = (self.head + 1) % self.maxSize

            if (self.head == self.tail):
                break
        
        self.queue = newqueue
        self.head = 0
        self.tail = i
        self.maxSize = newsize

    def w_inc(self):
        for task in self.queue:
            if task is not None:
                task.w_inc()
