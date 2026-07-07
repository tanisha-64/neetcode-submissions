# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
                
            # Node values must be strictly between low and high bounds
            if not (low < node.val < high):
                return False
            
            # The left child must be smaller than the current node's value
            # The right child must be larger than the current node's value
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
            
        return validate(root, float('-inf'), float('inf'))