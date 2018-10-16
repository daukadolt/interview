from Node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    
    ## O(1)
    def pushFront(self, key):
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    ## O(1)
    def topFront(self):
        if self.head == None:
            return None
        return self.head.val
    
    ## O(1)
    def popFront(self):
        if self.head == None:
            return None
        front = self.head.key
        self.head = self.head.next
        self.size -= 1
        return front

    # O(n)
    def pushBack(self, key):
        node = self.head
        if node == None:
            self.pushFront(key)
        else:
            while(node.next != None):
                node = node.next
            node.next = Node(key)
            self.size += 1
    
    # O(n)
    def topBack(self):
        node = self.head
        if node == None:
            return None
        while(node.next != None):
            node = node.next
        return node.val
    
    # O(n)
    def popBack(self):
        node = self.head
        if node == None:
            return None
        if node.next == None:
            self.popFront()
        while(node.next.next != None):
            node = node.next
        back = node.next.val
        node.next = None
        self.size -=1
        return back
    
    # O(n)
    def find(self, key):
        node = self.head
        if node == None:
            return False
        while(True):
            if node.next == None:
                break
            if node.val == key:
                return True
            node = node.next
        return False
    
    # O(n)
    def __repr__(self):
        string = "[ "
        node = self.head
        print("Head = %d" % self.head.val)
        if self.size != 0:
            if node.next == None:
                string += str(node.val)
            else:
                counter = 0
                while(node.next != None):
                    if counter != 0:
                        string += ", "
                    string += str(node.val)
                    node = node.next
                    counter += 1
                string += ", " + str(node.val)
        string += " ]"
        return string
            


if __name__ == "__main__":
    ll = LinkedList()
