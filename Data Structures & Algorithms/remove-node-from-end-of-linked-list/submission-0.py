# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        prev = None
        counter = 0
        
        while counter < n:
            first = first.next
            counter += 1

        if not first:
            return head.next

        while first:
            first = first.next
            prev = second
            second = second.next
        
        prev.next = second.next
        
        return head 