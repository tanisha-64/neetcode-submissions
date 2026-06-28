class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Step 1: Calculate prefix products and store them in output
        # output[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products on the fly and multiply with prefix
        # suffix will contain the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output