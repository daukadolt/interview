from SinglyLinkedList import LinkedList
class Queue:
    def __init__(self):
        self.list = LinkedList()
    def push(self, val):
        self.list.pushBack(val)
    def get(self):
        val = self.list.popFront()
        return val
    def __repr__(self):
        return self.list.__repr__()
    def empty(self):
        return self.list.size == 0
if __name__ == "__main__":
    q = Queue()
    print(q)
    q.push(1)
    a = q.get()
    print(a)
    print(q)