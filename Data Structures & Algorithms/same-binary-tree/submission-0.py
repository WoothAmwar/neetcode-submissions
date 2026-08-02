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
                print(r.val, s.val)
                if r.val != s.val:
                    isit = False
                l = its(r.left, s.left)
                t = its(r.right, s.right)
            elif r or s:
                if r:
                    print(r.val, None)
                else:
                    print(None, s.val)
                isit=False

        its(p, q)
        return isit       