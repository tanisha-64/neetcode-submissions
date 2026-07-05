# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty, it's always a subtree of any tree
        if not subRoot: 
            return True
        # If root is empty but subRoot isn't, subRoot cannot be a subtree
        if not root: 
            return False
        
        # Check if the trees are identical starting from the current root
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, check if subRoot is a subtree of the left or right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        # Both are empty -> identical
        if not r and not s:
            return True
        # One is empty, or values don't match -> not identical
        if not r or not s or r.val != s.val:
            return False
        
        # Check structural identity for both left and right children
        return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)