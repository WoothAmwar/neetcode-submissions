# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
    
        t = root.right if root.right else None
        root.right = root.left if root.left else None
        root.left = t
        # print(root.left.val if r, root.right.val)

        self.invertTree(root.right)
        self.invertTree(root.left)
        return root