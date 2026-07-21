class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False  # Cycle detected
            
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # Check if there is no cycle starting from node 0 and all nodes are visited
        return dfs(0, -1) and len(visit) == n