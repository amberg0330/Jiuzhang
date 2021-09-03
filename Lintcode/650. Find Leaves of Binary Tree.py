# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves,
# repeat until the tree is empty.
#
# Example
# Example1
# Input: {1,2,3,4,5}
# Output: [[4, 5, 3], [2], [1]].
# Explanation:
#
#     1
#    / \
#   2   3
#  / \
# 4   5
# Example2
# Input: {1,2,3,4}
# Output: [[4, 3], [2], [1]].
# Explanation:
#
#     1
#    / \
#   2   3
#  /
# 4

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # 通过孩子推父亲：99%的树的问题都需要通过这种方法求解
        # 母节点的层数 = max(左孩子层数， 右孩子层数) + 1
        lists = []
        self.dfs(root, lists)
        return lists

    def dfs(self, node, lists):
        if node is None:
            # 返回-1很巧妙 父节点 + 1 后变成第0层
            return -1

        left_level = self.dfs(node.left, lists)
        right_level = self.dfs(node.right, lists)
        curr_level = max(left_level, right_level) + 1
        self.add_into_lists(lists, curr_level, node.val)
        return curr_level

    def add_into_lists(self, lists, level, value):
        if level == len(lists):
            lists.append([])
        lists[level].append(value)

