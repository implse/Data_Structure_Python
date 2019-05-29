class MinHeap:
    def __init__(self, array):
        self.heap = self.heapify(array)
    # O(n) Time / O(1) Space
    def heapify(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) Time / O(1) Space
    def siftDown(self, currentIdx, endIdx, heap):
        # Left Child
        childOneIdx = (currentIdx * 2) + 1
        while childOneIdx <= endIdx:
            # Right Child
            childTwoIdx = (currentIdx * 2) + 2 if (currentIdx * 2) + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx * 2) + 1
            else:
                break

    # O(log(n)) Time / O(1) Space
    def siftUp(self, currentIdx, Heap):
        parrentIdx = (currentIdx - 1) // 2
        # While we are not of top of the heap and value at currentIdx is less than parent value
        while currentIdx > 0 and heap[currentIdx] < heap[parrentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parrentIdx = (currentIdx - 1) // 2

    # O(1) Time
    def peek(self):
        return self.heap[0]

    def heapPop(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def heapPush(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
