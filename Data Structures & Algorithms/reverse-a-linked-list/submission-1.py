# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        prev = None        
        curr = head     
        
        while curr is not None:
            nxt = curr.next  # save the next node you'd like to cope with
            curr.next = prev # reverse the pointer

            prev = curr # move both nodes to next
            curr = nxt  
            
        return prev
        