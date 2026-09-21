# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        qu = [root]
        rgl = []

        while qu:
            c_qu = qu
            rgl.append(c_qu[0].val)
            qu = []
            
            for n in c_qu:
                if n.right:
                    qu.append(n.right)
                if n.left:
                    qu.append(n.left)
        return rgl


