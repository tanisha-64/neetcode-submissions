class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Base case: boundary check or if the cell is water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
                
            # Mark the current cell as visited by flipping it to "0"
            grid[r][c] = "0"
            
            # Recursively visit all 4 adjacent directions
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        for r in range(ROWS):
            for c in range(COLS):
                # When we encounter an unvisited piece of land, we found a new island
                if grid[r][c] == "1":
                    islands += 1
                    # Sink the entire island using DFS
                    dfs(r, c)
                    
        return islands