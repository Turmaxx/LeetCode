# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        stack= [root]
        result = []
        
        while stack:
            curNode = stack.pop()
            result.append(curNode.val) 
            if curNode.right: stack.append(curNode.right)
            if curNode.left: stack.append(curNode.left)
                
        return result
               
        # recursive solution
        # def transverse(root, result):
        #     if not root: return []
        #     result.append(result.val)
        #     transverse(root.left, result)
        #     transverse(root.right, result)

        # return transverse(root, [])
            
        # recursive one-liner
        # return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
