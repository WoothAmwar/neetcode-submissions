# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def compare(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None and tree2 is not None:
            return False
        if tree1 is not None and tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.compare(tree1.left, tree2.left) and self.compare(tree1.right, tree2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            # if root.val == subRoot.val:
            #     return self.compare(root, subRoot)
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or self.compare(root, subRoot)
        else:
            return False
        