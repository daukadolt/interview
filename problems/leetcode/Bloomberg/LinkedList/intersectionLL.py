# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def pushToHashtable(self, hashtable, node):
        _hash = hash(node)
        _bucket_id = _hash%len(hashtable)
        _the_set = hashtable[_bucket_id]
        _the_set.add(node)
        
    def isInHashtable(self, hashtable, node):
        _hash = hash(node)
        _bucket_id = _hash%len(hashtable)
        _the_set = hashtable[_bucket_id]
        return node in _the_set
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hashtable = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set(), 9:set()}
        node = headA
        while(node != None):
            self.pushToHashtable(hashtable, node)
            node = node.next
        node = headB
        while(node != None):
            if self.isInHashtable(hashtable, node):
                return node
            node = node.next
        return None
            
        