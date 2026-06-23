class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # one represents ways(i-1), two represents ways(i-2)
        one, two = 2, 1
        
        for i in range(3, n + 1):
            current = one + two
            two = one
            one = current
            
        return one