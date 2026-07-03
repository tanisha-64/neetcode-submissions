# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to seamlessly handle removing the head node
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Advance the right pointer n steps ahead
        for _ in range(n):
            right = right.next
            
        # Move both pointers simultaneously until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Delete the n-th node from the end
        left.next = left.next.next
        
        return dummy.next