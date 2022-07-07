# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(leftNode, rightNode):
            if not leftNode and not rightNode: return True
            if not rightNode: return False
            if not leftNode: return False
            if leftNode.val != rightNode.val: return False
            else:  return isMirror(leftNode.left, rightNode.right) and isMirror(leftNode.right, rightNode.left)
                
    
        return isMirror(root.left, root.right)