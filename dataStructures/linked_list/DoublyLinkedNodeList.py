from DoublyNode import DoublyNode
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def pushFront(self, val):
        newNode = DoublyNode(val)
        newNode.next = self.head
        self.head = newNode
        if self.size == 0:
            self.tail = self.head
        self.size += 1
    
    def topFront(self):
        if self.size == 0:
            return None
        return self.head.key
    
    def popFront(self):
        if self.head == None:
            return None
        head = self.head
        self.head = self.head.next
        self.size -= 1
        return head.key
    
    def pushBack(self, val):
        if self.size == 0:
            self.pushFront(val)
        else:
            newNode = DoublyNode(val)
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
    
    def topBack(self):
        if self.size == 0:
            return None
        return self.tail.key
    
    def popBack(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            return self.popFront()
        else:
            tail = self.tail
            self.tail = self.tail.prev
            self.size -= 1
            return tail.key
    
    def erase(self, key):
        if self.size == 0:
            return False
        if self.size == 1:
            if self.head.key == key:
                self.head = None
                self.size = 0
                return True
            else:
                return False
        node = self.head
        while(True):
            if node == None:
                return False
            elif node.key == key:
                self.size -= 1
                return True
            node = node.next

    def find(self, key):
        node = self.head
        if node == None:
            return False
        while(True):
            if node.next == None:
                break
            if node.key == key:
                return True
            node = node.next
        return False
    
    
    # O(n)
    def __repr__(self):
        string = "[ "
        node = self.head
        if self.size != 0:
            if node.next == None:
                string += str(node.key)
            else:
                counter = 0
                while(node.next != None):
                    if counter != 0:
                        string += ", "
                    string += str(node.key)
                    node = node.next
                    counter += 1
                string += ", " + str(node.key)
        string += " ]"
        return string
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.pushFront(1)
    print(ll.size)
    ll.pushBack(2)
    print(ll.size)
    ll.pushFront(3)
    print(ll.size)
    print(ll)
    ll.erase(3)
    print(ll.size)