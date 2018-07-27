class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def RecreateTree(self, pre, tin):
        if not pre and tin:
