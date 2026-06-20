# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if slow == fast:          # Cycle detected
                return True
                
        return False