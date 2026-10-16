# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            h = list2
            return h
        if list2 == None:
            h = list1
            return h
        if list1.val <= list2.val:
            head = list1
            curr = list1.next
            temp = list2
        else:
            head = list2
            curr = list2.next
            temp = list1
        h = head
        while curr and temp:
            if curr.val <= temp.val:
                head.next = curr
                head = curr
                curr = curr.next
            else:
                head.next = temp
                head = temp
                temp = temp.next
        if temp:
            head.next = temp
        elif curr:
            head.next = curr
            
        return h

