# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def recursiveToNum(self, head, power = 0):
        if head.next == None:
            return head.val*pow(10, power)
        else:
            return pow(10, power)*head.val + self.recursiveToNum(head.next, power+1)
    
    def iterativeNumToLL(self, sum):
        head = None
        prevNode = None
        digits = []
        if sum != 0:
            while(sum != 0):
                digit = sum % 10
                digits.append(digit)
                sum = sum // 10
        else:
            digits = [0]
        for digit in digits:
            if head == None:
                head = ListNode(digit)
                prevNode = head
            else:
                prevNode.next = ListNode(digit)
                prevNode = prevNode.next
        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self.recursiveToNum(l1) + self.recursiveToNum(l2)
        sumLL = self.iterativeNumToLL(sum)
        return sumLL

if __name__ == "__main__":
    ll = ListNode(0)
    ll2 = ListNode(0)
    sol = Solution()
    sum = sol.recursiveToNum(ll)+sol.recursiveToNum(ll2)
    sumLL = sol.iterativeNumToLL(sum)
    print(sumLL.val)
        