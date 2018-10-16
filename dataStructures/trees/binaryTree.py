class DoublyNode:
    def __init__(self, val):
        self.key = val
        self.prev = None
        self.next = None

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
    

class Queue():
    def __init__(self):
        self.list = LinkedList()
    
    def put(self, val):
        self.list.pushBack(val)
    
    def empty(self):
        return self.list.size == 0
    
    def get(self):
        return self.list.popFront()

    def __repr__(self):
        return self.list.__repr__()
    

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, val):
        if self.leftChild == None:
            self.leftChild = BinaryTree(val)
        else:
            newNode = BinaryTree(val)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode

    def insert_right(self, val):
        if self.rightChild == None:
            self.rightChild = BinaryTree(val)
        else:
            newNode = BinaryTree(val)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

    def pre_order(self):
        print(self.val)
        if self.leftChild:
            self.leftChild.pre_order()
        if self.rightChild:
            self.rightChild.pre_order()
    
    def in_order(self):
        if self.leftChild:
            self.leftChild.in_order()
        print(self.val)
        if self.rightChild:
            self.rightChild.in_order()

    def post_order(self):
        if self.leftChild:
            self.leftChild.pre_order()
        if self.rightChild:
            self.rightChild.pre_order()
        print(self.val)
    
    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.val)

            if current_node.leftChild:
                queue.put(current_node.leftChild)
            
            if current_node.rightChild:
                queue.put(current_node.rightChild)

        
if __name__ == "__main__":  
    a_node = BinaryTree(1)
    a_node.insert_left(2)
    a_node.insert_right(5)

    b_node = a_node.leftChild
    b_node.insert_right(4)
    b_node.insert_left(3)

    c_node = a_node.rightChild
    c_node.insert_left(6)
    c_node.insert_right(7)

    print("pre-order")
    a_node.pre_order()
    print("in-order")
    a_node.in_order()
    print("post-order")
    a_node.post_order()
    print("BFS")
    a_node.bfs()
    
