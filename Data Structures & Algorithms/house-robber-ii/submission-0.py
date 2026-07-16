class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there's only one house, rob it!
        if len(nums) == 1:
            return nums[0]
            
        # Helper function to solve the simple linear House Robber I
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # The result is the maximum of:
        # 1. Robbing houses 1 to n-1 (skip last)
        # 2. Robbing houses 2 to n (skip first)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))