class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if self.isFull():
            print("Heap is Full")
            return
        self.currentPosition = self.currentPosition + 1
        self.heap[currentPosition] item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):
        parentIndex = int((index - 1) / 2)
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            swap = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = swap
            parentIndex = int((index - 1) / 2)

    def isFull(self):
        if self.currentPosition = heap.HEAP_SIZE:
            return True
        else:
            return False
