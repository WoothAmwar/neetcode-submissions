# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        global seen_levels, levels
        levels = []
        seen_levels = 0
        def bft(root, level):
            global seen_levels, levels
            if root is None:
                return
            if level > seen_levels:
                seen_levels += 1
                levels.append([])
            levels[level-1] = root.val
            return bft(root.left, level+1), bft(root.right, level+1)
        bft(root, 1)
        return levels