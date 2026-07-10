# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map to store the value -> index relation for the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to keep track of the current root element in the preorder array
        pre_idx = 0
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            # Base case: if the current subtree range in inorder is invalid
            if left > right:
                return None
            
            # The first element in the preorder sequence is always the root of the current subtree
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Find the index of this root node in the inorder array to split into subtrees
            pivot = inorder_map[root_val]
            
            # Recursively build the left subtree first, then the right subtree
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)