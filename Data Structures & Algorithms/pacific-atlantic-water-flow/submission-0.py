class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visit, prev_height):
            # Check boundaries, if already visited, or if the current cell is lower than the previous cell
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                (r, c) in visit or heights[r][c] < prev_height):
                return
                
            visit.add((r, c))
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        # 1. Run DFS for the top and bottom rows
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])             # Top row (Pacific)
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # Bottom row (Atlantic)
            
        # 2. Run DFS for the left and right columns
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])             # Left col (Pacific)
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Right col (Atlantic)
            
        # 3. Find the intersection where cells can reach both oceans
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
                    
        return result