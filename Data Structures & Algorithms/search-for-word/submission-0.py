class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            # Base Case: Found all characters of the word
            if i == len(word):
                return True
                
            # Base Cases: Out of bounds or character mismatch
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # Save the current character and mark the cell as visited
            temp = board[r][c]
            board[r][c] = ""
            
            # Explore all 4 adjacent directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack: Restore the original character
            board[r][c] = temp
            
            return res

        # Check every starting position in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False