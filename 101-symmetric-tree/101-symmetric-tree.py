# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, leftNode, rightNode):
        if not leftNode and not rightNode: return True
        if not rightNode: return False
        if not leftNode: return False
        if leftNode.val != rightNode.val: return False
        else: return self.isMirror(leftNode.left, rightNode.right) and self.isMirror(leftNode.right, rightNode.left)
        
        