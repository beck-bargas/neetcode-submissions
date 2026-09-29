# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('inf'), float('-inf'))

    def isValid(self, root, upper, lower):
        if not root:
            return True
        
        if root.val >= upper or root.val <= lower:
            return False
        
        left = self.isValid(root.left, root.val, lower)
        right = self.isValid(root.right, upper, root.val)

        return left and right
    

        