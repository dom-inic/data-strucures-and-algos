# first in first out FIFO
class MyQue:
    def __init__(self):
        self.data= []

    def length(self):
        return len(self.data)

    def enqueue(self, element): # instering an element into the queue
        if len(self.data) == 5:
            return "queue is full"
        else:
            self.data.append(element)

    def dequeue(self):
        if len(self.data)  == 0:
            return "queue is empty, nothing to remove"
        else:
            # pop the first element on them list 
            self.data.pop(0)

    
