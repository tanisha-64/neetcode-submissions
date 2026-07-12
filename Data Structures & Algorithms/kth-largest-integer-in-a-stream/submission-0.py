import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements in the heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # If adding the new element exceeds size k, pop the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of the min-heap is the k-th largest element
        return self.heap[0]