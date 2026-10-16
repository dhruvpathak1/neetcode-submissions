from typing import List

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        elif index == 0:
            self.head = self.head.next
            return True

        i = 1
        prev = self.head
        curr = self.head.next

        while curr:
            if i == index:
                prev.next = curr.next
                if prev.next == None:
                    self.tail = prev
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        if not self.head:
            return []
        
        curr = self.head
        vals = []
        while curr:
            print(curr.value)
            vals.append(curr.value)
            curr = curr.next
        return vals
