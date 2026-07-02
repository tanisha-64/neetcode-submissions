class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than the highest element, 
            # the minimum must be in the right unsorted part.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is either at mid or to its left.
            else:
                high = mid
                
        return nums[low]