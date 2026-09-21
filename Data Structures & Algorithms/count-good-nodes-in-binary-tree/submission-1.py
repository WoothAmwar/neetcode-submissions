# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    


    def goodNodes(self, root: TreeNode) -> int:
        global gl
        if root is None:
            return []
        gl = 0

        def seenGreater(root, maxSeen):
            global gl
            if root is None:
                return None
            
            if root.val >= maxSeen:
                gl+=1
                maxSeen = root.val
            
            l = seenGreater(root.left, maxSeen)
            r = seenGreater(root.right, maxSeen)
        seenGreater(root, root.val)
        return gl

            
        