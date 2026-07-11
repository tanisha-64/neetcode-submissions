class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            # Base Case: Success condition
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case: Out of bounds or exceeded target sum
            if i >= len(nums) or total > target:
                return
            
            # Decision 1: Include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            
            # Decision 2: Exclude nums[i] (Backtrack)
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res