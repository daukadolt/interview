class Vector:
    size = 0
    data = []
    def __init__(self):
        self.size = 0
    
    def __repr__(self):
        print("< " + "".join(str(i) for i in self.data) + " >")
    
    def __str__(self):
        return ("< " + ",".join(str(i) for i in self.data) + " >")

    def getData(self):
        return self.data
    
    def push_back(self, item):
        self.size += 1
        self.data.append(item)

if __name__ == "__main__":
    vect = Vector()
    vect.push_back(1)
    vect.push_back(1)
    print(vect)