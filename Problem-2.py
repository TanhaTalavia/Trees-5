# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = None
    first = TreeNode()
    last = TreeNode()
    flag = False

    def recoverTree(self, root) :
        """
        Do not return anything, modify root in-place instead.
        """

        self.inorder(root)
        self.first.val, self.last.val = self.last.val, self.first.val

    def inorder(self, root):

        if not root:
            return

        self.inorder(root.left)

        if self.prev and root.val < self.prev.val:
            if not self.flag:
                self.first = self.prev
                self.last = root
                self.flag = True
            else:
                self.last = root

        self.prev = root
        self.inorder(root.right)

