from Queue import Queue
class TreeNode:
    def __init__(self, char, val):
        self.val = val
        self.char = char
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.val < other.val
    def __gt__(self, other):
        return self.val > other.val
    def __eq__(self, other):
        return self.val == other.val
    def __le__(self, other):
        return self.val <= other.val
    def __ge__(self, other):
        return self.val >= other.val
    def __ne__(self, other):
        return self.val != other.val
    def __repr__(self):
        if self.val == None or self.char == None:
            return "{None, %d}" % self.val
        return str("{\"" + self.char + "\":%d}" % self.val)

class huffmanTree:
    def frequencies(self, str):
        freq = {}
        for char in str:
            if not freq.get(char):
                freq[char] = 1
            else:
                freq[char] += 1
        return freq
    
    def __init__(self, str):
        freq = sorted(self.frequencies(str).items(), key=lambda kv: kv[1]) # keys - chars, vals - frequencies
        freq = [TreeNode(item[0], item[1]) for item in freq]
        if len(freq) == 1:
            thePair = freq.pop(0)
            self.root = TreeNode(thePair[0], thePair[1])
        else:
            while(len(freq) > 1):
                # Take two lowest freq'd chars
                # Construct each into a node and pair them under a common root of (psy, freqA+freqB)
                nodeA = freq.pop(0)
                nodeB = freq.pop(0)
                # Remove them from the freq list and substitute by the new uniting root
                unitingNode = TreeNode(None, nodeA.val + nodeB.val)
                unitingNode.left = nodeA
                unitingNode.right = nodeB
                freq.append(unitingNode)
                freq = sorted(freq)
                print(freq)
            self.root = freq[0]
        # repeat the process until there is only one item in the freq, which will be the root
    def __repr__(self):
        if not self.root:
            return None
        else:
            tempQ = Queue()
            toPrint = Queue()
            tempQ.push(self.root)
            while not tempQ.empty():
                currentNode = tempQ.get()
                toPrint.push(currentNode)
                if currentNode.left:
                    tempQ.push(currentNode.left)
                if currentNode.right:
                    tempQ.push(currentNode.right)
            return toPrint.__repr__()
            
if __name__ == "__main__":
    a = TreeNode("a", 1)
    b = TreeNode("b", 2)
    c = TreeNode("c", 3)
    List = [c,b,a]
    tree = huffmanTree("abracadabra")
    print(tree)
    print(sorted(List))