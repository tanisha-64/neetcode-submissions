# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # Compute the maximum path sum of the left and right subtrees
            # Max with 0 ensures we ignore negative paths that would decrease our sum
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # Compute the max path sum WITH a split (current node acts as the bridge/root of the path)
            res = max(res, node.val + leftMax + rightMax)

            # Return the max path sum WITHOUT a split (to be chosen by the parent node)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res