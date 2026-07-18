"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Hash map to store the mapping from old node to new node
        old_to_new = {}
        
        def dfs(current_node):
            # If the node is already cloned, return its clone
            if current_node in old_to_new:
                return old_to_new[current_node]
                
            # Create a copy of the current node
            copy = Node(current_node.val)
            old_to_new[current_node] = copy
            
            # Recursively clone all neighbors
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)