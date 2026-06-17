class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Create an adjacency list for all unique characters
        adj = {char: set() for word in words for char in word}
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: If w2 is a prefix of w1 but w1 is longer, it's invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break # Only the first differing character determines the order
                    
        # Track visiting state: True = visiting (in current path), False = visited
        visited = {}
        res = []
        
        def dfs(char):
            if char in visited:
                return visited[char] # Returns True if a cycle is detected
                
            visited[char] = True # Mark as visiting
            
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True # Cycle detected downstream
                    
            visited[char] = False # Mark as fully processed
            res.append(char)
            return False

        # Run DFS for every unique character to handle disconnected components
        for char in adj:
            if dfs(char):
                return ""
                
        # Since we used post-order DFS, reverse the result to get top-sort order
        res.reverse()
        return "".join(res)