# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while slow and slow.next:
            slow = slow.next.next
            fast = fast.next
            if slow == fast: return True
            
        return False
            
        