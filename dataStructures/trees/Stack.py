class Stack:
    def __init__(self):
        self.vals = []
        self.size = 0
    def push(self, val):
        self.vals.append(val)
        self.size += 1
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.vals.pop()
    def size(self):
        return self.size

class Solution(object):
    def binaryToDec(self, a):
        sum = 0
        for i in range(len(a)):
            if a[i] == "1":
                sum += pow(2, len(a)-1-i)
        return sum
    def decToBinary(self, a):
        string = ""
        stack = Stack()
        while(a != 0):
            rem = a%2
            stack.push(rem)
            a = a//2
        if stack.size == 0:
            return str(0)
        while(stack.size != 0):
            string += str(stack.pop())
        return string
        
        
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = self.binaryToDec(a) + self.binaryToDec(b)
        return self.decToBinary(sum)
        