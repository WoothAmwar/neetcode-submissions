# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isit = True
        def its(r, s):
            nonlocal isit
            if r and s:
                if r.val != s.val:
                    isit = False
                its(r.left, s.left)
                its(r.right, s.right)
            elif r or s:
                isit=False

        its(p, q)
        return isit       