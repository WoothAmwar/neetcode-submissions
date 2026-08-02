# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        had_false = False
        # BFS starting from the root
        def bfs(root, depth):
            nonlocal had_false
            if not root:
                return depth-1
            ld = bfs(root.left, depth+1)
            rd = bfs(root.right, depth+1)
            # print(root.val, ld, rd, had_false)
            if abs(ld-rd)>=2:
                had_false=True

            return max(ld, rd)
            
        bfs(root, 0)
        return not had_false