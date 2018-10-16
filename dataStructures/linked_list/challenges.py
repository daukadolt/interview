from DoublyLinkedNodeList import LinkedList
import random

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(100):
        ll.pushBack(i)
        ll.pushBack(i)
    print(ll)