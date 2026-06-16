import heapq

class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half of numbers (inverted to mimic max-heap)
        self.max_heap = []
        # min_heap stores the larger half of numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 1. Push to max_heap first (negated because heapq is a min-heap by default)
        heapq.heappush(self.max_heap, -num)
        
        # 2. Make sure every element in max_heap is <= every element in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            
        # 3. Handle size balancing: sizes can differ by at most 1 element
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # If one heap has more elements, the median is its root
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        elif len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        
        # If heaps are of equal size, the median is the average of both roots
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0