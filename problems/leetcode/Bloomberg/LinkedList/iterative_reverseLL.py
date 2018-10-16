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

class Solution:
    def pushToNode(self, head, item):
        node = head
        while(node.next != None):
            node = node.next
        node.next = ListNode(item)
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        notToBe = None
        node = head
        newList = None
        newListSet = False
        while(True):
            if head == notToBe:
                return newList
            while(node.next != notToBe):
                node = node.next
            toBePushed = node
            if not newListSet:
                newList = ListNode(toBePushed.val)
                newListSet = True
            else:
                self.pushToNode(newList, toBePushed.val)
            notToBe = toBePushed
            node = head
        
if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    sol = Solution()
    newll = sol.reverseList(ll)
    print(newll)