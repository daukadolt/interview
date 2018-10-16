# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_p = fast_p = head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
            if slow_p == fast_p:
                return True
        return False
    