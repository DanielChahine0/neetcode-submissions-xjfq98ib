# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            
        dummy = ListNode()
        output = dummy
        setter = True
        
        if len(lists) == 0:
            return dummy.next

        while True:
            indexMin = -1
            minVal = float('inf')
            for i, LL in enumerate(lists):
                if LL:
                    print(LL.val)
                if LL and LL.val < minVal:
                    minVal = LL.val
                    indexMin = i
                # setter = setter and (LL)
            if indexMin == -1:
                break
            
            output.next = lists[indexMin]
            output = output.next
            lists[indexMin] = lists[indexMin].next
        
        return dummy.next
        