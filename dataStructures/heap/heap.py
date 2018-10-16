class maxHeap:
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # i*2 + 1 - leftChild
    # i*2 + 2 - rightChild
    # This will be a 0-based indexing Heap
    def __init__(self):
        self.vals = []
        self.size = 0
    def parent(self, i):
        if i <= 0:
            return 0
        else:
            return (i-1)//2
    def leftChild(self, i):
        return i*2+1
    def rightChild(self, i):
        return i*2+2
    def siftUp(self, i):
        if self.size == 0:
            return
        else:
           while(i>0 and self.vals[self.parent(i)]<self.vals[i]):
            #    print(i)
               self.swap(i, self.parent(i))
               i = self.parent(i)
    def swap(self, a, b):
        temp = self.vals[a]
        self.vals[a] = self.vals[b]
        self.vals[b] = temp
    def siftDown(self, i):
        if i<0:
            return
        maxIndex = i
        x = self.leftChild(i)
        if x<self.size and self.vals[x]>self.vals[maxIndex]:
            maxIndex = x
        y = self.rightChild(i)
        if y<self.size and self.vals[y]>self.vals[maxIndex]:
            maxIndex = y
        if i != maxIndex:
            self.swap(i, maxIndex)
            self.siftDown(maxIndex)
        else:
            return
    def insert(self, val):
        self.size += 1
        self.vals.append(val)
        self.siftUp(self.size-1)
    def extractMax(self):
        if self.size == 0:
            return None
        else:
            result = self.vals[0]
            self.vals[0] = self.vals[self.size-1]
            self.size -= 1
            self.siftDown(0)
            return result
    def remove(self, i):
        if i < self.size:
            self.vals[i] = self.vals[0]+1
            self.siftUp(i)
            self.extractMax()
    def __repr__(self):
        return str(self.vals)

if __name__ == "__main__":
    heap = maxHeap()
    # print(heap)
    for i in range(10):
        heap.insert(i)
    # print(heap)
    # print(heap.extractMax())
    # heap.siftDown(0)
    # print(heap)
    
    # #
    # #
    # #

    # heap.remove(0)
    # print(heap)
    # heap.insert(7)
    print(heap)