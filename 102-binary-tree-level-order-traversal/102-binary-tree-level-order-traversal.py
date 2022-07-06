# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.temp = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        self.temp.append(root)
        
        while self.temp:
            node_depth = []
            
            for _ in range(len(self.temp)):
                node = self.temp.pop(0)        
                if node.left: 
                    self.temp.append(node.left)
                if node.right: 
                    self.temp.append(node.right)
                node_depth.append(node.val)

            self.result.append(node_depth)
        
        return self.result