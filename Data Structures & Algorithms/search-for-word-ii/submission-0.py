class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # Avoid duplicate entries
                
            # Temporarily mark the cell as visited
            board[r][c] = "#"
            
            # Explore 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc, next_node)
                    
            # Restore the cell back
            board[r][c] = char
            
            # Optimization: Prune the trie leaf nodes
            if not next_node.children:
                del node.children[char]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return res