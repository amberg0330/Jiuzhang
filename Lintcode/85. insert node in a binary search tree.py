"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

# method1: 递归做法
    def insertNode(self, root, node):

        if not root:
            return node
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

# method 2: 非递归法
    def insertNode(self, root, node):
        if not root:
            return node

        cur = root
        while cur != node:
            if node.val < cur.val:
                if cur.left is None:
                    cur.left = node
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                cur = cur.right
            return root
