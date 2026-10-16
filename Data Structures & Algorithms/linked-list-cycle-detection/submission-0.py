# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []
        while curr:
            if curr.next not in arr:
                arr.append(curr.next)
            else:
                return True
            curr = curr.next
        
        return False
