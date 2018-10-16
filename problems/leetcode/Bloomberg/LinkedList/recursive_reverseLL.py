# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        node = self
        string = "[ "
        while(node != None):
            string += str(node.val)
            node = node.next
        string += " ]"
        return string
    
    def setNext(self, node):
        print("setting next of %d to %d" % (self.val, node.val))
        self.next = node

class Solution:
    def reverse(self, node, head):
        print("Head = %d" % head.val)
        if node.next == None:
            print("if none")
            head = node
            print("Head = %d" % head.val)
            return node
        else:
            print("else")
            nextNode = node.next
            node.next = None
            newChain = self.reverse(nextNode, head).setNext(node)
            return newChain

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        self.reverse(node, head)
        return head
        
        
        
if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    sol = Solution()
    newll = sol.reverseList(ll)
    print(newll)