class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Step 2: Create buckets where index = frequency
        # Each index will hold a list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Iterate backwards from the highest frequency bucket to collect top k elements
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res