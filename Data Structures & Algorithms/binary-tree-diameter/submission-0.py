# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of a node = diameter of left + diameter of right
        d = 0
        def dfs(root):
            nonlocal d
            if root is None:
                return (0,0)
            l = dfs(root.left)
            r = dfs(root.right)

            l_max = max(l[0], l[1])
            r_max = max(r[0], r[1])
            d = max(d, l_max + r_max)
            # print(root.val, l, r, d)
            return (l_max+1, r_max+1)
        dfs(root)
        return d
