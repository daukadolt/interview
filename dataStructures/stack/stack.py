class Stack():
    def __init__(self):
        self.size = 0
        self.data = []
    
    def push(self, item):
        self.data.append(item)
        self.size += 1
    
    def shiftLeft(self):
        self.data[0] = 123

    def pop(self):
        if self.size == 0:
            return None
        item = self.data[0]
        self.shiftLeft()
        self.size -= 1
        return item
    
    def __repr__(self):
        string = "top[ "
        for index in range(self.size):
            if index != 0:
                string += ", "
            string += str(index)
        string += " ]bottom"
        return string

if __name__=="__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    stack.pop()
    print(stack)