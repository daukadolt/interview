class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def pushBack(self, val):
        newNode = Node(val)
        if self.size == 0:
            self.head = newNode
            self.size += 1
        else:
            node = self.head
            while(node.next != None):
                node = node.next
            node.next = newNode
            self.size += 1
    def pushFront(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    def popBack(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = None
            self.size -= 1
        else:
            node = self.head
            while(node.next.next != None):
                node = node.next
            val = node.next.val
            node.next = None
            self.size -= 1
            return val
    def popFront(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            val = self.head.val
            self.head = None
            self.size -= 1
            return val
        else:
            val = self.head.val
            self.head = self.head.next
            self.size -= 1
            return val
    def topBack(self):
        if self.size == 0:
            return None
        else:
            node = self.head
            while(node.next != None):
                node = node.next
            val = node.val
            return val
    def topFront(self):
        if self.size == 0:
            return None
        else:
            val = self.head.val
            return val
    def __repr__(self):
        string = "[ "
        node = self.head
        for index in range(self.size):
            if index != 0:
                string += ", "
            string += str(node.val)
            node = node.next
        string += " ]"
        return string

if __name__ == "__main__":
    ll = LinkedList()
    ll.pushBack(1)
    print(ll.popFront())
    print(ll)