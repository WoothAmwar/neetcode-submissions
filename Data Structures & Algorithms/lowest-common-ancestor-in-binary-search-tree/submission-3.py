# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root, endVal, routeStr):
        if root is None:
            return None
        if root.val == endVal:
            return routeStr
        
        l = self.bfs(root.left, endVal, f"{routeStr}L") 
        r = self.bfs(root.right, endVal, f"{routeStr}R")

        return l if l else r


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_dir = self.bfs(root, p.val, "")
        q_dir = self.bfs(root, q.val, "")
        cur_root = root
        for dir in range(min(len(p_dir), len(q_dir))):
            if p_dir[dir] != q_dir[dir]:
                return cur_root
            if p_dir[dir] == "L":
                cur_root = cur_root.left
            elif p_dir[dir] == "R":
                cur_root = cur_root.right
        return cur_root