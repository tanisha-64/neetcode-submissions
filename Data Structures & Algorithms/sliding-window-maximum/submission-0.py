from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # Stores indices of elements
        
        for r in range(len(nums)):
            # Remove smaller values from the back of the queue
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
                
            q.append(r)
            
            # Remove the front index if it falls out of the current window boundary
            if q[0] < r - k + 1:
                q.popleft()
                
            # Append max element to output once window reaches size k
            if r >= k - 1:
                res.append(nums[q[0]])
                
        return res